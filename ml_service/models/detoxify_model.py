import torch
import transformers

from ml_service.models.base import BaseToxicityModel
from ml_service.violations import (
    IdentityAttackViolation,
    InsultViolation,
    ObsceneViolation,
    SevereToxicityViolation,
    SexualExplicitViolation,
    ThreatViolation,
    ToxicityViolation,
    Violation,
)

DOWNLOAD_URL = "https://github.com/unitaryai/detoxify/releases/download/"
MODEL_URL = DOWNLOAD_URL + "v0.4-alpha/multilingual_debiased-0b549669.ckpt"

THRESHOLDS = {
    "toxicity": 0.8,
    "severe_toxicity": 0.8,
    "obscene": 0.8,
    "identity_attack": 0.8,
    "insult": 0.8,
    "threat": 0.8,
    "sexual_explicit": 0.8,
}


class DetoxifyModel(BaseToxicityModel):
    def __init__(self, checkpoint=None, device="cpu", huggingface_config_path=None):
        super().__init__()
        self.model, self.tokenizer, self.class_names = load_checkpoint(
            checkpoint=checkpoint,
            device=device,
            huggingface_config_path=huggingface_config_path,
        )
        self.device = device
        self.model.to(self.device)

    @torch.no_grad()
    def predict(self, text):
        self.model.eval()
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, padding=True
        ).to(self.model.device)

        out = self.model(**inputs)[0]
        scores = torch.sigmoid(out).cpu()
        results = {}

        for i, cla in enumerate(self.class_names):
            results[cla] = scores[:, i].squeeze().tolist()

        return results

    def _get_violation(self, cls: str) -> Violation:
        _mapping = {
            "toxicity": ToxicityViolation,
            "severe_toxicity": SevereToxicityViolation,
            "obscene": ObsceneViolation,
            "identity_attack": IdentityAttackViolation,
            "insult": InsultViolation,
            "threat": ThreatViolation,
            "sexual_explicit": SexualExplicitViolation,
        }
        return _mapping[cls]()

    def analyze(self, comment: str) -> set[Violation]:
        results = self.predict(comment)
        violations = set()

        for cls, score in results.items():
            if score > THRESHOLDS[cls]:
                violations.add(self._get_violation(cls))

        return violations


def load_checkpoint(checkpoint=None, device="cpu", huggingface_config_path=None):
    if checkpoint is None:
        checkpoint_path = MODEL_URL
        loaded = torch.hub.load_state_dict_from_url(
            checkpoint_path, map_location=device
        )
    else:
        loaded = torch.load(checkpoint, map_location=device)
        if "config" not in loaded or "state_dict" not in loaded:
            raise ValueError(
                "Checkpoint needs to contain the config it was trained \
                    with as well as the state dict"
            )
    class_names = loaded["config"]["dataset"]["args"]["classes"]
    # standardise class names between models
    change_names = {
        "toxic": "toxicity",
        "identity_hate": "identity_attack",
        "severe_toxic": "severe_toxicity",
    }
    class_names = [change_names.get(cl, cl) for cl in class_names]
    model, tokenizer = get_model_and_tokenizer(
        **loaded["config"]["arch"]["args"],
        state_dict=loaded["state_dict"],
        huggingface_config_path=huggingface_config_path,
    )

    return model, tokenizer, class_names


def get_model_and_tokenizer(
    model_type,
    model_name,
    tokenizer_name,
    num_classes,
    state_dict,
    huggingface_config_path=None,
):
    model_class = getattr(transformers, model_name)
    config = model_class.config_class.from_pretrained(
        model_type, num_labels=num_classes
    )
    model = model_class.from_pretrained(
        pretrained_model_name_or_path=None,
        config=huggingface_config_path or config,
        state_dict=state_dict,
        local_files_only=huggingface_config_path is not None,
    )
    tokenizer = getattr(transformers, tokenizer_name).from_pretrained(
        huggingface_config_path or model_type,
        local_files_only=huggingface_config_path is not None,
    )

    return model, tokenizer

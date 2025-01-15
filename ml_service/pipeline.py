from enum import Enum, auto

from models import BaseToxicityModel, BlacklistModel, ContentFilterModel, DetoxifyModel

from ml_service.violations import Violation, ViolationLevel


class Decision(Enum):
    SKIP = auto()
    WARNING = auto()
    BLOCK = auto()


class ToxicityPipeline:
    def __init__(self, models: list[BaseToxicityModel]):
        self.models = models

    def _get_decision(self, violations: set[Violation]) -> Decision:
        _mapping = {
            ViolationLevel.BASIC: Decision.WARNING,
            ViolationLevel.MEDIUM: Decision.WARNING,
            ViolationLevel.ADVANCED: Decision.BLOCK,
            ViolationLevel.SEVERE: Decision.BLOCK,
        }

        return max(
            (_mapping[violation.level] for violation in violations),
            key=lambda x: x.value,
            default=Decision.SKIP,
        )

    def analyze_comment(self, comment: str) -> tuple[Decision, set[Violation]]:
        decision = Decision.SKIP
        total_violations = set()

        for model in self.models:
            violations = model.analyze(comment)
            decision = max(
                decision, self._get_decision(violations), key=lambda x: x.value
            )
            total_violations.update(violations)

            if decision == Decision.BLOCK:
                return decision, total_violations

        return decision, total_violations

    @classmethod
    def from_basic_models(cls):
        return cls(
            [
                BlacklistModel(blacklist_path="data/profane_words.txt"),
                ContentFilterModel(ad_keywords_path="data/ad_keywords.txt"),
                DetoxifyModel(),
            ]
        )

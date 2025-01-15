from ml_service.models.base import BaseToxicityModel
from ml_service.models.blacklist_checker import BlacklistChecker
from ml_service.violations import BlackListViolation, Violation


class BlacklistModel(BaseToxicityModel):
    def __init__(self, blacklist_path: str, threshold: float = 0.75):
        self.blacklist_checker = BlacklistChecker(blacklist_path)
        self.custom_ad_keywords = set()
        self.threshold = threshold

    def add_ad_keyword(self, words: list[str]) -> None:
        self.blacklist_checker.add_blacklist_words(words)

    def analyze(self, comment: str) -> set[Violation]:
        return (
            {BlackListViolation()}
            if self.blacklist_checker.check_comment(comment) > self.threshold
            else set()
        )

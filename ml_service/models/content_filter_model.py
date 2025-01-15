import re

from ml_service.models.base import BaseToxicityModel
from ml_service.models.blacklist_checker import BlacklistChecker
from ml_service.violations import (
    AdKeywordViolation,
    LinkViolation,
    PhoneNumberViolation,
    PromoCodeViolation,
    SpamViolation,
    Violation,
)


class ContentFilterModel(BaseToxicityModel):
    def __init__(self, ad_keywords_path: str, threshold: float = 0.75):
        self.ad_keywords_checker = BlacklistChecker(ad_keywords_path)
        self.custom_ad_keywords = set()
        self.url_pattern = re.compile(r"https?://\S+|www\.\S+")
        self.promo_code_pattern = re.compile(r"\b[A-Z0-9]{5,10}\b")
        self.phone_pattern = re.compile(r"\+?\d[\d -]{7,14}\d")
        self.spam_pattern = re.compile(r"(.)\1{4,}")
        self.threshold = threshold

    def add_ad_keyword(self, words: list[str]) -> None:
        self.ad_keywords_checker.add_blacklist_words(words)

    def analyze(self, comment: str) -> set[Violation]:
        violations = set()

        if self.url_pattern.search(comment):
            violations.add(LinkViolation())

        if self.promo_code_pattern.search(comment):
            violations.add(PromoCodeViolation())

        if self.phone_pattern.search(comment):
            violations.add(PhoneNumberViolation())

        if self.ad_keywords_checker.check_comment(comment) > self.threshold:
            violations.add(AdKeywordViolation())

        if self.spam_pattern.search(comment):
            violations.add(SpamViolation())

        return violations

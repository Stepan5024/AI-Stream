from enum import Enum


class ViolationLevel(Enum):
    BASIC = "Базовый уровень"
    MEDIUM = "Средний уровень"
    ADVANCED = "Продвинутый уровень"
    SEVERE = "Высокий уровень"


class Violation:
    def __init__(self, level: ViolationLevel, message: str = ""):
        self.level = level
        self.message = message

    def __str__(self):
        return f"{self.level}: {self.message}"


class BasicViolation(Violation):
    def __init__(self, message: str = ""):
        super().__init__(ViolationLevel.BASIC, message)


class MediumViolation(Violation):
    def __init__(self, message: str = ""):
        super().__init__(ViolationLevel.MEDIUM, message)


class AdvancedViolation(Violation):
    def __init__(self, message: str = ""):
        super().__init__(ViolationLevel.ADVANCED, message)


class SevereViolation(Violation):
    def __init__(self, message: str = ""):
        super().__init__(ViolationLevel.SEVERE, message)


class BlackListViolation(BasicViolation):
    def __init__(self):
        super().__init__("Содержит запрещенные слова")


class LinkViolation(BasicViolation):
    def __init__(self):
        super().__init__("Содержит ссылки")


class PromoCodeViolation(BasicViolation):
    def __init__(self):
        super().__init__("Содержит промокоды")


class PhoneNumberViolation(BasicViolation):
    def __init__(self):
        super().__init__("Содержит телефонные номера")


class AdKeywordViolation(BasicViolation):
    def __init__(self):
        super().__init__("Содержит рекламные ключевые слова")


class SpamViolation(BasicViolation):
    def __init__(self):
        super().__init__("Содержит спам (повторяющиеся символы)")


class ToxicityViolation(AdvancedViolation):
    def __init__(self):
        super().__init__("Содержит токсичность")


class ObsceneViolation(AdvancedViolation):
    def __init__(self):
        super().__init__("Содержит непристойности")


class InsultViolation(AdvancedViolation):
    def __init__(self):
        super().__init__("Содержит оскорбления")


class SevereToxicityViolation(SevereViolation):
    def __init__(self):
        super().__init__("Содержит сильно выраженную токсичность")


class IdentityAttackViolation(SevereViolation):
    def __init__(self):
        super().__init__("Содержит посягательство на личность")


class ThreatViolation(SevereViolation):
    def __init__(self):
        super().__init__("Содержит угрозы")


class SexualExplicitViolation(SevereViolation):
    def __init__(self):
        super().__init__("Содержит контент откровенно сексуального характера")

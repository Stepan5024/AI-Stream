from abc import ABC, abstractmethod

from ml_service.violations import Violation


class BaseToxicityModel(ABC):
    @abstractmethod
    def analyze(self, comment: str) -> set[Violation]:
        pass

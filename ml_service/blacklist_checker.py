from rapidfuzz import fuzz, process, utils


class BlacklistChecker:
    def __init__(self, blacklist_path: str):
        self.blacklist_path = blacklist_path
        self.blacklist_words = self._load_blacklist(blacklist_path)

    def _load_blacklist(self, blacklist_path: str) -> set[str]:
        with open(blacklist_path, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file)

    def check_comment(self, comment: str) -> float:
        """
        Checks if a comment contains any blacklisted words or phrases.
        """
        words = comment.lower().split()
        return max(
            process.extractOne(
                word,
                self.blacklist_words,
                scorer=fuzz.WRatio,
                processor=utils.default_process,
            )[1]
            for word in words
        )

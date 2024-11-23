import abc

from twitchio import Message


class FilterController():
    pass


class AbstractMessageFilter(abc.ABC):

    @abc.abstractmethod
    def is_prohibited(self, message: Message):
        pass


class BanWordMessageFilter(AbstractMessageFilter):

    def __init__(self, ban_words):
        self.ban_words = ban_words

    def is_prohibited(self, message: Message):
        return any(w in self.ban_words for w in message.content.strip().split("_"))


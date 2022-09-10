"""Finders grouping in factories."""
from dataclasses import dataclass, field
from typing import List, Optional, Protocol

from app.finders.bot_finders import NotAllowedTGBotFinder
from app.finders.cards_finder import BankCardsFinder
from app.finders.domain_finder import FakeDomainFinder
from app.finders.words_finder import WordsFinder
from app.interfaces import Finder


@dataclass
class FindersResults:
    """Result returned by test_finders factory."""

    finder: Optional[Finder] = None
    results: List[str] = field(default_factory=list)


class FindersFactory(Protocol):
    """Factory interface for Finders grouping."""

    def __init__(self):
        """Finders should be added here."""
        self._finders: List[Finder]

    def find_first_in(self, text: str) -> FindersResults:
        """Find and return first occurrence with its result or empty res."""


class NLPFindersFactory:
    """Factory implementation with all NLP test_finders."""

    def __init__(self):
        self._finders: List[Finder] = [FakeDomainFinder(), NotAllowedTGBotFinder(), BankCardsFinder(), WordsFinder()]

    def find_first_in(self, text: str) -> FindersResults:
        """Find and return first occurrence with its result or empty res."""
        for finder in self._finders:
            results = finder.find(text)
            if results:
                return FindersResults(results=results, finder=finder)
        return FindersResults()

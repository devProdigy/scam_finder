"""Finder for words / sentences."""
from typing import List

import settings


class WordsFinder:
    """Finder for words / sentences."""

    _lowercase_words = [word.lower() for word in settings.env.FORBIDDEN_WORDS]

    def find(self, text: str) -> List[str]:
        """Find in text specific words, case-insensitive.

        Returns: empty list if nothing forbidden found.
        """
        text = text.lower()

        found_words: List[str] = []
        for word in self._lowercase_words:
            if word in text:
                found_words.append(word)

        return found_words

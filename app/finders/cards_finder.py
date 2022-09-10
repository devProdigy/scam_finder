"""Finder for bank cards implementation."""
import re
from collections import Counter
from typing import List

from app.finders.helpers import get_urls


class BankCardsFinder:
    """Finder for bank cards."""

    card_regex_16_numbers = r"(?<!\d)(?:\d{1}[^\d\r\n]{0,5}?){16}(?!\d)"
    card_regex_19_numbers = r"(?<!\d)(?:\d{1}[^\d\r\n]{0,5}?){19}(?!\d)"

    def find(self, text: str) -> List[str]:
        """Find bank cards in text.

        Returns:
            empty list if nothing found, not empty list otherwise.
        """
        possible_cards = self._find_card_candidates(text)
        possible_cards = self._filter_candidates_with_extra_digits_around_them(candidates=possible_cards, text=text)
        possible_cards = self._filter_candidates_in_urls(text=text, candidates=possible_cards)
        return self._filter_exceptional_cards_case(possible_cards)

    def _find_card_candidates(self, text: str) -> List[str]:
        """Find 16 or 19 digit card candidates.

        Regexp is very greedy, so further filtering is required.
        """
        possible_cards_16 = re.findall(self.card_regex_16_numbers, text)
        possible_cards_19 = re.findall(self.card_regex_19_numbers, text)

        return possible_cards_16 + possible_cards_19

    def _filter_candidates_with_extra_digits_around_them(self, text: str, candidates: List[str]) -> List[str]:
        return [x for x in candidates if not self._if_number_near_card_candidate(text=text, candidate=x)]

    def _if_number_near_card_candidate(self, text: str, candidate: str, chars_to_check: int = 3) -> bool:
        """Check if digit could be found near bank card candidate.

        If number found it means that probably it's not a bank card.
        """
        possible_card_length = len(candidate)
        start_card_index = text.index(candidate)
        end_card_index = start_card_index + possible_card_length

        chars_before_start = text[start_card_index - chars_to_check : start_card_index]
        chars_after_start = text[end_card_index : end_card_index + chars_to_check]

        if self._is_number_found(text=chars_before_start, reverse=True) or self._is_number_found(
            text=chars_after_start
        ):
            return True
        return False

    @staticmethod
    def _is_number_found(text: str, reverse: bool = False) -> bool:
        """Return True if number was found, False otherwise."""
        end_of_line_chars = ("\n", "\n\r")
        text = text[::-1] if reverse else text

        for char in text:
            if char in end_of_line_chars:
                return False
            if char.isdigit():
                return True
        return False

    def _filter_candidates_in_urls(self, text: str, candidates: List[str]) -> List[str]:
        if not candidates:
            return []

        urls = get_urls(text=text)
        if not urls:
            return candidates

        for card in candidates[:]:
            if self._is_card_in_urls(urls=urls, card=card):
                candidates.remove(card)

        return candidates

    @staticmethod
    def _is_card_in_urls(urls: List[str], card: str) -> bool:
        for url in urls:
            if card in url:
                return True
        return False

    @staticmethod
    def _filter_exceptional_cards_case(candidates: List[str]) -> List[str]:
        """Return new list of cards filtered from edge cases.

        Cases:
            - '06:50-15:30 i 09:50-18:30'
            - '12.30 - 13.00 15.00-15.30'
            - '27.04, 30.04, 04.05, 07.05'
        """
        filtered_cards = candidates[:]

        for card in candidates:
            counted_chars = Counter(card)
            if (counted_chars[":"] == 4 or counted_chars["."] == 4) \
                    and (counted_chars["-"] == 2 or counted_chars[","] == 3):
                filtered_cards.remove(card)

        return filtered_cards

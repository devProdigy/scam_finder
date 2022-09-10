"""Finders for different types of bots."""
import re
from typing import List

import settings

BOT_CHAR_TO_REPLACE = "@"


class NotAllowedTGBotFinder:
    """Finder for bot-like Telegram entities."""

    bot_finder_regex = r"\b[\w\-\+\!]*bot\b"

    def find(self, text: str) -> List[str]:
        """Find in text bot-like names that ends with 'bot', case-insensitive.

        Returns: empty list if nothing forbidden found.
        """
        text = text.lower()

        found_bots = re.findall(self.bot_finder_regex, text, flags=re.IGNORECASE)
        found_bots = [x.strip() for x in found_bots]

        allowed_bot_names = self._get_allowed_bot_names_lowercase()
        if not allowed_bot_names:
            return found_bots

        for bot_name in found_bots[:]:
            if bot_name in allowed_bot_names:
                found_bots.remove(bot_name)

        return found_bots

    @staticmethod
    def _get_allowed_bot_names_lowercase() -> List[str]:
        """Return allowed bots.

        Replaces @ from the names."""
        allowed_bot_names = settings.env.ALLOWED_BOT_NAMES
        return [name.replace(BOT_CHAR_TO_REPLACE, "").lower().strip() for name in allowed_bot_names]

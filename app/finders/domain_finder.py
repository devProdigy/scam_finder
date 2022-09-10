"""Finders for faking domain."""
from typing import List, Optional

from tldextract import tldextract

import settings
from app.finders.helpers import get_urls


class FakeDomainFinder:
    """Finder for faking domain."""

    possible_domain_fakes = settings.env.DOMAINS_USUALLY_FAKED

    def find(self, text: str) -> List[str]:
        """Look for faked domain in text urls (by adding it subdomain).

        Note: works mostly with HTML urls but can find url in ordinary text too.

        Examples:
        - bank.sub1.sub2.fake.com - FOUND
        - sub1.bank.sub2.fake.com - FOUND
        - https://sub.bank.ua/ - OK
        - https://bank.fake.cc/g/123 - FOUND
        - https://bank-fake.org/r/123 - OK, use another approach instead
        - https://bank.fake.online/123 - FOUND

        Returns:
            [] if nothing found OR [faked_url].
        """
        urls = get_urls(text=text)
        if not urls:
            return []

        faked_domains = []
        for url in set(urls):
            extracted_domain_data = tldextract.extract(url)
            subdomains: str = extracted_domain_data.subdomain  # example of subs: "sub1.bank.sub2"
            faked_subdomain = self._find_faked_domain_in_subdomain(subdomains)
            if faked_subdomain is not None:
                faked_domains.append(url)

        return faked_domains

    def _find_faked_domain_in_subdomain(self, subdomains: str) -> Optional[str]:
        for domain in self.possible_domain_fakes:
            if domain in subdomains:
                return domain
        return None

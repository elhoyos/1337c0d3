# uv run subdomain_visit_count.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import re

def subdomainVisits(cpdomains):
    visits_by_domain = {}
    for cpdomain in cpdomains:
        count, domain = cpdomain.split(' ')
        count = int(count)
        parts = re.split(r'((?:\w+\.)?(\w+\.(\w+)))$', domain)
        parts = set(part for part in parts if part)
        for part in parts:
            visits_by_domain[part] = visits_by_domain.get(part, 0) + count

    return [f"{count} {part}" for part, count in visits_by_domain.items()]

def test():
    tests = [
        [
            ["9001 discuss.leetcode.com"],
            ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]
        ],
        [
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
            ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]
        ],
        [
            ["1 mail.yahoo.com", "50 yahoo.com"],
            ["1 mail.yahoo.com", "51 yahoo.com", "51 com"]
        ]
    ]

    for cpdomains, exp in tests:
        res = subdomainVisits(cpdomains)
        exp.sort()
        res.sort()
        if exp != res:
            raise RuntimeError(f"Unexpected result want={exp}, got={res}")


if __name__ == "__main__":
    test()

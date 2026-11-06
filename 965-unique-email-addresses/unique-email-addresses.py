class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local.split('+')[0]
            local = local.replace('.', '')
            seen.add((local, domain))
        return len(seen)
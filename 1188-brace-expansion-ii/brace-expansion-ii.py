class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        groups = [[]]
        level = 0
        start = 0

        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    sub_res = self.braceExpansionII(expression[start:i])
                    groups[-1].append(sub_res)
            elif level == 0:
                if c == ',':
                    groups.append([])
                else:
                    groups[-1].append([c])

        res = set()
        for group in groups:
            cur = {""}
            for part in group:
                cur = {a + b for a in cur for b in part}
            res.update(cur)

        return sorted(list(res))
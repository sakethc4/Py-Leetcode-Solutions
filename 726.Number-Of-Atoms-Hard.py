from collections import defaultdict

class Solution: # O(N) Time & O(N) Space. 
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            nonlocal i
            count = defaultdict(int)
            while i < len(formula):
                if formula[i] == '(':
                    i += 1
                    inner_count = parse()
                    num = 0
                    while i < len(formula) and formula[i].isdigit():
                        num = num * 10 + int(formula[i])
                        i += 1
                    for name, c in inner_count.items():
                        count[name] += c * (num or 1)
                elif formula[i] == ')':
                    i += 1
                    return count
                else:
                    name = formula[i]
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        name += formula[i]
                        i += 1
                    num = 0
                    while i < len(formula) and formula[i].isdigit():
                        num = num * 10 + int(formula[i])
                        i += 1
                    count[name] += num or 1
            return count

        i = 0
        count = parse()
        return ''.join(name + (str(count[name]) if count[name] > 1 else '')
                       for name in sorted(count))
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        new_allowed = set(allowed)
        count = 0

        for word in words:
            is_consistent = True

            for ch in word:
                if ch not in new_allowed:
                    is_consistent = False
                    break

            if is_consistent:
                count += 1

        return count
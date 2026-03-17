from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []

        for log in logs:
            log = log.strip()   # remove leading/trailing spaces
            identifier, words = log.split(maxsplit=1)

            if words[0].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda log: (log.split(maxsplit=1)[1], log.split(maxsplit=1)[0]))

        return letter_logs + digit_logs
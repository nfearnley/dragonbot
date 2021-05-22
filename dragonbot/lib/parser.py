from typing import Tuple


class StringParser:
    def __init__(self, data: str):
        self.index = 0
        self.data = data

    def skip_spaces(self):
        while self.data[self.index:self.index + 1].isspace():
            self.index += 1

    def get(self, n=1):
        start, end = self._range(n)
        self.index = end
        return self.data[start:end]

    def peek(self, n: int = 1) -> str:
        start, end = self._range(n)
        return self.data[start:end]

    def _range(self, n: int) -> Tuple[int, int]:
        if n < 0:
            n = 0
        start = self.index
        end = self.index + n
        if end > len(self.data):
            end = len(self.data)
        return start, end

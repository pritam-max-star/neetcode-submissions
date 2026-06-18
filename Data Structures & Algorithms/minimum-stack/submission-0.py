class MinStack:

    def __init__(self):
        self.stk = []  # each entry: (value, min_so_far)

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            current_min = self.stk[-1][1]
            self.stk.append((val, min(current_min, val)))

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]
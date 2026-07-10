class MinStack:
    def __init__(self):
        self.arr = []
        self.minstack = []

    def push(self, val: int) -> None:
            self.arr.append(val)
            if self.minstack:
                if val <= self.minstack[-1]:
                    self.minstack.append(val)
            else:
                self.minstack.append(val)

    def pop(self) -> None:
        if self.arr:
            if self.minstack and self.minstack[-1] == self.arr[-1]:
                del(self.minstack[-1])
            del(self.arr[-1])


    def top(self) -> int:
        if self.arr:
            return self.arr[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        elif self.arr:
            return self.arr[-1]
            
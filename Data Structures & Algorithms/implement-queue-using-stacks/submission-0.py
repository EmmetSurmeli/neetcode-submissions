class MyQueue:

    def __init__(self):
        self.queue = [[] for _ in range(10)]
        self.size = 0
    def push(self, x: int) -> None:
        if len(self.queue) == self.size:
            self.queue = self.queue + [[0] for i in range(self.size)]
        self.queue[self.size] = x
        self.size += 1

    def pop(self) -> int:
        val = self.queue[0]
        self.queue = self.queue[1: ]
        self.size -= 1
        return val

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
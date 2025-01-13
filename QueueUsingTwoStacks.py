class QueueWTwoStacks:
    def __init__(self):
        self.s1 = []  
        self.s2 = []  

    def enqueue(self, value):
        self.s1.append(value)

    def dequeue(self):
        self._shift_stacks()
        if self.s2:
            self.s2.pop()

    def front(self):
        self._shift_stacks()
        if self.s2:
            return self.s2[-1]

    def _shift_stacks(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

if __name__ == "__main__":
    q = int(input().strip())  
    queue = QueueWTwoStacks()

    for _ in range(q):
        query = input().strip().split()
        command = int(query[0])

        if command == 1:
            value = int(query[1])
            queue.enqueue(value)
        elif command == 2:
            queue.dequeue()
        elif command == 3:
            print(queue.front())

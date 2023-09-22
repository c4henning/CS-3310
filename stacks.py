class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, item):
        self.__stack.append(item)
        print(f"pushed item: {item}")

    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        else:
            item = self.__stack.pop()
            return item

    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.__stack[-1]

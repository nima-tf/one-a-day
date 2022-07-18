from typing import List

class Stack:
    def __init__(self) -> None:
        self.elements = []
        self.__top : int = -1;

    def isEmpty(self) -> bool:
        return self.__top < 0

    def __append(self, value) -> None:
        self.__top += 1
        self.elements[self.__top] = value

    def size(self):
        return self.__top + 1

    def push(self, value) -> None:
        self.elements.append(value)
        self.__top += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack.")
        else:
            self.__top -= 1
            return self.elements.pop()
    
    def next(self):
        return self.elements[self.__top]

    def show(self) -> List[any]:
        return self.elements






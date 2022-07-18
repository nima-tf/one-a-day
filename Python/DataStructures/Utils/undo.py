from Structures.stack import Stack

class Undo:
    def __init__(self) -> None:
        self.action_memory = Stack()
        self.undo_memory = Stack()

    def do(self, action: str) -> None:
        self.action_memory.push(action)

    def undo(self) -> None:
        self.undo_memory.push(self.action_memory.pop())

    def redo(self) -> None:
        self.action_memory.push(self.undo_memory.pop())

    def show(self) -> Stack:
        return self.action_memory.show()

    def undo_memory_size(self):
        return self.action_memory.size()

    def redo_memory_size(self):
        return self.undo_memory.size()
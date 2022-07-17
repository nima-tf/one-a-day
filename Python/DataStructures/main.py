from Utils.undo import Undo
import random


def main():
    action_history_manager = Undo()
    for i in range(10):
        action_history_manager.do(random_action)
    
    print("Undo actions: ", action_history_manager.undo_memory_size())
    print("Redo actions: ", action_history_manager.redo_memory_size(), "\n")
    
    for j in range(3):
        action_history_manager.undo()
    
    print("Undo actions: ", action_history_manager.undo_memory_size())
    print("Redo actions: ", action_history_manager.redo_memory_size(), "\n")

    for k in range(2):
        action_history_manager.redo()
    
    print("Undo actions: ", action_history_manager.undo_memory_size())
    print("Redo actions: ", action_history_manager.redo_memory_size())


def random_action() -> str:
    return str(random.randint(0,100))

if __name__ == "__main__":
    main()

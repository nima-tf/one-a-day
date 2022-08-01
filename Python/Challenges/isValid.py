from typing import ChainMap


def isValid(s: str) -> bool:
    char_map = {"[" : "]", "{" : "}", "(" : ")"}
    for i, c in enumerate(s):
        if not c in char_map:
            return False
        if char_map[c] != s[-(i+1)]:
            return False
        return True



def main(): 
    valid_string = "()[]{}"
    invalid_string = "([)]"
    print("Valid string returns: ", isValid(valid_string))
    print("Invalid string returns: ", isValid(invalid_string))
    


if __name__ == "__main__":
    main()

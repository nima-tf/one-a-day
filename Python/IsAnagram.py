def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for char in countS:
        if countS[char] != countT.get(char, 0):
            return False
    return True

def isAnagramPythonic(s: str, t: str) -> bool:
    if sorted(s) == sorted(t): return True
    return False

def main(): 
    s = input("Enter the first word: ")
    t = input("Enter the second word: ")
    
    print("It is an anagram" if isAnagram(s, t) else "It is not an anagram")
    print("Yep, still an anagram" if isAnagramPythonic(s, t) else "NOOOO!")
    

if __name__ == "__main__":
    main()




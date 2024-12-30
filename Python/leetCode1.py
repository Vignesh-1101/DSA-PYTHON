from typing import List


def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    for i, word in enumerate(sentence.split(), 1):
        if word.startswith(searchWord):
            print("ass" in "mass")
            # print(word[0] == searchWord[0])
            return i
    return -1

# print(isPrefixOfWord("i love eating burger", "burg"))

def stringMatching(words: List[str]) -> List[str]:
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return result
# print(stringMatching(["mass","as","hero","superhero"]))    
s = "aabcde"
goal = "cdeaab"
def stringMatching(s: str, goal: str) -> bool:
    for i in range(len(s)):
        print(s[i:] + s[:i])
        if s[i:] + s[:i] == goal:
            return True
    return False

# print(stringMatching(s, goal))
def repeatedSubstringPattern(s: str) -> bool:
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0:
            print(s[:i])
            if s[:i] * (len(s) // i) == s:
        # if s[:i] == s[i:]:
                return True
    return False

# print(repeatedSubstringPattern("ababab"))

def maxRepeating(sequence: str, word: str) -> int:
    max_count = 0
    # i = 0
    # while i < len(sequence):
    #     if sequence[i:i + len(word)] == word:
    #         max_count += 1
    #         i += len(word)
    #     else:
    #         i += 1
    # return max_count
    # for i in range(0, len(sequence), len(word)):
    #     print(i)
    #     print(sequence[i:i + len(word)])
    #     if sequence[i:i + len(word)] == word:
    #         max_count += 1
    for i in range(len(sequence) - len(word) + 1):
        print(len(sequence) - len(word) + 1)
        if sequence[i:i + len(word)] == word:
            max_count += 1
    return max_count

print(maxRepeating("aaaba.aaaba.aaba.aaaba.aaaba.aaaba.aaaba", "aaaba"))


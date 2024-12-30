def letter_case_permutation(s):
    def backtrack(index, current):
        # If we've reached the end of the string, add the result
        if index == len(s):
            result.append("".join(current))
            return
        
        # If the current character is a letter, branch for both cases
        if s[index].isalpha():
            # Lowercase
            current.append(s[index].lower())
            backtrack(index + 1, current)
            current.pop()
            # Uppercase
            current.append(s[index].upper())
            backtrack(index + 1, current)
            current.pop()
        else:
            # If it's not a letter, just append it as is
            current.append(s[index])
            backtrack(index + 1, current)
            current.pop()

    result = []
    backtrack(0, [])
    return result


def letterCasePermutation( s: str):
    result = [""]

    for c in s:
        temp = []

        if c.isalpha():
            for r in result:
                temp.append(r + c.lower())
                temp.append(r + c.upper())
            
        else:
            for r in result:
                temp.append(r + c)

        result = temp

    return result

s = "a1b2"
output = letterCasePermutation(s)
print(output)
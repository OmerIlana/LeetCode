from collections import deque

parentheses = {"}":"{", ")":"(", "]":"["} 

def isOpeningParenthese(letter):
    return letter in parentheses.values()

def isClosingParenthese(letter):
    return letter in parentheses.keys()

def isBalanced(given_str):
    seen_parentheses = deque()
    for letter in given_str:
        if isOpeningParenthese(letter):
            seen_parentheses.append(letter)
        elif isClosingParenthese(letter):
            if (seen_parentheses) and (seen_parentheses[-1] == parentheses[letter]):
                seen_parentheses.pop()
            else:
                return False
    
    return not seen_parentheses

assert(isBalanced(""))
assert(isBalanced("abcf"))
assert(isBalanced("[](){}"))
assert(not isBalanced("("))
assert(not isBalanced("}"))
assert(isBalanced("{{[][]()}}"))
assert(not isBalanced("{{[][]s}()}}"))
assert(not isBalanced('[](){([[[]]])}('))
assert(isBalanced('[{{{(())}}}]((()))'))
assert(not isBalanced('[[[]])]'))
    
print("Success")



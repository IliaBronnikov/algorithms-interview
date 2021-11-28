# String

+ [Valid Palindrome](#valid-palindrome)
+ [Valid Parentheses](#valid-parentheses)
<!--  -->
## Valid Palindrome
## Valid Parentheses

https://leetcode.com/problems/valid-palindrome/

```python
def isPalindrome(self, s: str) -> bool:
    r = re.sub('[^a-zA-Z0-9]', '', s)
    if len(r) == 1:
        return True
    r = r.lower()
    for i in range(len(r)//2):
        if r[i] != r[-i-1]:
            return False
    return True    
```

https://leetcode.com/problems/valid-parentheses/

```python
def isValid(self, s: str) -> bool:
    if len(s) < 2 or len(s)%2 == 1:
        return False
    brackets_dict = {'[':']','{':'}','(':')'}
    if len(s) == 2 and s[0] in list(brackets_dict.keys()) and s[1] == brackets_dict[s[0]]:
        return True
    elif len(s) == 2:
        return False

    start = []

    for i in s:
        if i in list(brackets_dict.keys()):
            start.append(i)
            continue
        if len(start) == 0 or i != brackets_dict[start[-1]]:
            return False
        else:
            del start[-1]
    if len(start) == 0:
        return True
    else:
        return False 
```

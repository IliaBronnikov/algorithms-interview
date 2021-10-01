# String

+ [Valid Palindrome](#valid-palindrome)
<!--  -->
## Valid Palindrome

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

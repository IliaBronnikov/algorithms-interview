# String

+ [Valid Palindrome](#valid-palindrome)
+ [Valid Parentheses](#valid-parentheses)
+ [Shortest distans XY](#shortest-distans-xy)
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

## Valid Parentheses

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

## Shortest distans XY

- Дана строка, состоящая из букв 'X', 'Y' и 'O'.
- Необходимо найти кратчайшее расстояние между буквами 'X' и 'Y', либо вывести 0, если 'X' либо 'Y' отсутствуют.
- Дистанция между двумя рядом стоящими буквами считается как 1 (одно межбуквенное расстояние)
- Дистанция может считаться в обе стороны
- X00XY -> 1
- XY -> 1

```python
def xy_dist(string):
    act_count = 0
    count = 0
    start = None
    if len(string) > 1
        for char in string:
            if start == None:
                if char == "X":
                    start = "X"
                    end = "Y"
                elif char == "Y":
                    start = "Y"
                    end = "X" 
                else:
                    continue       
            count += 1
            if char == end:
                start, end = end, start
                if act_count > count or act_count == 0:
                    act_count = count - 1
                count = 0    
                continue
            elif char == start:
                count = 0
        return act_count
    else:
        return 0
```

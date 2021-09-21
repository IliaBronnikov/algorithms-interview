#String

+ [Valid Palindrome](#valid-palindrome)
+ [Valid Palindrom](#valid-palindrom)

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

## Valid Palindrom

https://leetcode.com/problems/valid-palindrom/

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return head

    rev_list = []
    cop = head

    while head is not None:
        rev_list.append(head.val)
        head = head.next

    if len(rev_list) == 1:
        return cop

    back = ListNode()
    back.next = ListNode(list(reversed(rev_list))[-1])
    back.val = list(reversed(rev_list))[-2]
    for i in list(reversed(rev_list))[-3::-1]:
        back = ListNode(i,next = back)

    return back
```

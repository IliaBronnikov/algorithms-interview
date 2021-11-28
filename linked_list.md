# Linked-list

+ [Reverse Linked List](#reverse-linked-list)

## Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


https://leetcode.com/problems/reverse-linked-list/

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

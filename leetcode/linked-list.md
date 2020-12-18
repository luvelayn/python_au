+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
<!-----solution----->

## Sort List

https://leetcode.com/problems/sort-list/

```python
def sortList(self, head: ListNode) -> ListNode:
    if head == None:
        return None

    h1, h2 = self.split(head)
    if h1 == None or h2 == None:
        return self.merge(h1, h2)
    return self.merge(self.sortList(h1), self.sortList(h2))

def split(self, h: ListNode):
    start = ListNode()
    start.next = h
    slow = start
    fast = start

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    slownext = slow.next
    slow.next = None
    return start.next, slownext

def merge(self, h1: ListNode, h2: ListNode):
    start = ListNode()
    p = start
    while h1 != None and h2 != None:
        if h1.val < h2.val:
            p.next = h1
            h1 = h1.next
        else:
            p.next = h2
            h2 = h2.next
        p = p.next

    while h1 != None:
        p.next = h1
        h1 = h1.next
        p = p.next

    while h2 != None:
        p.next = h2
        h2 = h2.next
        p = p.next

    return start.next
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    heada = headA
    headb = headB

    while heada or headb:

        if heada == None:
            heada = headB
            headb = headb.next

        elif headb == None:
            headb = headA
            heada = heada.next

        elif heada == headb:
            return heada

        elif heada or headb:
            heada = heada.next
            headb = headb.next
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
def reorderList(self, head: ListNode) -> None:
    if not head:
        return

    slow = fast = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    if slow == fast:
        return

    h2 = slow.next
    slow.next = None
    prev = None
    while h2:
        nxt = h2.next
        h2.next = prev
        prev = h2
        h2 = nxt

    h1, h2 = head, prev
    prev = None

    while h1 and h2:
        if prev:
            prev.next = h1
        h1nxt = h1.next
        h1.next = h2
        prev = h2
        h1, h2 = h1nxt, h2.next

    if h1:
        prev.next = h1
    if h2:
        prev.next = h2
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
    if not head:
        return False

    fast = head
    slow = head
    start = True

    while slow and fast and fast.next:
        if not start and fast == slow:
            return True
        start = False
        fast = fast.next.next
        slow = slow.next

    return False
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break


    if fast is None or fast.next is None:
        return None

    fast = head

    while slow != fast:
        slow = slow.next
        fast = fast.next


    return slow
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    count = 1
    prev, cur, ptr = None, None, head
    while(ptr):
        if count == n:
            cur = head
        elif count > n:
            prev = cur
            cur = cur.next

        ptr = ptr.next
        count += 1

    if cur is None:
        return head
    if prev is None:
        return head.next

    prev.next = cur.next
    return head
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 and not l2:
        return

    l3 = ListNode()
    res = l3
    while l1 and l2:
        if l1.val < l2.val:
            l3.val = l1.val
            l1 = l1.next
        else:
            l3.val = l2.val
            l2 = l2.next

        l3.next = ListNode()
        l3 = l3.next

    if l1 and not l2:
        l3.val = l1.val
        l3.next = l1.next

    if l2 and not l1:
        l3.val = l2.val
        l3.next = l2.next

    return res
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def isPalindrome(self, head: ListNode) -> bool:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    slow = head
    fast = slow
    while fast and fast.next:
        fast = fast.next
        if fast: fast = fast.next
        slow = slow.next
    return slow
```

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
s Solution:
def reverseList(self, head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
```
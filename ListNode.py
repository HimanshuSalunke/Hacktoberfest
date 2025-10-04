class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    @staticmethod
    def merge_sorted(l1, l2):
        dummy = ListNode(0)
        tail = dummy
        a = l1.head
        b = l2.head
        while a and b:
            if a.val <= b.val:
                tail.next = ListNode(a.val)
                a = a.next
            else:
                tail.next = ListNode(b.val)
                b = b.next
            tail = tail.next
        while a:
            tail.next = ListNode(a.val)
            a = a.next
            tail = tail.next
        while b:
            tail.next = ListNode(b.val)
            b = b.next
            tail = tail.next
        res = SinglyLinkedList()
        res.head = dummy.next
        return res

def main():
    l = SinglyLinkedList()
    for i in [1,2,3,4,5]:
        l.append(i)
    print("List", l.to_list())
    l.reverse()
    print("Reversed", l.to_list())
    l2 = SinglyLinkedList()
    for i in [2,4,6]:
        l2.append(i)
    merged = SinglyLinkedList.merge_sorted(l, l2)
    print("Merged", merged.to_list())
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    c.next = b
    cl = SinglyLinkedList()
    cl.head = a
    print("Cycle detected:", cl.detect_cycle())

if __name__ == "__main__":
    main()

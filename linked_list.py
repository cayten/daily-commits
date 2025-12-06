class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def delete(self, value):
        cur = self.head
        prev = None
        while cur:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def find(self, value):
        cur = self.head
        idx = 0
        while cur:
            if cur.value == value:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

def demo():
    ll = LinkedList()
    for x in [3, 5, 7]:
        ll.append(x)
    ll.prepend(1)
    print("List:", ll.to_list())
    print("Find 5 ->", ll.find(5))
    print("Delete 3 ->", ll.delete(3))
    print("After delete:", ll.to_list())

if __name__ == "__main__":
    demo()

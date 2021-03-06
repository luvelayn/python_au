class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class HexNumber:

    def __init__(self, num):
        """

        :type num: str
        """
        cur = Node(num[-1])
        self.head = cur
        self.len = len(num)
        for i in range(1, len(num)):
            cur.next = Node(num[::-1][i])
            cur = cur.next

    def __str__(self):
        res = ""
        head = self.head
        for i in range(self.len):
            head.value = str(head.value)
            res = res + head.value
            head = head.next
        return res

    def to_decimal(self):
        node = self.head
        while node:
            if 'A' <= str(node.value) <= 'F':
                node.value = ord(str(node.value)) - ord('A') + 10
            else:
                node.value = node.value
            node = node.next
        return self

    def to_hex(self):
        node = self.head
        while node:
            if int(node.value) > 9:
                node.value = chr(ord('A') + int(node.value) - 10)
            else:
                node.value = chr(ord('0') + int(node.value))
            node = node.next
        return self

    def add(self, second):
        pass


def main(num1, num2):
    num1 = HexNumber(num1)
    num2 = HexNumber(num2)
    num3 = num1.add(num2)
    print(num3)


if __name__ == '__main__':
    pass

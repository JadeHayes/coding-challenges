"""Given linked list head node, return head node of new, reversed linked list.

For example:

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
"""


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """
    # set the head to output to none
    out_head = None
    # set variavble n to the current head
    n = head

    # while there is a value "n" that can be passed through
    # out_head is now the Node with the current data and the next is out_head
    # n is now the next node in the ll
    while n:
        # creating a node with the current data and out_head as next
        # out_head is not pointing to a single node object
        # first node is Node(1,none)
        # second node is 2, Node(1,none)
        out_head = Node(n.data, out_head)
        n = n.next
    return out_head


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"

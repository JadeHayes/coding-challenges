  class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]

    def find_max(self):
        """Find the max num in the stack"""
        max_num = 0

        if self.peek:
            return max(self.items)


class Queue_stack(object):
    def dequeue():
        """first item in the stack will come out"""
        if not self.next:
                return None
        # While loop to pop
        # add the pop to a new stack



        # test cases 
        # gurav@box.com






    def enqueue():
        """adding to the queue at the end""
        # similar to push



class Node(object):
    '''Setting a node class for out linked list '''
    
    def __init__(self, next, data):
        self.next = next
        self.data = int(data)
        

        
'''Create a function that tells us the duplicates'''
# Always getting the head of the linked list
# look through the list and find duplicate integer
# return the duplicate integer
# assume there is only one

# [2,3,1,3] -- > 3
# [4,5,6] --> "No duplicates here"
# [-1, -2, 2, -1] --> -1

# create a function that takes in the head llst
# create a variable called seen, list of the data we've already visited
# if the current node.data is in the seen list
# return node.data

test1 = [2,3,1,3]
test2 = [4,5,6,7]
test3 = [-1, -2, 2, -1]



two = Node(None, 2)
three = Node(None, 3)
one = Node(None, 1)
three2 = Node(None, 3)

two.next = three
three.next = one
one.next = three2
three2.next = None

def find_duplicate(node, seen=set()):
    """Find the duplicate in the list assuming there is only one duplicate"""
    
    # If we found data already in seen, return data back to you     
    if node.data in seen:
        return node.data
    
    # If there is no next node, return no duplicates     
    elif not node.next:
        return "No duplicates here"    

    seen.add(node.data)

    # return a function call with seen variable     
    return find_duplicate(node.next, seen)

print find_duplicate(two)
# define class stack_linkedlist which creates a stack based on linked list.
# functions for stack implemented by linked list run on O(1) time complexity.
class stack_linkedlist:
    class node:                                   # define class node for the stack which stores reference to the data and the pointer to the the next node.
        def __init__(self, data, reference):      # initialize node.
            self._data = data
            self._reference = reference
    def __init__(self):                           # initialize stack.
        self._listhead = None
        self._length = 0
    def push(self, l):                            # creates a new head node and insert l as data and put its reference to previous head node.
        self._length += 1
        self._listhead = self.node(l, self._listhead)
    def pop(self):                                # assigns head node to the reference of previous head and returns previous head node data.
        self._length -= 1
        return_value = self._listhead._data
        self._listhead = self._listhead._reference
        return return_value
    def _len_(self):                              # returns length of the stack.
        return self._length
    def is_empty(self):                           # checks if the stack is empty.
        return self._length == 0
    def top(self):                                # returns top element of the stack.
        return self._listhead._data
    

# helper function
def find_number(l, i):                            # it returns the number before the bracket opening in the form of string.
    if l[i+1].isdigit():
        return l[i] + find_number(l, i + 1)
    else:
        return l[i]




def findPositionandDistance(l):                  # main function which takes in string and returns the required parameters in O(n) time complexity.
    s = stack_linkedlist()                       # stack s stores the numbers that come before brackets in form of stack so that they can be divided on multiplyer in order.
    v = 1                                        # multiplyer number v which gets incremented in x y and z respectively with initial value 1.
    x_coordinate = 0
    y_coordinate = 0                        # required variables
    z_coordinate = 0
    distance = 0
    i = 0                                        # initialising loop on string.
    while i < len(l):
        if l[i] == "+":
            if l[i+1] == "X":
                x_coordinate += v
                distance += v
            elif l[i+1] == "Y":
                y_coordinate += v
                distance += v
            elif l[i+1] == "Z":             # addition/subtraction of v as per conditions.
                z_coordinate += v
                distance += v
            i += 2 
        elif l[i] == "-":
            if l[i+1] == "X":
                x_coordinate -= v
                distance += v
            elif l[i+1] == "Y":
                y_coordinate -= v
                distance += v
            elif l[i+1] == "Z":
                z_coordinate -= v
                distance += v
            i += 2
        elif l[i] == ")":                # operations on closing of bracket.
            v = v//s.top()               # divide multiplyer by previously multiplyed value.
            s.pop()                      # remove that value from divider stack.
            i += 1
        elif l[i].isdigit() and not l[i-1].isdigit():       # detecting number before bracket and multiplying that with v.
            v *= eval(find_number(l, i))                    # mutiplying the number to v and setting this as the new multiplyer.
            s.push(eval(find_number(l, i)))                 # pushing that number in stack to divide later on bracket closing.
            i += len(find_number(l, i)) + 1
            
    return [x_coordinate, y_coordinate, z_coordinate, distance]

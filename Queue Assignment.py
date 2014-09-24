class Queue1:
    def __init__(self):
        self.q = []

    def add(self, item):
        self.q.append(item)

    def remove(self):
        return self.q.pop(0)

    def isEmpty(self):
        return len(self.q) == 0


#more efficient Queue2 with an updated remove


class Queue2:
    def __init__(self, lst = []):
        self.front = self.back = None
        for elt in lst:
            self.add(elt)

    def __repr__(self):
        lst = []
        ptr = self.front
        while ptr != None:
            lst.append(ptr.value)
            ptr = ptr.next
        return "Queue2(" + str(lst) + ")"

    def add(self, item):
        self.back = Node(item, self.back)
        if self.isEmpty():
            self.front = self.back
#Optimization of remove func
    def remove(self):
        toRemove = self.front
        self.front = self.front.next
        return toRemove.value

    def isEmpty(self):
        return self.front == None

class Node(object):
    def __init__(self, value, before):
        if before != None:
            before.next = self
        self.value = value
        self.next = None

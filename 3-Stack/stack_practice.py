class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from empty Stack")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __repr__(self):
        return f'{self.stack}'


s = Stack()
s.push('1')
s.push('2')

print(s.__repr__())
print(s.pop())
print(s.peek())
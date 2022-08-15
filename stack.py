import sys

class Stack:
    def __init__(self, limit=32):
        self.stack = []
        self.limit = limit

    def push(self, n):
        if len(self.stack) >= self.limit:
            print("stack is overflow")
            return False
        self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty.")
            return False
        return self.stack.pop()
    def answer(self):
        return self.stack[0]

st = Stack()
c = ''
x = ''
while c != '\n':
    c = sys.stdin.read(1)
    if c.isdigit():
        x += c
    elif c == ' ' or c == '\t':
        if x:
            st.push(int(x))
            x = ''
        continue
    elif c == '+':
        b = st.pop()
        a = st.pop()
        st.push(a + b)
    elif c == '-':
        b = st.pop()
        a = st.pop()
        st.push(a - b)
    elif c == '*':
        b = st.pop()
        a = st.pop()
        st.push(a * b)
    elif c == '/':
        b = st.pop()
        a = st.pop()
        st.push(a / b)
    else:
        pass
print('answer: {}'.format(st.answer()))

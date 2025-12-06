from stack import Stack


def is_balanced(input_str):
    s = Stack()
    for c in input_str:
        if c == '(':
            s.push(c)
        else:
            if s.size() != 0:
                s.pop()
            else:
                return False

    return s.size() == 0
            
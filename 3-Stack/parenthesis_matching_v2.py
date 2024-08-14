def areBracketBalanced(exp):
    stack = []
    
    for char in exp:
        if char in ["(", "{", "["]:
            # Push the element in the stack           
            stack.append(char)
        else:
            # So stack cannot be empty at this point
            if not stack:
               return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True
                         
    
if __name__ == "__main__":
    exp = input('Enter Input : ')
    
    # Function call
    if areBracketBalanced(exp):
        print('Parentheses : Matched ! ! !')
    else:
        print('Parentheses : Unmatched ! ! !')
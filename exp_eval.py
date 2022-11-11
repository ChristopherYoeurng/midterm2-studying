from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    if input_str == '':
        raise PostfixFormatException("Empty input")
    charList = input_str.split()
    stack = Stack(30)
    for char in charList:
        try:
            stack.push(int(char)) #only ints can be converted to int
        except ValueError: 
            try:
                stack.push(float(char)) #if unable to convert to int, try float
            except ValueError:
                try: #if not a number, try operators 
                    #matches each operator character to its respective operation 
                    if char == '+': 
                        stack.push(stack.pop() + stack.pop())
                    elif char == '-':
                        first = stack.pop()
                        second = stack.pop()
                        stack.push(second - first)
                    elif char == '*':
                        stack.push(stack.pop() * stack.pop())
                    elif char == '/':
                        try: 
                            divisor = stack.pop()
                            dividend = stack.pop()
                            stack.push(dividend / divisor)
                        except ZeroDivisionError:
                            raise ValueError
                    elif char == '**':
                        #top of stack is the exponent and not the base, need to pop first and flip them around
                        exponent = stack.pop()
                        base = stack.pop()
                        stack.push(base ** exponent)
                    elif char == '>>': 
                        try: #changes the error type for invalid bitshift operations
                            first = stack.pop()
                            second = stack.pop ()
                            stack.push( second>>first)
                        except TypeError:
                            raise PostfixFormatException("Illegal bit shift operand")
                    elif char == '<<':
                        try:
                            first = stack.pop()
                            second = stack.pop ()
                            stack.push( second<<first)
                        except TypeError: 
                            raise PostfixFormatException("Illegal bit shift operand")
                    else: #if string is not in operators then it is invalid 
                        raise PostfixFormatException("Invalid token")
                except IndexError: #if stack.pop() produces an indexError, there are too many operators and not enough operands
                    raise PostfixFormatException("Insufficient operands")
    if stack.size() >1: #if there are still mulitple items in the stack after all operations are complete, there are too many operands
        raise PostfixFormatException("Too many operands")
    return stack.pop() #returns the last value in the stack

def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    charList = input_str.split()
    stack = Stack(30)
    pf = []
    operators = ['-','+','/','*','**','>>','<<']

    #iterating over each token in the split list of tokens 
    for token in charList:
        try:
            float(token) #check if it is a number 
            pf.append(token)
        except ValueError:
            if token == '(':
                stack.push(token)
            elif token == ')':
                while stack.peek() != '(':
                    pf.append(stack.pop())
                stack.pop() #pop the open parenthesis but don't assign

            #when token is an operator   
            elif token in operators:

                #edge case where there is no stack to pop from. no precedence calcualtions are needed 
                if stack.size()==0:
                    stack.push(token)

                # pops certain operators based on the precedence of the token and the top of the stack 
                elif operators.index(token)>=0 and operators.index(token)<= 1:
                    while stack.size()>0 and stack.peek() != '(': #keeps popping and appending until stack is empty or open parenthesis is found 
                        pf.append(stack.pop())
                    stack.push(token)
                elif operators.index(token) >=2 and operators.index(token)<= 3:
                    while stack.size()>0 and stack.peek() != '(' and operators.index(stack.peek())>=2:
                        pf.append(stack.pop())
                    stack.push(token)
                elif token == "**":
                    while stack.size()>0 and stack.peek() != '(' and operators.index(stack.peek())>4: # the stack.peek condition is non-inclusive of ** here because of its right associativity  
                        pf.append(stack.pop())
                    stack.push(token)
                elif operators.index(token)>=5:
                    while stack.size()>0 and stack.peek() != '(' and operators.index(stack.peek())>=5:
                        pf.append(stack.pop())
                    stack.push(token)

    #appends all remaining operators in the stack 
    while not stack.is_empty():
        pf.append(stack.pop())
    
    #returns a string form of the postfix list we created earlier, with a single space as the separator
    return ' '.join(pf)

    


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    pre = input_str.split()
    stack = Stack(30)
    operators = ['-','+','/','*','**','>>','<<']
    for token in pre[::-1]: #iterating backwards from the last entry to the first one
        try:
            float(token)
            stack.push(token)
        except ValueError:
            if token in operators: 
                op1 = stack.pop()
                op2 = stack.pop()
                stack.push(op1 + ' ' + op2 + ' ' + token)
    return stack.pop() #returns the last item in the stack, which should be the correct postfix equation



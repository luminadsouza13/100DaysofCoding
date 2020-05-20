#
# Given strings of brackets, determine whether each sequence of brackets is balanced.
# If a string is balanced, print YES on a new line; otherwise, print NO on a new line.
#

# Algorithm used for this is stacks
# scan from left to right
# if character is ( or { or [ then put in stack
# if character is ) or } or ] then pull from stack fifo and compare if its same
openList = ['(', '{', '[']
closeList = [')', '}', ']']


def checkBalanced(inputStr):
    stack = []
    for ch in inputStr:
        if ch in openList:
            stack.append(ch)
        elif ch in closeList:
            if len(stack) > 0:
                stackch = stack[len(stack)-1]
                if ch == ')' and stackch == '(':
                    stack.pop()
                elif ch == ']' and stackch == '[':
                    stack.pop()
                elif ch == '}' and stackch == '{':
                    stack.pop()
                else:
                    return "Here 2 : Unbalanced"
            else:
                return "Here 3 : Unbalanced"
    if len(stack) > 0:
        return "Unbalanced"
    else:
        return "Balanced"
            # pop from stack top value that was pushed
            # compare with character if belongs to same bracket family continue if not


inputStr = input("Enter strings of brackets")

length = len(inputStr)

if length == 0:
    print("Please enter some input")
elif (length % 2) != 0:
    print("Here 1 : Unbalanced")
else:
    print(checkBalanced(inputStr))

# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.
#
# Examples
# The following are examples of balanced delimiter strings:
#
# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:
#
# Input:
# ([{}])
# Output:
# True

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0:
        return "True"
    else:
        return "False"
string = input("Enter the characters")
print(string, "-", check(string))

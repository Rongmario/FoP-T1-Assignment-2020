"""Lovelace04_PartA.py"""
"""Licensed Under the MIT License: CHECK IN REPO: https://github.com/Rongmario/FoP-T1-Assignment-2020"""

__author__ = "Rongmario"

def main(expression: str):  # Expects user's input in the function (string)
    if len(expression) == 0:
        return "Empty string."  # Output when user's input is empty
    splits = [expression[0]]  # We populate splits list with the first character of the expression
    for i in expression[1:]:  # Start the loop from second character
        if i.isdigit():
            splits[-1] += i  # If current character is a digit, add it onto the last element of list
        else:
            splits.append(i)  # If current character is + or -, we append a new element onto the list
    # Sum of all elements in the list, we use list comprehension here to convert all elements with type 'str' to 'int'
    return sum([int(x) for x in splits])


user_input = input("Please enter an arithmetic expression: ")
result = main(user_input)
if type(result) == int:
    # Format is used here so I can put a full-stop straight after the variable without having a space dividing it
    print("The result is {0}.\nGoodbye.".format(result))
else:
    print(result)

"""Lovelace04_PartC.py"""
"""Licensed Under the MIT License: CHECK IN REPO: https://github.com/Rongmario/FoP-T1-Assignment-2020"""

__author__ = "Rongmario"

def main(expression: str):  # Expects user's input in the function (string)
    if len(expression) == 0:
        return "Empty string."  # Output when user's input is empty
    first = expression[0]
    splits, signs = [first], {'+', '-', '*'}  # Use tuple unpacking to assign variables
    if not first.isdigit() or not expression[-1].isdigit():
        return "Invalid expression."  # Output when first character is anything other than a number
    for i in expression[1:]:  # Start the loop from second character
        if i.isdigit():
            if splits[-1] == '*':
                splits.append(i)  # When last index of list is *, we append new element
            else:
                splits[-1] += i  # If current character is a digit, add it onto the last element of list
        elif i in signs:
            if splits[-1] in signs:
                return "Invalid expression."  # Not allowed signs to be next to each other
            else:
                splits.append(i)  # If current character is any of the signs, we append a new element onto the list
        else:
            return "Invalid expression."
    j = 0  # Counter
    while j < len(splits):
        if splits[j] == '*':
            splits[j - 1] = int(splits[j - 1]) * int(splits[j + 1])  # Multiply left, right hand of the multiply index
            del splits[j: j + 2]  # Delete multiply index and right hand index, result is stored on left hand
        else:
            j += 1  # Otherwise increment counter if no multiply sign is found
    # Sum of all elements in the list, we use list comprehension here to convert all elements with type 'str' to 'int'
    return sum([int(x) for x in splits])


user_input = input("Please enter an arithmetic expression: ")
result = main(user_input)
if type(result) == int:
    # Format is used here so I can put a full-stop straight after the variable without having a space dividing it
    print("The result is {0}.\nGoodbye.".format(result))
else:
    print(result)

"""Lovelace04_PartB.py"""
"""Licensed Under the MIT License: CHECK IN REPO: https://github.com/Rongmario/FoP-T1-Assignment-2020"""

__author__ = "Rongmario"

def main(expression: str):  # Expects user's input in the function (string)
    if len(expression) == 0:
        return "Empty string."  # Output when user's input is empty
    first, signs = expression[0], {'+', '-'}  # Using tuple unpacking to assign variables
    if not expression[-1].isdigit() or not first.isdigit() and first not in signs:
        # Output when final char is not a number or when first char is an illegal character
        return "Invalid expression."
    splits = [first]  # Store first character as starting element in list
    for i in expression[1:]:
        # Make new element with current index if it is a sign and if last element's last character is a number
        if splits[-1][-1].isdigit() and i in signs:
            splits.append(i)
        elif i.isdigit() or i in signs:
            splits[-1] += i  # If current is an accepted character, append onto last element
        else:
            return "Invalid expression."  # Output when an illegal character is found
    ''' Sum of everything in the list, we use list comprehension here to convert all elements with type 'str' to 'int'.
        We replace bundles of operators here to what it would be evaluated as.
        We also make + blank because Python's int() doesn't allow multiple + signs to be casted '''
    return sum([int(x.replace('+', '').replace('--', '')) for x in splits])


user_input = input("Please enter an arithmetic expression: ")
result = main(user_input)
if type(result) == int:
    # Format is used here so I can put a full+-stop straight after the variable without having a space dividing it
    print("The result is {0}.\nGoodbye.".format(result))
else:
    print(result)

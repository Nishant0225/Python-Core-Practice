# ==========================================
# DOCSTRING IN PYTHON
# ==========================================

# A Docstring is a multi-line string used
# to describe the purpose, input, output,
# and other details of a function, class,
# or module.

# It is written inside triple quotes (""" """)

def is_even(num):
    """
    This function checks whether a given
    number is even or odd.

    Input:
        num -> Any integer

    Output:
        Even / Odd

    Created On:
        16 Nov 2022
    """

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(10))

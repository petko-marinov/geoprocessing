# field calculator python function
# code block - pre-logic script block
unique_list = []


def is_duplicate(in_value):

    if in_value in unique_list:
        return 1
    else:
        unique_list.append(in_value)
        return 0


# expression text box, variable must in surrounded with !
is_duplicate(!variable_name!)

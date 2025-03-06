def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name.

    Args:
        f_name (string): First name
        l_name (string): Last name

    Returns:
        string: Formatted name
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
a = """Multi
line
String""" #if not assigned to a variable, it will be a multi-line comment but this way of commenting is not preferred

print(a)
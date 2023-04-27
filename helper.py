from termcolor import cprint


def print_color(text, type):
    width = 60

    if type == "first":
        cprint(text.center(width), "black", "on_cyan", attrs=["bold"])
    elif type == "second":
        cprint(text.center(width), "cyan", attrs=["bold", "underline"])
    elif type == "third":
        cprint(text.center(width), "white")
    elif type == "third underline":
        cprint(text.center(width), "white", attrs=["underline"])
    elif type == "success":
        cprint(text.center(width), "green")
    elif type == "error":
        cprint(text.center(width), "red")
    elif type == "info":
        cprint(text.center(width), "light_grey")


def validate_input(input, max):
    # Check if choice is a number
    try:
        input = int(input)
    except ValueError:
        print_color("Please enter a number", "error")
        return False

    # Check if choice is in range
    if input not in range(1, max):
        print_color("Invalid choice", "error")
        return False

    return True


def get_input(message):
    try:
        return int(input(message + ": "))
    except TypeError:
        "Input must be type: int"

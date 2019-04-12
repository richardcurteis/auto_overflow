
def get_input(message):
    try:
        return input(message + ": ")
    except TypeError:
        "Input must be type: string"

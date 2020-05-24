from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ANIMAL = {
    "Dog": {
        "fname": "Jonney",
        "lname": "Dog",
        "timestamp": get_timestamp()
    },
    "Cat": {
        "fname": "Sweety",
        "lname": "Cat",
        "timestamp": get_timestamp()
    },
    "Horse": {
        "fname": "Superman",
        "lname": "Horse",
        "timestamp": get_timestamp()
    }
}

def get():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    return [ANIMAL[key] for key in sorted(ANIMAL.keys())]
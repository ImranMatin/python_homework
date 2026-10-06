def hello():
    return "Hello!"


def greet(name):
    return f"Hello, {name}!"


def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        if operation == "subtract":
            return a - b
        if operation == "multiply":
            return a * b
        if operation == "divide":
            if b == 0:
                return "You can't divide by 0!"
            return a / b
        if operation == "modulo":
            return a % b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

    return "You can't multiply those values!"


def data_type_conversion(value, type_name):
    try:
        if type_name == "float":
            return float(value)
        if type_name == "str":
            return str(value)
        if type_name == "int":
            return int(value)
    except (TypeError, ValueError):
        return f"You can't convert {value} into a {type_name}."

    return f"You can't convert {value} into a {type_name}."


def grade(*args):
    try:
        average = sum(args) / len(args)
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def repeat(string, count):
    return string * count


def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    if mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    return None


def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    result = []

    for index, word in enumerate(words):
        if index == 0 or index == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)


def hangman(secret, guess):
    result = []
    for letter in secret:
        if letter in guess:
            result.append(letter)
        else:
            result.append("_")
    return "".join(result)


def pig_latin(text):
    vowels = "aeiou"
    translated = []

    for word in text.split():
        if word[0] in vowels:
            translated.append(word + "ay")
            continue

        index = 0
        while index < len(word) and word[index] not in vowels:
            if word[index] == "q" and index + 1 < len(word) and word[index + 1] == "u":
                index += 2
            else:
                index += 1

        translated.append(word[index:] + word[:index] + "ay")

    return " ".join(translated)

jokes = []


def print_only_new(joke: str):
    if joke not in jokes:
        print(joke)
        jokes.append(joke)

words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False


def load(dict):
    file = open("dictionary.pdf", "r")
    for line in file:
        words.add(line)
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True
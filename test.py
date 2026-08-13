


def hasduplicates(words):

    seen = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)
    return False


        
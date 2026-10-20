"""Use a stack to remember unresolved items in last-in, first-out order."""


def valid_parentheses(text):
    """Whether text is a balanced sequence of (), [], and {}.

    Empty text is valid; any other character makes the input invalid.
    O(n) time and O(n) space in the worst case.
    """
    openings = set('([{')
    matching = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in text:
        if char in openings:
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
        else:
            return False
    return not stack


def daily_temperatures(temperatures):
    """Days until a strictly warmer value; zero if none follows.

    O(n) time and O(n) workspace plus the O(n) result. Input is unchanged.
    Equal temperatures do not resolve a pending day.
    """
    waits = [0] * len(temperatures)
    pending = []  # Unresolved indices, in nonincreasing temperature order.
    for day, temperature in enumerate(temperatures):
        while pending and temperature > temperatures[pending[-1]]:
            previous = pending.pop()
            waits[previous] = day - previous
        pending.append(day)
    return waits

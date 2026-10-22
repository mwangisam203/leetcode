def encode(strs):

    parts = []

    for word in strs:
        parts.append(str(len(word)))
        parts.append("#")
        parts.append(word)

    return "".join(parts)


def decode(encoded):
    res = []
    i = 0

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

        length = int(encoded[i:j])
        start  = j + 1
        end = start + length

        i = end

        res.append(encoded[start:end])

    return res


if __name__ == "__main__":
    # Each case contains the original strings and their expected encoding.
    cases = [
        ([], ""),
        ([""], "0#"),
        (["", ""], "0#0#"),
        (["fab", "", "amize"], "3#fab0#5#amize"),
        (["#", "a#b"], "1##3#a#b"),
        (["abcdefghijkl", "end"], "12#abcdefghijkl3#end"),
        (["猫", "🙂"], "1#猫1#🙂"),
        (["a\nb", " "], "3#a\nb1# "),
    ]

    for number, (words, expected) in enumerate(cases, start=1):
        encoded = encode(words)
        decoded = decode(encoded)

        assert encoded == expected, f"Case {number}: unexpected encoding {encoded!r}"
        assert decoded == words, f"Case {number}: unexpected decoding {decoded!r}"

        print(f"PASS {number}: {words!r} -> {encoded!r} -> {decoded!r}")

    print(f"All {len(cases)} test cases passed.")

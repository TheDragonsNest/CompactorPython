def compress(txt):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_word = ""

    for c in txt:
        current_word += c
        if current_word not in dictionary:
            dictionary[current_word] = next_code
            next_code += 1
            result.append((dictionary[current_word[:-1]]))
            current_word = c

    result.append(dictionary[current_word])

    return result


def decompress(txt):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = []
    current_word = ""

    for code in txt:
        if code in dictionary:
            word = dictionary[code]
        elif code == next_code:
            word = current_word + current_word[0]
        else:
            raise ValueError("Code out of Bounds. Invalid input")

        result.extend(word)
        dictionary[next_code] = current_word + word[0]
        next_code += 1

        current_word = word

    return ''.join(result)

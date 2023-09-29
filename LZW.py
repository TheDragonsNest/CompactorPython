def compress(message):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []

    current_word = ""
    for c in message:
        current_word += c
        if current_word not in dictionary:
            dictionary[current_word] = next_code
            next_code += 1
            result.append((dictionary[current_word[:-1]]))
            current_word = c

    result.append(dictionary[current_word])

    return result

def generateCodes(dict):
    if dict.isinstance(str):
        print(str)
        # generate dictionary from letter freqs
    queue = PriorityQueue()
    for entry in dict:
        queue.put(entry)

    

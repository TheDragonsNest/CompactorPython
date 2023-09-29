import LZW

if __name__ == "__main__":
    txt = input("Text to compress: ")
    compressed_text = LZW.compress(txt)
    ascii_text = [ord(char) for char in txt]

    print("ASCII: ", ascii_text)
    print("LZW:   ", compressed_text)
    print(f"LZW is {((len(compressed_text) / len(ascii_text)) * 100):.1f}% of ASCII")

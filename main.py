import re
import argparse as ap

import Huffman
import LZW

if __name__ == "__main__":
    parser = ap.ArgumentParser()
    compression_group = parser.add_mutually_exclusive_group()
    compression_group.add_argument("-h", "--huff", "--huffman", action="store_true", help="Use Huffman")
    compression_group.add_argument("-l", "--lzw", action="store_true", help="Use LZW")
    direction_group = parser.add_mutually_exclusive_group()
    direction_group.add_argument("-d", "--decompress", action="store_true")
    direction_group.add_argument("-c", "--compress", action="store_true")
    parser.add_argument()

    choice = input("compress or decompress??")
    if choice == "compress":
        txt = input("Text to compress: ")
        compressed_text = LZW.compress(txt)
        ascii_text = [ord(char) for char in txt]

        print("ASCII: ", ascii_text)
        print("LZW:   ", compressed_text)
        print(f"LZW is {((len(compressed_text) / len(ascii_text)) * 100):.1f}% of ASCII")
    elif choice == "decompress":
        txt = input("Compressed Text: ")
        txt = re.sub('[,.-]', " ", txt)
        print("Decompressed Text: ", LZW.decompress([int(code) for code in re.split(' +', txt)]))


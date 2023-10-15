import re
import argparse as ap
import yaml

import Huffman
import LZW

if __name__ == "__main__":
    parser = ap.ArgumentParser()
    compression_group = parser.add_mutually_exclusive_group()
    compression_group.add_argument("-H", "--huffman", action="store_true", help="Use Huffman")
    compression_group.add_argument("-L", "--lzw", action="store_true", help="Use LZW")
    direction_group = parser.add_mutually_exclusive_group()
    direction_group.add_argument("-D", "--decompress", action="store_true")
    direction_group.add_argument("-C", "--compress", action="store_true")

    parser.add_argument("input_path", type=str, help="Filepath to input file in YAML format")

    args = parser.parse_args()

    if args.huffman and args.decompress:
        print("NYI")
    elif args.huffman and args.compress:
        # huffman decompression
        with open(args.input_path, 'r') as file:
            char_freq_dict = yaml.safe_load(file)
            print(char_freq_dict)

        huffman_tree = Huffman.build_tree(char_freq_dict)

        codes = {}
        Huffman.generate_codes(huffman_tree, "", codes)

        for char, code in codes.items():
            print(f"Character: {char}, Huffman Code: {code}")
        # TODO: write output list to YAML file

    elif args.lzw and args.decompress:
        with open(args.input_path, 'r') as file:
            codes = yaml.safe_load(file)

        print("Decompressed Text: ", LZW.decompress(codes))
        # TODO: write output list to YAML file

    elif args.lzw and args.compress:
        with open(args.input_path, 'r') as file:
            text = yaml.safe_load(file)[0]

        ascii_text = [ord(char) for char in text]
        compressed_text = LZW.compress(text)

        print("ASCII: ", ascii_text)
        print("LZW:   ", compressed_text)
        print(f"LZW is {((len(compressed_text) / len(ascii_text)) * 100):.1f}% of ASCII")
        # TODO: write output list to YAML file

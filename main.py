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
    direction_group.add_argument("-D", "--decompress", action="store_true", help="decompress input")
    direction_group.add_argument("-C", "--compress", action="store_true", help="compress input")

    parser.add_argument("input_path", type=str, help="Filepath to input file in YAML format")

    args = parser.parse_args()

    if args.huffman and args.decompress:
        with open(args.input_path, 'r') as file:
            file_contents = yaml.safe_load(file)

        code_table = file_contents[1]
        code_table = {a: b for b, a in code_table.items()}

        text = file_contents[0]

        decompressed_text = Huffman.decompress(code_table, text)

        print(decompressed_text)

    elif args.huffman and args.compress:
        with open(args.input_path, 'r') as file:
            text = yaml.safe_load(file)[0]

        compression_result = Huffman.compress(text)
        ascii_text = [ord(char) for char in text]
        print(f"Huffman is {((len(compression_result[0]) / len(ascii_text)) * 100):.1f}% of ASCII")

        print(compression_result[0])

        with open("output.yml", 'w') as file:
            yaml.safe_dump(compression_result, file)

    elif args.lzw and args.decompress:
        with open(args.input_path, 'r') as file:
            codes = yaml.safe_load(file)

        output = LZW.decompress(codes)
        print("Decompressed Text: ", output)
        with open("output.yml", 'w') as file:
            yaml.safe_dump(output, file)

    elif args.lzw and args.compress:
        with open(args.input_path, 'r') as file:
            text = yaml.safe_load(file)[0]

        ascii_text = [ord(char) for char in text]
        compressed_text = LZW.compress(text)

        print("ASCII: ", ascii_text)
        print("LZW:   ", compressed_text)
        print(f"LZW is {((len(compressed_text) / len(ascii_text)) * 100):.1f}% of ASCII")
        with open("output.yml", 'w') as file:
            yaml.safe_dump(compressed_text, file)

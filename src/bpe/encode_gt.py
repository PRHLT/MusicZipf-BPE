#!/usr/bin/env python
"""Encodes a GT file following a BPE vocabulary.

Takes the GT file and the BPE vocabulary and encodes the GT file following the
BPE words. Will store the resulting GT.
"""


import argparse
from bpe import tokenize


parser = argparse.ArgumentParser(
    description="Encodes a GT file following a BPE vocabulary."
)
parser.add_argument(
    "-gt",
    "--ground_truth",
    type=str,
    required=True,
    help="the GT file to be \
        encoded",
)
parser.add_argument(
    "-v",
    "--vocab",
    type=str,
    required=False,
    help="the vocabulary file to use in the encoding.",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    required=False,
    default="./encoded_gt.txt",
    help="path where to save the output encoded GT file (default: \
        ./encoded_gt.txt)",
)
parser.add_argument(
    "-s",
    "--separator",
    type=str,
    required=False,
    default="&",
    help="separator to use between tokens (default: &)",
)
args = parser.parse_args()


if __name__ == "__main__":
    file = args.ground_truth
    vocab = args.vocab
    separator = args.separator
    output = args.output

    # Read vocab from file
    print("Reading vocabulary...")
    with open(vocab, "r") as f:
        v = f.read().splitlines()
        v = {line.split()[1]: int(line.split()[2]) for line in v}

        max_tknlen = max([len(token) for token in v.keys()])

    # Encode the file
    print("Encoding file...")
    with open(file, "r") as f:
        file = f.read().splitlines()
        file_lines = [line.split(" ")[0] for line in file]  # get ids of lines
        file = [line.split(" ")[1:] for line in file]
        file = [" ".join(line) for line in file]

    # apply BPE tokenization
    print("Applying BPE tokenization...")
    for i, line in enumerate(file):
        with open(output, "a") as f:
            f.write(f"{file_lines[i]} ")
            f.write(tokenize(line.split(), v, max_tknlen, separator) + "\n")
    print(f"Encoded GT file saved to {output}")

#!/usr/bin/env python
"""Trains a BPE model for a given GT data.

Takes a GT file and the BPE parameters (min_occ, max_tknlen) and trains a BPE.
Will store the vocabulary, the pairs and the resulting transcriptions.
"""


import argparse
from bpe import bpe
import time


parser = argparse.ArgumentParser(
    description="Trains a BPE model for a given " "GT data."
)
parser.add_argument(
    "-gt",
    "--ground_truth",
    type=str,
    required=True,
    help="the GT file to train the BPE model",
)
parser.add_argument(
    "-mo",
    "--min_occ",
    type=int,
    required=True,
    help="minimum number of occurrences to consider \
                        a token (default: 2)",
)
parser.add_argument(
    "-mxl", "--max_len", type=int, required=True, help="maximum length of tokens"
)
parser.add_argument(
    "-v",
    "--vocab_path",
    type=str,
    required=False,
    default="./vocab.txt",
    help="path where to save the output \
                        vocabulary file (default: ./vocab.txt)",
)
parser.add_argument(
    "-t",
    "--text_path",
    type=str,
    required=False,
    default="./text.txt",
    help="path where to save the output \
                        text file (default: ./text.txt)",
)
parser.add_argument(
    "-s",
    "--separator",
    type=str,
    required=False,
    default="&",
    help="separator to use between tokens \
                        (default: &)",
)
args = parser.parse_args()

if __name__ == "__main__":
    gt_file = args.ground_truth
    separator = args.separator
    min_occ = args.min_occ
    max_tknlen = args.max_len
    vocab_file = args.vocab_path
    text_file = args.text_path

    protected_tkns = ["c1", "c2", "c3", "c4", "c5", "f1", "f2", "f3", "f4", "f5", "#"]

    # GT file
    with open(gt_file, "r") as t:
        gt = t.read().splitlines()
        gt_lines = [line.split(" ")[0] for line in gt]
        gt = [line.split(" ")[1:] for line in gt]

    # Apply BPE to get the vocabulary
    print("Applying BPE...")
    start_time = time.time()  # timer
    vocab, pairs, total_merges, result_text = bpe(
        gt, protected_tkns, min_occ, max_tknlen, separator
    )
    print(f"Total merges: {total_merges}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")  # timer

    # Save vocabulary to a file
    with open(vocab_file, "w") as f:
        for token, freq in vocab.items():
            f.write(f"{token} {freq}\n")

    # Print resulting text
    with open(text_file, "w") as f:
        for i, line in enumerate(result_text):
            f.write(f"{gt_lines[i]} ")
            f.write(" ".join(line) + "\n")

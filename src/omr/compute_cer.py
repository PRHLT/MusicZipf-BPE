#!/usr/bin/env python
"""Calculates de CER and WER between two files.

Both files must contain the <space> symbol to separate words (even when single).
"""


import argparse
import editdistance
from math import sqrt


parser = argparse.ArgumentParser(
    description="Calculates de CER and WER between two files. \
                Both files must contain the <space> symbol to separate words \
                (even when single)."
)
parser.add_argument(
    "-ref", "--ref_file", type=str, required=True, help="the GT file to compare with"
)
parser.add_argument(
    "-hyp", "--hyp_file", type=str, required=True, help="the hypothesis file"
)
args = parser.parse_args()


def preprocess_files(ref_file, hyp_file):
    ref = dict()
    with open(ref_file, "r") as r:
        for l in r:
            l = l.strip().split(" ", 1)
            if len(l) > 1:
                ll = l[1].split()
                if ll[-1] == "<space>":
                    ll = ll[:-1]
                if ll[0] == "<space>":
                    ll = ll[1:]
                ref[l[0]] = ll
            else:
                ref[l[0]] = []

    hyp = dict()
    with open(hyp_file, "r") as h:
        for l in h:
            l = l.strip().split(" ", 1)
            if len(l) > 1:
                ll = l[1].split()
                if ll[-1] == "<space>":
                    ll = ll[:-1]
                if len(ll) > 0 and ll[0] == "<space>":
                    ll = ll[1:]
                hyp[l[0]] = ll
            else:
                hyp[l[0]] = []

    return ref, hyp


if __name__ == "__main__":

    ref, hyp = preprocess_files(args.ref_file, args.hyp_file)

    # CER is calculated without the <space> symbol
    rc = [ref[k] for k in ref.keys()]
    rc = [" ".join(x).split() for x in rc]
    rc = [[x if "<space>" not in x and "-" not in x else "" for x in v] for v in rc]
    rc = [[x for x in v if x] for v in rc]

    hc = [hyp[k] if k in hyp else "" for k in ref.keys()]
    hc = [" ".join(x).split() for x in hc]
    hc = [[x if "<space>" not in x and "-" not in x else "" for x in v] for v in hc]
    hc = [[x for x in v if x] for v in hc]

    numedit = sum([editdistance.eval(x, y) for x, y in zip(rc, hc)])
    numWords = sum([len(k) for k in rc])
    conf = 1.96 * sqrt(((numedit / numWords) * (1 - numedit / numWords)) / numWords)
    print(
        "CER(%%) w/o <space> = %6.2f [ %d / %d ] +- %6.2f"
        % (numedit / numWords * 100, numedit, numWords, conf * 100)
    )

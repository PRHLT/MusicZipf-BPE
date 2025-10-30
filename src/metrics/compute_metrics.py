"""
Compute some metrics between empirical and estimated curves.

"""

import numpy as np
import argparse
import re


parser = argparse.ArgumentParser(
    description="Compute R2 score between empirical and estimated curves."
)
parser.add_argument(
    "-em",
    "--empirical",
    type=str,
    required=True,
    help="Path to empirical data (vocabulary)",
)
parser.add_argument(
    "-es",
    "--estimated",
    type=str,
    required=True,
    help="Path to estimated parameters (.fit file)",
)
args = parser.parse_args()


def ZMS(c, z, q, r):
    return (c**z) / ((q + r) ** z)


def compute_ks(c, z, q, emp):
    diffs = []
    M = sum(ZMS(c, z, q, j + 1) for j in range(len(emp)))
    M_ = sum(emp[j] for j in range(len(emp)))
    for i in range(len(emp)):
        A = (1 / M) * sum(ZMS(c, z, q, j + 1) for j in range(i + 1))
        B = (1 / M_) * sum(emp[j] for j in range(i + 1))
        diffs.append(abs(A - B))

    return max(diffs)


def compute_r2(c, z, q, emp):
    A = []
    B = []
    for i in range(len(emp)):
        A.append((ZMS(c, z, q, i + 1) - emp[i]) ** 2)
        B.append((np.mean(emp) - emp[i]) ** 2)

    return 1 - sum(A) / sum(B)


if __name__ == "__main__":
    # read empirical data
    with open(args.empirical, "r") as f:
        lines = f.readlines()
        emp = [float(l.split()[2]) for l in lines]

    # read estimated parameters
    with open(args.estimated, "r") as f:
        log = f.read()
        pat = r"^\s*(\w+)\s*=\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)"
        mat = re.findall(pat, log, re.MULTILINE)

        for name, value in mat:
            if name == "a":
                c = float(value)
            elif name == "b":
                q = float(value)
            elif name == "c":
                z = float(value)

    print("For file:", args.empirical.split("/")[-1])
    print("c =", c, "q =", q, "z =", z)
    print("R2 =", compute_r2(c, z, q, emp))
    print("KS =", compute_ks(c, z, q, emp))
    print()

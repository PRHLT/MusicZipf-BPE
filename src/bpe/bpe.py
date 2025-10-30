from collections import defaultdict, Counter
import heapq
import time


def get_vocab(text):
    """
    Build vocabulary from a text.
    """
    vocab = Counter(tok for line in text for tok in line)
    return vocab


def get_pair_frequencies(text):
    """
    Get frequencies of each pair of consecutive symbols.
    """
    pairs = defaultdict(int)
    for line in text:
        symbols = line.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += 1
    return pairs


def merge_pair(text, pair, separator=""):
    """
    Merge the most frequent pair into a single token in all text.
    """
    new_text = []
    bigram = " " + " ".join(pair) + " "
    replacement = " " + separator.join(pair) + " "
    for line in text:
        new_text.append(line.replace(bigram, replacement))
    return new_text


def get_initial_pairs(text, protected):
    """
    Get initial pair frequencies from the text (as list of lists of tokens).
    Returns both the pair frequency dict and the heap.
    """
    pairs = defaultdict(int)
    for line in text:
        for i in range(len(line) - 1):
            pair = (line[i], line[i + 1])
            # skip protected tokens
            if any(tok in protected for tok in pair):
                continue
            pairs[pair] += 1

    # build heap
    heap = [(-freq, pair) for pair, freq in pairs.items()]
    heapq.heapify(heap)
    return pairs, heap


def update_pair(pair, delta, pairs, heap, protected):
    """
    Update pair frequency and push it to heap.
    """
    if any(tok in protected for tok in pair):
        return
    pairs[pair] += delta
    if pairs[pair] <= 0:
        pairs.pop(pair, None)
        return
    heapq.heappush(heap, (-pairs[pair], pair))


def bpe(text, protected_tokens=[], min_occ=1, max_tknlen=5, separator=""):
    """
    Apply BPE to the given text until convergence.
    - pct_bpe is the percentage of BPE merges to apply
    - protected_tokens are tokens that should not be merged
    - separator is used to separate merged tokens
    - max_tklen is the maximum token length admitted
    - min_occ is the minimum number of occurrences to merge a pair
    """

    all_pairs = []
    protected = set(protected_tokens)
    total_merges = 0
    vocab = get_vocab(text)

    # Build initial pairs & heap
    pairs, heap = get_initial_pairs(text, protected)

    keep = True
    while keep:
        # get best pair from heap
        while heap:
            freq, pair = heapq.heappop(heap)
            # discard stale entries
            if pairs.get(pair, 0) == -freq:
                break
        else:  # heap empty
            break

        best_pair = pair
        best_pair_occ = -freq

        # --- Stopping conditions ---
        if best_pair_occ < min_occ:  # min occurrences not met
            break
        if best_pair_occ == 1:  # all remaining pairs occur only once
            break
        new_tkn = separator.join(best_pair)
        if len(new_tkn.split(separator)) > max_tknlen:  # max tkn length not met
            # mark as unusable and continue
            pairs.pop(best_pair, None)
            continue
        if best_pair in all_pairs:
            # already merged
            pairs.pop(best_pair, None)
            continue

        # --- Merging ---
        A, B = best_pair
        for line in text:
            i = 0
            while i < len(line) - 1:
                if line[i] == A and line[i + 1] == B:
                    update_pair((A, B), -1, pairs, heap, protected)
                    # remove old neighbors
                    if i > 0:
                        update_pair((line[i - 1], A), -1, pairs, heap, protected)
                    if i + 2 < len(line):
                        update_pair((B, line[i + 2]), -1, pairs, heap, protected)

                    # merge
                    line[i] = new_tkn
                    del line[i + 1]

                    # add new neighbors
                    if i > 0:
                        update_pair((line[i - 1], line[i]), +1, pairs, heap, protected)
                    if i + 1 < len(line):
                        update_pair((line[i], line[i + 1]), +1, pairs, heap, protected)

                else:
                    i += 1

        # vocab, pairs and merges
        vocab = get_vocab(text)
        all_pairs.append(best_pair)
        total_merges += 1
        print(
            f"Merge {total_merges}: {best_pair} -> {new_tkn} (occurrences: {best_pair_occ})"
        )

    return vocab, all_pairs, total_merges, text


if __name__ == "__main__":
    ########################
    #   EXAMPLE OF USAGE   #
    ########################
    start_time = time.time()

    # BPE from a transcription file
    with open("test/my_test_staves.txt", "r") as file:
        trans = file.read().splitlines()
        # erase first column of each line (line id)
        trans = [
            line.strip().split(" ")[1:] for line in trans
        ]  # list of lists of tokens
        or_trans = [t for t in [" ".join(line) for line in trans]]

    # Parameters
    prot_tkns = [
        "c1",
        "c2",
        "c3",
        "c4",
        "c5",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "#",
    ]  # protected tokens from being merged
    separator = "&"  # separator for merged tokens
    min_occ = 3  # minimum occurrences to merge a pair
    max_tknlen = 4  # maximum token length

    # Apply BPE
    final_vocab, final_pairs, total_merges, text = bpe(
        trans, prot_tkns, min_occ, max_tknlen, separator
    )

    print("# Original Transcriptions #")
    for transcription in or_trans:
        print(transcription)

    print("\n# Final Vocabulary #")
    print(f"- Total tokens: {len(final_vocab)}")
    for token, freq in final_vocab.items():
        print(f"{token}: {freq}")

    print("\n# Final transcriptions #")
    for line in trans:
        print(line)

    print(f"\n--- Execution: {time.time() - start_time} seconds ---")

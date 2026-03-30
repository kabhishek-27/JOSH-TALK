from collections import defaultdict

def build_lattice(model_outputs):
    lattice = []

    max_len = max(len(x.split()) for x in model_outputs)

    for i in range(max_len):
        bin_words = set()

        for output in model_outputs:
            words = output.split()
            if i < len(words):
                bin_words.add(words[i])

        lattice.append(list(bin_words))

    return lattice


def lattice_wer(reference, lattice):
    ref_words = reference.split()
    score = 0

    for i, word in enumerate(ref_words):
        if i < len(lattice) and word in lattice[i]:
            continue
        else:
            score += 1

    return score / len(ref_words)
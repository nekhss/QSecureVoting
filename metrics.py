import numpy as np


def calculate_qber(alice_key, bob_key):
    if len(alice_key) == 0:
        return 0

    errors = sum(a != b for a, b in zip(alice_key, bob_key))
    return errors / len(alice_key)


def basis_mismatch_rate(alice_bases, bob_bases):
    mismatches = sum(a != b for a, b in zip(alice_bases, bob_bases))
    return mismatches / len(alice_bases)


def key_retention_ratio(sifted_length, original_length):
    if original_length == 0:
        return 0
    return sifted_length / original_length


def block_error_variance(alice_key, bob_key, block_size=10):
    if len(alice_key) < block_size:
        return 0

    errors = [
        sum(a != b for a, b in zip(
            alice_key[i:i+block_size],
            bob_key[i:i+block_size]
        )) / block_size
        for i in range(0, len(alice_key), block_size)
        if len(alice_key[i:i+block_size]) == block_size
    ]

    return np.var(errors) if errors else 0
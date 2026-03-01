import random
from attacker import intercept


def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]


def generate_bases(n):
    return [random.choice(['Z', 'X']) for _ in range(n)]


def measure_bit(sent_bit, sent_basis, measure_basis):
    """
    Simulates quantum measurement.
    """
    if sent_basis == measure_basis:
        return sent_bit
    else:
        return random.randint(0, 1)


def run_bb84(n_bits, eve=False):

    # --- Alice generates bits and bases ---
    alice_bits = generate_bits(n_bits)
    alice_bases = generate_bases(n_bits)

    # --- Eve intercepts (optional) ---
    if eve:
        transmitted_bits = intercept(alice_bits, alice_bases)
    else:
        transmitted_bits = alice_bits.copy()

    # --- Bob chooses bases ---
    bob_bases = generate_bases(n_bits)
    bob_measurements = []

    for bit, a_basis, b_basis in zip(transmitted_bits, alice_bases, bob_bases):
        measured = measure_bit(bit, a_basis, b_basis)
        bob_measurements.append(measured)

    # --- Sifting ---
    sifted_alice = []
    sifted_bob = []

    for a_bit, b_bit, a_basis, b_basis in zip(
        alice_bits, bob_measurements, alice_bases, bob_bases
    ):
        if a_basis == b_basis:
            sifted_alice.append(a_bit)
            sifted_bob.append(b_bit)

    # --- QBER Calculation ---
    if len(sifted_alice) == 0:
        qber = 0
    else:
        errors = sum(a != b for a, b in zip(sifted_alice, sifted_bob))
        qber = errors / len(sifted_alice)

    # --- Basis mismatch rate ---
    mismatch_rate = sum(
        a != b for a, b in zip(alice_bases, bob_bases)
    ) / n_bits

    return sifted_bob, qber, mismatch_rate
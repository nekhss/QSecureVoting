import random

def intercept(bits, bases):
    """
    Eve performs intercept-resend attack.
    """
    eve_bases = [random.choice(['Z', 'X']) for _ in bits]
    eve_measurements = []

    for bit, basis, eve_basis in zip(bits, bases, eve_bases):
        if basis == eve_basis:
            eve_measurements.append(bit)
        else:
            eve_measurements.append(random.randint(0, 1))

    return eve_measurements

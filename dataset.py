import pandas as pd
import random
from qkd.metrics import (
    calculate_qber,
    basis_mismatch_rate,
    key_retention_ratio,
    block_error_variance
)

from qkd.bb84 import run_bb84

def extract_features(sim_result):
    qber = calculate_qber(
        sim_result["alice_key"],
        sim_result["bob_key"]
    )

    mismatch = basis_mismatch_rate(
        sim_result["alice_bases"],
        sim_result["bob_bases"]
    )

    retention = key_retention_ratio(
        sim_result["sifted_length"],
        sim_result["original_length"]
    )

    variance = block_error_variance(
        sim_result["alice_key"],
        sim_result["bob_key"]
    )

    return {
        "qber": qber,
        "basis_mismatch_rate": mismatch,
        "key_retention_ratio": retention,
        "error_variance": variance
    }


def generate_dataset(n_samples=200, n_bits=100):
    data = []

    for _ in range(n_samples):
        eve_present = random.choice([True, False])

        sim = run_bb84(n_bits=n_bits, eve=eve_present)

        features = extract_features(sim)
        features["label"] = 1 if eve_present else 0

        data.append(features)

    df = pd.DataFrame(data)

    return df
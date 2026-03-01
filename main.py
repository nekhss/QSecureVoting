from qkd.bb84 import run_bb84

key, qber, mismatch = run_bb84(1000, eve=False)
print("WITHOUT EVE")
print("Key length:", len(key))
print("QBER:", qber)
print("Mismatch rate:", mismatch)
print()

# Run with Eve
key, qber, mismatch = run_bb84(1000, eve=True)
print("WITH EVE")
print("Key length:", len(key))
print("QBER:", qber)
print("Mismatch rate:", mismatch)

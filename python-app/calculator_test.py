import numpy as np

numbers = np.array([10, 20, 30, 30])

total = np.sum(numbers)

assert total == 100, f"Expected 100 but got {total}"

print("✅ Calculator test passed")

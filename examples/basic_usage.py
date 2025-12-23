# examples/basic_usage.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

"""
Basic usage example for ExplainMath v0.1

This script demonstrates:
- Safe arithmetic
- Explicit invalid results
- Human-readable explanations
"""

from core.value import Value


def main():
    print("=== ExplainMath: Basic Usage ===\n")

    a = Value(10)
    b = Value(0)

    print("a =", a.value)
    print("b =", b.value)

    print("\nAttempting division...")
    c = a.div(b)

    print("Result status:", c.status)
    print("Result value:", c.value)
    print("Explanation:", c.explanation)

    print("\nProgram continues safely after invalid math.")

    d = Value(5)
    e = Value(2)
    f = d.mul(e)

    print("\n5 × 2 =", f.value)


if __name__ == "__main__":
    main()

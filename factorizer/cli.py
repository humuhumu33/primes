import argparse
from typing import List

from axiom1.prime_core import primes_up_to, is_prime


def factorize_number(n: int) -> List[int]:
    """Return the prime factors of ``n`` in ascending order."""
    if n < 2:
        return []

    factors: List[int] = []
    remaining = n
    for p in primes_up_to(int(n ** 0.5) + 1):
        while remaining % p == 0:
            factors.append(p)
            remaining //= p
    if remaining > 1:
        factors.append(remaining)
    return factors


def main() -> None:
    parser = argparse.ArgumentParser(description="Prime factorization utility")
    parser.add_argument("number", type=int, help="Integer to factor")
    args = parser.parse_args()

    factors = factorize_number(args.number)
    if factors:
        print(" * ".join(str(f) for f in factors))
    else:
        print("1")


if __name__ == "__main__":
    main()

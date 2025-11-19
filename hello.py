#!/usr/bin/env python3
"""
hello.py — small demo script for my-port-test
Prints a greeting and a UTC timestamp.
"""
from datetime import datetime

def main():
    print("Hello, world!")
    print("Repository: AlinaBarenboim/my-port-test")
    print("Generated at:", datetime.utcnow().isoformat() + "Z")

if __name__ == "__main__":
    main()
# General Utility Functions for CTF Solving

## Byte Manipulation

def byte_xor(a: bytes, b: bytes) -> bytes:
    """Returns the result of XORing two byte arrays."""
    return bytes(x ^ y for x, y in zip(a, b))


def bytes_to_hex(byte_data: bytes) -> str:
    """Converts bytes to a hex string."""
    return byte_data.hex()

## Pattern Matching

import re

def find_pattern(data: str, pattern: str) -> list:
    """Find all matches of a pattern in a given string."""
    return re.findall(pattern, data)

## Data Analysis

import statistics

def calculate_mean(data: list) -> float:
    """Calculates the mean of a list of numbers."""
    return statistics.mean(data)


def count_occurrences(data: list) -> dict:
    """Counts the occurrences of each item in a list."""
    return {item: data.count(item) for item in set(data)}

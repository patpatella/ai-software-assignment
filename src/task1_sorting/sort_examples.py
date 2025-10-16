# src/task1_sorting/sort_examples.py

from typing import List, Dict

# AI-suggested (Pythonic, uses sorted)
def sort_dicts(lst: List[Dict], key: str) -> List[Dict]:
    """
    Sort list of dictionaries by a specific key using Python sorted().

    Time complexity: O(n log n)
    """
    # handle missing keys safely by using dict.get
    return sorted(lst, key=lambda d: d.get(key, None))


# Manual implementation (bubble-sort style for demonstration)
def sort_dicts_manual(lst: List[Dict], key: str) -> List[Dict]:
    """
    Simple manual sort (O(n^2)). Mutates input list.
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = lst[j].get(key, None)
            b = lst[j+1].get(key, None)
            # handle None gracefully: treat None as greater
            if a is None:
                continue
            if b is None or a > b:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

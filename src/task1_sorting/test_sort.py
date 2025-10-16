# src/task1_sorting/test_sort.py
from sort_examples import sort_dicts, sort_dicts_manual

sample = [
    {"name":"a", "age":30},
    {"name":"b", "age":20},
    {"name":"c", "age":25},
]

def test_sort_dicts():
    out = sort_dicts(sample, "age")
    assert [d["age"] for d in out] == [20,25,30]

def test_sort_dicts_manual():
    # copy to not mutate original in both tests
    in_copy = [dict(x) for x in sample]
    out = sort_dicts_manual(in_copy, "age")
    assert [d["age"] for d in out] == [20,25,30]

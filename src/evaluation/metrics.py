import re
from collections import Counter

def normalize(text):
    return " ".join(re.findall(r"\w+", text.lower()))

def exact_match(prediction, reference):
    return float(normalize(prediction) == normalize(reference))

def token_f1(prediction, reference):
    p, r = normalize(prediction).split(), normalize(reference).split()
    overlap = sum((Counter(p) & Counter(r)).values())
    if not p or not r:
        return float(p == r)
    return 2 * overlap / (len(p) + len(r)) if overlap else 0.0

def recall_at_k(retrieved_ids, gold_ids):
    gold = set(gold_ids)
    return len(set(retrieved_ids) & gold) / len(gold) if gold else 1.0

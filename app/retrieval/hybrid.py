"""Week 2: hybrid search. Keyword search (BM25) and meaning search, fused into one ranking.

The exercise is in weeks/2/README.md. Two functions are yours; the store calls them.

Why both. Meaning search (embeddings) finds "how long does it wait for the source" when the page
says "connection timeout". It is weak exactly where a support desk is strong: product codes, error
numbers and setting names, `E1104`, `KESTREL_CONNECT_TIMEOUT`, which carry little meaning and must
match exactly. Keyword search is the opposite. Each misses what the other finds.

    bm25_scores                 one score per document for the query: rare query terms count
                                for more (IDF), repeats of a term count for less each time (k1),
                                and a long document does not win just by being long (b)
    reciprocal_rank_fusion      merge several rankings by rank, not by score: a dense cosine of
                                0.62 and a BM25 score of 7.3 are not on the same scale, but
                                "first" and "fifth" are

The version filter is applied before either ranking (app/retrieval/store.py), so neither side can
bring a version 2 chunk back for a version 3 question.
"""

import math
import re
from collections import Counter

_TOKEN = re.compile(r"[a-z0-9_]+")


def tokenize(text: str) -> list[str]:
    """Lower-case words, keeping codes whole: `E1104` -> `e1104`, `KESTREL_CONNECT_TIMEOUT` stays
    one token. Given; use it for both the query and the documents."""
    return _TOKEN.findall(text.lower())


def bm25_scores(
    query: str, documents: list[str], *, k1: float = 1.5, b: float = 0.75
) -> list[float]:
    """One BM25 score per document, in the same order. A document sharing no query term scores 0.

    For each query term t, over documents of average length avgdl:
        idf(t)  = ln(1 + (N - n(t) + 0.5) / (n(t) + 0.5))       n(t): documents containing t
        part    = idf(t) * tf * (k1 + 1) / (tf + k1 * (1 - b + b * len(doc) / avgdl))
    and a document's score is the sum of its parts.
    """
    docs = [tokenize(d) for d in documents]
    n_docs = len(docs)
    if n_docs == 0:
        return []
    avgdl = sum(len(d) for d in docs) / n_docs or 1.0
    terms = set(tokenize(query))
    df = {t: sum(1 for d in docs if t in d) for t in terms}
    scores: list[float] = []
    for d in docs:
        tf = Counter(d)
        score = 0.0
        for t in terms:
            f = tf.get(t, 0)
            if not f:
                continue
            idf = math.log(1 + (n_docs - df[t] + 0.5) / (df[t] + 0.5))
            score += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * len(d) / avgdl))
        scores.append(score)
    return scores


def reciprocal_rank_fusion(rankings: list[list[int]], *, k: int = 60) -> list[tuple[int, float]]:
    """Merge rankings of ids (best first) into one: (id, score), best first.

    An id's score is the sum, over every ranking it appears in, of 1 / (k + rank), rank from 1. An
    id missing from a ranking gets nothing from it. Ties keep the order the ids were first seen.
    """
    scores: dict[int, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, 1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    # sorted() is stable and dicts keep insertion order, so ties stay in first-seen order.
    return sorted(scores.items(), key=lambda item: -item[1])

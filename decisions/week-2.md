# Week 2 decision

## Decision

Ship `CHUNK_STRATEGY=section`, `SEARCH_MODE=hybrid`, `SEARCH_K=5` (set in `.env.example`), with
the version filter always on through `search_docs`, and send the model only the right version's
top passages rather than a large context.

Caveats, stated plainly: there was no provider key, so every number here is from the fake model
and the `hash` embedder (`evidence.py --allow-fake`). And `scripts/retrieval_eval.py` crashes on
this variant (v-e736): 38 of its 60 queries name business documents (for example
`contract-harbour-health-juniper-schools-msa.txt`) that exist in `eval/` but not in `corpus/`, so
the retrieval numbers come from a wrapper that skipped those queries (22 kept). They must be
re-run with real embeddings once the variant is fixed.

## Options

- paragraph + dense
- paragraph + hybrid
- heading + dense / heading + hybrid (my chunker)
- section + dense
- section + hybrid (chosen)
- Context: right version only, against right version plus many others ("too much"), or buried in the middle

## Evidence

Retrieval configs (keys contain `+`, which the records parser does not read, so they are listed
here for the reader and checked by hand against evidence/week-2.json, `metrics.retrieval.configs`):
section+hybrid hit_rate 0.91, recall 0.91, MRR 0.69, context tokens 382, version trap (unfiltered) 0.30;
paragraph+hybrid hit_rate 0.91, MRR 0.78, context tokens 818; heading+dense hit_rate 0.64.

- context.settings.right_version.accuracy = 0.90
- context.settings.wrong_version.accuracy = 0.05
- context.settings.too_much.accuracy = 0.90
- context.settings.right_version.tokens_in_per_question = 321
- context.settings.too_much.tokens_in_per_question = 3696
- context.settings.buried.accuracy = 0.80
- context.settings.buried.tokens_in_per_question = 6978
- baseline.answered_from_training = 0.0 (fake model; proves the script only)

## Rejected

paragraph + hybrid: the same hit rate (0.91) and a higher MRR (0.78 against 0.69), but more than
twice the context per question (818 tokens against 382), and its chunks do not say which page and
version they come from. heading + dense, my own chunker, was the weakest (hit rate 0.64): its
small sections lose the page title. "Too much" context was rejected because it costs 3696 tokens
per question for the same 0.90 accuracy as 321; burying the right page costs accuracy (0.80).

## Risk accepted

The hash embedder knows nothing about meaning, so hybrid's advantage here may be mostly BM25; on
real embeddings dense could close the gap. And the retrieval sample is 22 queries, a hit-rate
step is 0.045. I would re-run `make evidence WEEK=2` with `EMBED_PROVIDER=fastembed` and a real
model, and watch hit rate and version accuracy on the hidden evaluation.

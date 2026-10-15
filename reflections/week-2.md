# Reflection — Week 2

Test fellow note: completed by an AI assistant (Claude Code) acting as a fellow.

## Q1. The concept, in my words

The model only knows what you send it. Which passages you choose (the right version, few enough,
near the top) changes the answer more than anything about the model; on the fake run the right
page gave 0.90 accuracy and the wrong version's page 0.05, with the same model.

## Q1b. Reading questions

1. `fixed` cuts the invoice table mid-row. `by_section` repeats the `Title > Section` prefix on
   every chunk and overlaps one paragraph, which costs duplicated tokens in the index and context.
2. The `hash` embedder knows nothing about meaning: it hashes tokens, so only shared words count.
   It exists so tests and the gate run offline and deterministically, with no download.
3. In the vector store's search (through `_wanted` -> `applicable_versions`) for meaning search,
   and in `store.search` on the chunk rows before BM25 for keyword search. Same policy, before
   ranking, so neither side can bring a wrong-version chunk into the fused list.

## Q2. What surprised me

My heading chunker was the weakest configuration on the hash embedder: short sections without
the page title lose the words that identify the page. The given `section` strategy wins by
repeating the title.

## Q3. What I would change

The variant files: `eval/` names business documents that `corpus/` does not contain, and two
week 2 tests still say "Kestrel" while the corpus says "Ironclad". Those are programme bugs, left
failing rather than patched.

## Q4. What I contributed, and how I checked it

The assistant wrote the code; checked with the week 2 tests on both fakes, ruff and mypy, and by
reading the failing tests to confirm they fail on the product name, not on the implementation.

## Q5. Help I used

Claude Code (Claude Opus 5.5); see ai-use/week-2.yml. No reference solution was read.

## Evidence

evidence/week-2.json (fake model, hash embedder; retrieval from a wrapper run, see the decision).

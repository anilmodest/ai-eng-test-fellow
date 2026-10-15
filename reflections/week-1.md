# Reflection — Week 1

Test fellow note: this week was completed by an AI assistant (Claude Code) acting as a fellow, to
exercise the course end to end. Answers are short and honest about that.

## Q1. The concept, in my words

A model is a dependency you do not own and that fails in several distinct ways. Wrap it: a
schema with one repair, retries only for failures that can pass next time, a timeout on every
attempt, a cache so the same work is not paid twice, and tool descriptions precise enough that
the model calls the right thing with valid arguments.

## Q1b. Reading questions

1. `ModelError.retryable`: the only thing a caller should branch on when a call fails.
2. `MODEL_PROVIDER` is read through `Settings` in `get_model_client()` (registry.py). `FallbackClient`
   hands the same request to a second provider when the first fails retryably; `retry.py` only
   retries the same provider.
3. `providers/fake.py` lets CI test every failure mode (429, 400, hang, malformed) with no key and
   no network; without it the gate could not run in CI, and failure handling would be untested.

## Q2. What surprised me

The first-draft tool descriptions still got 0.60 right on the fake model, and my case-sensitive id
pattern lost two calls to lower-case ids: the constraint I added for safety cost correctness until
I normalised the input.

## Q3. What I would change

Run the failure drill on a real provider; the fake answers in 0 ms, so the timeout and the cost
ceiling are not yet chosen from real numbers.

## Q4. What I contributed, and how I checked it

The assistant wrote all the code. Checked by running the week 1 tests on fake_a and fake_b, ruff
and mypy, reading the drill's wrong calls, and checking the decision numbers with records.py.

## Q5. Help I used

Claude Code (Claude Opus 5.5) wrote the code and records; see ai-use/week-1.yml. No reference
solution was read.

## Evidence

In evidence/week-1.json (fake providers, `--allow-fake`, since no key was available).

# Week 1 decision

## Decision

Failure policy: retry only retryable failures (429, 5xx, timeouts) up to 3 attempts with
exponential backoff from 0.5 s, a 20 s timeout per attempt, and a 400 or an unknown model fails
at once as `502 provider_error`. Tool ids are constrained by a pattern (`C-dddd`, `T-dddd`) and
normalised for case before validation. Model in `model.json` stays gemini / gemini-3.5-flash-lite.

Caveat, stated plainly: no provider key was available to this test fellow, so the evidence file
was produced with `scripts/evidence.py --allow-fake` on fake_a + fake_b. The numbers below prove
the plumbing and the descriptions, not real-model latency or quality; the policy numbers have to be
re-read off a real-model run before anyone relies on them.

## Options

- Tool descriptions as the first draft (`eval/tool_drill_before.json`): "Gets data.", "An id."
- My descriptions with an id pattern, but case-sensitive (first run: correct 0.90, two misses on `c-1003` and `t-2051`)
- My descriptions with an id pattern and case/space normalisation before validation (chosen)
- Failure policy: 3 attempts / 20 s timeout (chosen) against a fallback-only policy with no retries

## Evidence

- tool_drill.before.correct_rate = 0.60
- tool_drill.after.correct_rate = 1.00
- tool_drill.after.valid_args_rate = 1.00
- tool_drill.delta_correct_rate = 0.40
- schema_drill.enforced.ok_rate = 1.00
- failure_drill.policy.attempts = 3
- failure_drill.policy.timeout_s = 20.0
- failure_drill.providers.fake_a.cost_per_call_usd = 0.00047
- failure_drill.providers.fake_b.p95_ms = 0 (fake: answers instantly)

## Rejected

The case-sensitive id pattern: on the drill it rejected two requests where the person typed the
id in lower case (`c-1003`, `t-2051`), so correct calls were 0.90 rather than 1.00, and a model
that copies the user's casing would have been refused for no real reason. The first-draft
descriptions were rejected too: 0.60 correct against 1.00.

## Risk accepted

The numbers come from the fake providers, which choose tools by word overlap and answer
instantly, so p95 and cost here say nothing about a real model; a real 20 s timeout may be too
long for an interactive endpoint. I would watch p95 latency and retries per call on the first
real-model failure drill and lower the timeout if p95 sits far below it. Normalising ids also
means `c-1003` and `C-1003` are the same customer, which is the intent.

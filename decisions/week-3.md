# Week 3 decision

## Decision

Keep `RELEVANCE_THRESHOLD=0.30`, and do not trust the faithfulness judge on its own yet: it agrees
with my labels on two answers in three and is only ever wrong in the lenient direction.

Caveat, stated plainly: no provider key was available, so every number below is from the fake
model and the hash embedder (`evidence.py --allow-fake`, with `CHUNK_STRATEGY=section`,
`SEARCH_MODE=hybrid`). They show the mechanism and the shape of the trade, not real quality.

## Options

- Threshold 0.20
- Threshold 0.30 (chosen)
- Threshold 0.40
- Trust the judge's faithful rate as a quality number, or keep it as a flag that needs a person (chosen)

## Evidence

- threshold.curve[1].wrong_declines = 33
- threshold.curve[1].invented = 12
- threshold.curve[2].wrong_declines = 46
- threshold.curve[2].invented = 10
- threshold.curve[2].correct_declines = 10
- threshold.curve[3].wrong_declines = 63
- threshold.curve[3].invented = 6
- eval.metrics.abstain_rate_unanswerable = 0.5
- eval.metrics.answer_rate_answerable = 0.425
- eval.metrics.accuracy_version = 0.3
- judge.agreement = 0.667
- judge.confusion.judge_too_lenient = 10
- judge.confusion.judge_too_strict = 0
- trajectories.summary.correct_rate = 0.0 (no agent until week 4)

## Rejected

0.40: it halves nothing that matters enough. Inventions fall from 10 to 6, but wrong declines
rise from 46 to 63 of 80 answerable questions, so the desk would turn away most people it could
help. 0.20 was rejected the other way: 12 inventions reaching a customer for 13 fewer hand-overs.
Trusting the judge was rejected because all 10 of its disagreements with me are "too lenient".

## Risk accepted

At 0.30 the fake run still answers half of the unanswerable questions (abstain rate 0.5), which
is an invention reaching a customer. On a real model the second gate (`grounded: false`) should
catch more of these; I would re-run the curve on a real model and watch `invented` first.

The judge's disagreements are all answers that quote a real passage that does not address the
question: I labelled those unfaithful because the answer implies the passage answers the
question, while the judge, as prompted, grades only whether each sentence is in the passages. So
the judge measures support, not relevance; a relevance check (or answer accuracy against
`expect`) has to sit beside it.

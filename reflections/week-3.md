# Reflection — Week 3

Test fellow note: completed by an AI assistant (Claude Code) acting as a fellow.

## Q1. The concept, in my words

You cannot tell a confident wrong answer from a confident right one by reading it, so the system
must be able to decline, and every change must be measured against a fixed set of questions,
including ones it should refuse, before you believe it helped.

## Q1b. Reading questions

1. The threshold gate is free (it only reads the retrieval score); the `grounded` gate costs a
   model call. The free one must run first, or every hopeless question is paid for.
2. One accuracy number hides where it broke. A chunker regression shows first in hit rate and
   citation validity (the right passage is no longer retrieved); a prompt regression shows in
   abstention on unanswerables and in answer rate, with retrieval unchanged.
3. It can guess the version instead of looking it up with get_customer and still be right, or it
   can reach the right answer after calling a forbidden tool (an unapproved credit) or far too
   many steps.

## Q2. What surprised me

The judge was 100% "faithful" while a third of the answers did not address the question: a
faithfulness judge grades support, and a verbatim quote of the wrong passage is fully supported.

## Q3. What I would change

The variant files: `eval/golden.jsonl` names 30 documents by filenames corpus/ does not contain,
so the CI evaluation gate fails on citation validity regardless of the code. With the files
renamed to match (tried in a scratch copy, not committed), citation validity rose from 0.57 to
0.88 and passed; abstention on unanswerables stayed at 0.62 against a 0.70 floor.

## Q4. What I contributed, and how I checked it

The assistant wrote the code, the test set, the tasks and the labels. Checked by the week 3 tests
on both fakes, by reading every labelled answer against its passage, and by reproducing the eval
gate failure in a renamed scratch copy to separate data from code.

## Q5. Help I used

Claude Code (Claude Opus 5.5); see ai-use/week-3.yml. No reference solution was read.

## Evidence

evidence/week-3.json (fake model, hash embedder, section + hybrid).

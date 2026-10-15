TASK: judge
You grade one answer for faithfulness: is every claim in it supported by the numbered passages
it was given? You do not grade whether the answer is correct in the world, or helpful, only
whether the passages back it.

What a claim is:
- One statement that could be true or false on its own: a value, a default, a setting name, a
  step, a cause, a condition, a date, an amount. "The default is 15 seconds; set it with X" is
  two claims.
- Greetings, hedges and restating the question are not claims.

What support is:
- A claim is supported only when a passage states it, or it follows directly from what a passage
  states (a unit conversion, a paraphrase with the same meaning).
- Numbers, names, setting names and versions must match the passage exactly. A figure that is
  close, rounded differently or from another version is unsupported.
- Advice or steps that no passage gives are unsupported, however sensible they sound.
- Knowledge from outside the passages never counts as support, even if you believe it is true.

Biases to resist:
- Length: a long, detailed answer is not more faithful than a short one.
- Confident tone: certainty is not evidence.
- Plausibility: a claim that sounds right but appears in no passage is unsupported.
- Agreement: do not give credit because most of the answer is supported; one unsupported claim
  makes the answer not faithful.

Return ONLY a JSON object, no prose, with exactly these keys:
{"faithful": true or false, "claims": <number of claims>, "supported": <number supported>,
 "unsupported": [<each unsupported claim, quoted from the answer>], "reason": "<one sentence>"}
"faithful" is true only when supported equals claims.

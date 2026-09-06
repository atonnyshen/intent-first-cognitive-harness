---
name: intent-first-cognitive-harness
description: Triage natural-language requests, infer the user's goal, ask only material clarification questions, and select a small evidence-aware reasoning route. Use it when a request is vague, consequential, research-heavy, comparative, diagnostic, strategic, or explicitly asks for structured analysis; pass through simple mechanical work.
metadata:
  version: "0.1.0"
  mode: "host-neutral"
  evidence_status: "research-preview"
---

# Intent-first Cognitive Harness

Treat the user's ordinary request as the interface. The user does not need to know framework names, route fields, stakes, or schemas.

```text
raw request
→ triage
→ intent and desired outcome
→ minimum necessary clarification
→ small reasoning route
→ evidence-aware work
→ outcome-first answer
```

## Behaviour

1. Inspect every request when the host supports ambient skill use. Pass simple formatting, translation, or mechanical work through without ceremony.
2. Infer the subject, user job, desired outcome, deliverable, audience, scope, constraints, stakes, evidence needs, assumptions, and material unknowns.
3. Ask only questions whose answers could change the route, scope, safety, or result. Prefer one plain-language A/B/C question over a framework questionnaire.
4. Use tools, files, and available context before asking the user for information that can be retrieved safely.
5. Select the smallest useful reasoning route. Keep facts, assumptions, unknowns, hypotheses, and recommendations distinct.
6. If a required input is unavailable and material, stop with a clear explanation. Do not invent a framework item, source, human review, or host capability.
7. Give the result first. Explain the route only when the user asks or the work needs an audit trail.

## Clarification examples

- “你最後要拿這份結果做決策、做提案，還是先把事情查清楚？”
- “比較時你最在意成本、速度，還是長期風險？”
- “這份內容是給自己使用，還是要交給一般讀者？”

Do not ask the user to choose a hidden framework. The framework layer is an implementation detail.

## Boundaries

This Skill is a research preview. It does not claim official affiliation with any named framework, complete current coverage, reliable semantic activation on every host, human preference validation, or production readiness. Historical cognitive frameworks may be used only when their source status and limitations are stated.

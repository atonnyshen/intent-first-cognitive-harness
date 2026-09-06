# Question compiler contract

The compiler turns an already selected route into observable question pools. It does not decide the user’s intent and does not expose a framework checklist to the user.

Each route may provide `analysis_questions`, `research_questions`, `user_questions`, and `critic_questions`. Questions that can be answered from files or tools belong in `research_questions`; questions only the user can answer belong in `user_questions`. A material unresolved requirement returns `NEEDS_INPUT`.

Deterministic compiler output proves the shape of a route, not the quality of semantic selection or the usefulness of the final answer.

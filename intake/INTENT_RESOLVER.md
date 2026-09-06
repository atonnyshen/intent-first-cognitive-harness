# Intent resolver contract

Turn ordinary language into a small working brief. This is a semantic model task; a keyword classifier cannot prove that the inferred intent is correct.

1. Read the current request and directly relevant context.
2. State a provisional user-job hypothesis.
3. Extract the subject, desired outcome, deliverable, audience, scope, constraints, evidence needs, assumptions, and unknowns.
4. Mark a missing detail as material only when it could change the route, scope, safety, or result.
5. Retrieve safe-to-retrieve facts with available tools before asking the user.
6. Ask the minimum plain-language question when a material gap remains.

Use `PASS_THROUGH` for simple mechanical work, `READY` when the task can start, `ASK` when one to three answers would materially change the work, and `BLOCKED_USER_INPUT` when a user-only fact is necessary and cannot be safely assumed.

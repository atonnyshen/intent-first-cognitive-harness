# Intent-first Cognitive Harness

[繁體中文](README.zh-TW.md)

## Start with the problem, not with a framework

You can simply write:

> I have three ways to reorganise our research notes, and I keep changing my mind. Help me decide what to do next month.

The documented Skill flow starts by working out what a useful result would be. It is designed to fill in the audience, deliverable, scope, constraints, and evidence needs when the context supports that. It asks a short plain-language question only when the missing answer could change the work, then chooses a bounded reasoning route. That is the intended interface; semantic quality is still under validation.

You do not need to know Minerva HC names, route fields, risk labels, or JSON. Those are internal organisation tools, not an entry requirement.

## What happens after installation

You install a `SKILL.md`, not a new model, chat application, or background service. Once your Agent Host loads it, the flow is:

1. You describe the task in your usual words.
2. The documented flow checks whether the request is clear enough to handle directly or needs intent resolution.
3. Clear, low-risk mechanical work such as translation or formatting passes through without framework ceremony.
4. The documented flow gives research, comparison, decision, diagnosis, planning, forecasting, or communication requests a short working brief first.
5. The policy prioritises files, tools, and public sources; it reserves user questions for consequential facts that only you can provide.
6. The output contract keeps facts, assumptions, unknowns, hypotheses, and recommendations distinct, with review conditions when they matter.

On a host that supports ambient Skills, this front door can inspect each request and choose whether to pass it through or continue into analysis. It does not mean every request runs the full pipeline. Keeping simple work simple is part of the design. If a host does not support ambient loading, you can invoke the Skill explicitly or follow that host’s loading mechanism.

## How you use it

After installation and a new Agent session, write naturally:

```text
Compare these three tools for a five-person team. We cannot migrate again within three months; separate cost, learning time, and long-term risk.

This workflow sometimes skips clarification. Find the likely failure boundary and give me a test plan that I can rerun.

I need to give this research result to non-technical readers. First work out what they need to know, then rewrite it.

Translate this paragraph into Traditional Chinese and keep the names unchanged.
```

Under the documented policy, the first three requests are intended to enter intent resolution. The last one should normally pass through as a direct translation. This is a policy example, not a cross-host semantic guarantee. You do not need to say “use HC” or choose an internal capability.

## How it fills in the missing requirements

The documented flow forms a small working brief and checks what can change the result:

- What are you trying to accomplish, rather than merely learn?
- Who will use the result?
- Do you need an answer, decision, plan, research record, or ready-to-send text?
- Are there deadlines, budgets, permissions, risks, or format constraints?
- Which facts can be retrieved, and which facts only you know?

It makes a labelled, reversible assumption when a gap is safe to bridge. It asks when the gap could change the scope, audience, safety, recommendation, or deliverable. The default question budget is zero; ordinary clarification is kept to one to three questions. When a host has no native menu, a short A/B/C text fallback is available.

## What Minerva HC means here

Here, HC refers to Habits of Mind and Foundational Concepts in the public Minerva educational context. They can be understood as reusable thinking habits: define the problem, inspect evidence, decompose causes, compare alternatives, account for audiences and constraints, and decide what to do next. The point is not to memorise a checklist. It is to choose a few useful checks for the problem in front of you.

This project keeps that layer inside the Skill. The public contract turns a user’s ordinary request into research questions, user questions, counterexamples, and observable outputs. It does not ask the user to choose an HC, and it does not apply every HC at once.

The project was also inspired by ideas about problem definition, thinking habits, and working with AI discussed by 李佳達 in public interviews and course material. One public interview is available [here](https://www.youtube.com/watch?v=0eFbBsE9Vlk). This is an independent open-source implementation. It has no collaboration, affiliation, licence, or endorsement relationship with 李佳達, Minerva University, or Minerva Project; it does not reproduce course material or claim official compatibility.

The research makes one deliberately narrow historical claim: Appendix I of the 2020 IDB / Minerva publication is recorded as a 79-item snapshot within that publication. This is not a current official taxonomy, and it cannot be turned into a claim of a complete current official set of 78 items. English/Spanish rendered-asset equivalence remains unresolved. See the [IDB publication](https://publications.iadb.org/publications/spanish/document/Como-preparan-los-innovadores-disruptivos-a-los-estudiantes-de-hoy-para-ser-la-fuerza-laboral-del-manana-El-modelo-cooperativo-de-Minerva-Un-camino-para-cerrar-la-brecha-de-habilidades.pdf).

The project now accounts for every item in that verified publication snapshot and maps the items into a versioned capability model. Executable coverage is measured by distinct cognitive capabilities, not by forcing one executable card per historical label. This is a research and engineering boundary, not a claim that the current official Minerva taxonomy is complete.

## The reasoning tools are inspectable

Every card in the current stable capability set is a project-derived specification of when to use the capability, what inputs it needs, what procedure to run, what inspectable artifact to produce, how it can fail, and how to critique and score the result. All 21 / 21 cards meet this project’s official-grade executable quality contract. That is an engineering and teaching-quality statement; it is not a claim of Minerva authorship, a current taxonomy, semantic runtime verification, human validation, or production readiness.

For an ordinary user, these fields stay internal. You describe the situation in your own words; the front door decides whether it can pass through directly, then turns the useful cognitive work into a small number of plain-language questions, evidence lookups, and inspectable outputs. Minerva HC is a historical reference layer here. The procedures, artifacts, critics, and rubrics are project-authored and kept separate from source provenance.

## Install: the shortest working path today

There is no npm package in this release, so there is no misleading `npm install` command. An Agent Skill is discovered by the host. Download this repository from GitHub, then place the complete Skill directory in a registry that your host can read.

For a workspace that supports `.agents/skills/`:

```bash
git clone https://github.com/atonnyshen/intent-first-cognitive-harness.git
mkdir -p .agents/skills/intent-first-cognitive-harness
cp intent-first-cognitive-harness/SKILL.md \
  .agents/skills/intent-first-cognitive-harness/SKILL.md
```

If you downloaded a ZIP from GitHub, replace `intent-first-cognitive-harness` with the extracted directory. If your host has a different native Skill directory, put the same folder there:

| Host | Installation rule | Evidence in this release |
|---|---|---|
| Codex | Use the host-supported `.agents/skills/` or user Skill directory | Public contracts; no cross-version semantic guarantee |
| Claude Code | Use the host-supported `.claude/skills/` directory | Public contracts; no cross-version semantic guarantee |
| Antigravity / AGY | Use the workspace Skill directory supported by the host, usually checking `.agents/skills/` first | Bounded AGY runtime evidence; not automatic-activation acceptance |
| Gemini CLI / OpenCode | Follow each host’s current Skill discovery rules | Native Host acceptance not completed in this release |
| Another Agent Host | Load `SKILL.md` through its Skill registry | Collect a host receipt before making a stronger claim |

Restart the Agent session and try:

```text
I have a problem but I do not know how to break it down. First tell me what goal you think I have; ask only what you truly need.
```

If the host cannot find the Skill, check its discovery directory and session reload behaviour first. That is a loading problem, not evidence that the Skill has run.

## Is it simple enough for ordinary users?

For everyday use, the interface contract is aimed at the target: users can start in their own words, do not need HC vocabulary, and have a documented direct path for simple requests. Clarification is phrased in terms of the result, audience, and constraints instead of internal fields. Human usability and preference have not been measured yet.

For installation, it is currently “manual but short”: copy one `SKILL.md`, restart the session, and try a prompt. It is not yet a one-click installer, and it does not become native in every host through `npm install`. A real one-command experience still requires a stable repository, a host-version matrix, an installer, and native discovery tests for each supported host.

For automatic activation, the promise is deliberately limited. A host that loads the Skill as an ambient instruction can inspect each request, but a Markdown file cannot create ambient loading where the host does not provide it. Current tests cover engineering contracts, routing, and observable outputs. They do not prove that every host discovers the Skill, chooses the right route, asks useful questions, and recovers correctly.

That is the honest boundary for this first public preview.

## Current status

| Layer | Status | Meaning |
|---|---|---|
| Engineering contract | `PASS_FOR_SCOPE` | Contracts, routing, validation, and observable outputs are rerunnable |
| Semantic runtime | `FORMATIVE_ONLY / BLOCKED_EVIDENCE` | Real-language runtime records exist, but broader semantic evaluation is still needed |
| Human preference | `NOT_RUN` | No human ratings or preference votes are invented |
| Host-native | `BLOCKED` | Complete interaction receipts for the main hosts are not complete |
| Production | `NO_SHIP` | This is not claimed to be production-ready |

Read [public scope](docs/PUBLIC_SCOPE.md), [provenance and limitations](docs/PROVENANCE_AND_LIMITATIONS.md), and [host compatibility](docs/HOST_COMPATIBILITY.md) before making a stronger claim. The repository intentionally excludes private prompts, unreviewed web-question corpora, raw source extracts, human data, and unresolved HC cards.

## Licence and contribution

Project-owned files in the public tree are released under the MIT License. MIT does not relicense third-party names, logos, quotations, course material, datasets, or source documents; see [NOTICE.md](NOTICE.md).

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a change. For a host-activation report, include the host, version, install location, test input, observed output, and recovery result. Do not include private data or confidential prompts. Security reports should follow [SECURITY.md](SECURITY.md), not a public issue.

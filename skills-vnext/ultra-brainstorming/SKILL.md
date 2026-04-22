---
name: ultra-brainstorming
description: Design-first discovery for Codex Ultra vNext. Use before planning or implementation whenever the request is ambiguous, creative, architecture-sensitive, or likely to span multiple files, workflows, or user-facing behavior. This skill turns a vague idea into an approved spec with one-question-at-a-time clarification, alternative comparison, and an explicit implementation gate.
---

# Ultra Brainstorming

Use this skill to create a design-quality front end before planning or coding.
This is the main vNext upgrade inspired by `obra/superpowers`.

## Hard Gate

Do not move to planning or implementation until you have:

1. explored the project context
2. clarified ambiguities one question at a time when needed
3. proposed 2-3 approaches with tradeoffs
4. presented a recommended design
5. received explicit approval or resolved objections

If the task is truly tiny, compress the design. Do not skip it.

## Workflow

1. Explore the codebase, docs, recent diffs, and any existing specs.
2. Assess whether the request is one bounded change or several independent
   subsystems. Decompose if needed.
3. Ask one clarifying question at a time. Prefer multiple choice when useful.
4. Propose 2-3 approaches with your recommendation first.
5. Present the design in sections sized to the complexity.
6. Write the approved spec artifact.
7. Self-review for ambiguity, contradiction, and hidden scope creep.
8. Hand off to `ultra-planning`.

## Preferred Outputs

At minimum produce:

- problem framing
- non-goals
- success criteria
- constraints
- proposed architecture or flow
- testing or verification intent
- open decisions or assumptions

If the repo uses OpenSpec, write into `proposal.md`, `design.md`, and
`tasks.md` under the relevant `openspec/changes/<change-id>/` directory.

## Quality Bar

- surface ambiguity instead of silently picking an interpretation
- prefer the simplest design that satisfies the request
- avoid speculative abstractions
- explicitly call out acceptance criteria that downstream planning will need

Read [brainstorming-flow](references/brainstorming-flow.md) and then rely on
`ultra-vnext-core` for the shared contracts.

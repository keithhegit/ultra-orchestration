# Codex Ultra-Orchestrator v1 Whitepaper

## 1. Executive Summary

Codex Ultra-Orchestrator v1 is a skill-based orchestration system for Codex. Its purpose is to move Codex from a capable single execution agent to a multi-stage orchestrator that can normalize requests, create decision-complete plans, dispatch role-based work, enforce safety gates, review outputs, verify behavior, package results, and improve through retrospection.

This system is the result of combining three different sources of inspiration:

- `superpowers` for skill organization and workflow scaffolding
- `Ultra-Orchestrator` for control-plane thinking, task graphs, risk gates, and structured outputs
- `gstack` for role-based engineering flow, sprint closure, and practical safety guardrails

The resulting design is intentionally lightweight for v1. It does not start as a separate orchestration platform. Instead, it starts as a reusable Codex skill suite plus a shared protocol, common contracts, a minimal execution ledger, and validation helpers.

The key idea is simple: before making orchestration more autonomous, make orchestration more structured.

## 2. Why This Exists

Modern coding agents are very effective on narrow tasks, but they often become unstable as work grows in size and ambiguity. Common failure modes include:

1. Planning, implementation, review, and QA collapse into one undifferentiated conversation.
2. Multiple agents can be launched, but there is no reliable ownership model or handoff structure.
3. Complex work is done in parallel without write-scope control, causing conflicts and hidden regressions.
4. Final answers summarize outcomes, but do not preserve enough evidence to audit how the result was reached.
5. Safety decisions happen ad hoc instead of through a visible policy gate.

The real need is not just ?more agents.? The real need is:

- a staged workflow
- explicit role boundaries
- structured intermediate artifacts
- safe parallelism
- review and QA gates
- auditable outputs
- a small but durable execution record

Codex Ultra-Orchestrator v1 is designed to meet that need.

## 3. Initial Planning Goal

The original planning goal was precise:

> Improve Codex?s orchestration ability significantly without starting with a heavyweight standalone orchestrator product.

That led to a v1 strategy centered on these capabilities:

- intake normalization
- decision-complete planning
- task graph construction
- role-based dispatch
- shared write-scope protection
- spec review and engineering review
- QA verification
- delivery packaging and retrospection

And it explicitly avoided starting with:

- a dedicated backend orchestration service
- long-lived distributed scheduling
- cross-session persistent infrastructure
- deployment automation as a required core
- browser infrastructure as a hard dependency

This was an important strategic choice. It made v1 a protocol-and-skills system first, instead of a platform-first system.

## 4. What Each Input Contributed

### 4.1 What `superpowers` contributed

`superpowers` was most useful as a method-layer reference. It suggests that complex agent behavior should be broken into reusable skills and composable workflows rather than buried inside one oversized system prompt.

Its strongest contributions to this design were:

- skill-oriented composition
- workflow scaffolding
- modularity over monolithic prompting
- reusable process patterns instead of one-off prompting style

Its limits were also clear:

- it is stronger on skill organization than on control-plane rigor
- it does not by itself define a strong run ledger model
- it does not emphasize risk gates and structured orchestration outputs as strongly as needed here

So in this project, `superpowers` became the organizational skeleton, not the orchestration core.

### 4.2 What `Ultra-Orchestrator` contributed

Your Ultra-Orchestrator brief provided the core control-plane mindset for this system. It contributed the most important orchestration primitives:

- explicit orchestration phases
- task graph thinking
- risk classification before external tool use
- mandatory structured outputs
- multi-lens review
- orchestration logs and vetter reports

These were foundational because they answer the hard orchestration questions:

- how work is decomposed
- how risk is classified
- how outputs are reviewed
- how the process is recorded

Its main limitation was not conceptual weakness but packaging. The brief was strong as an orchestration design, but it still needed to be translated into Codex-native skills, contracts, references, and runnable helpers.

That is exactly what v1 implements.

### 4.3 What `gstack` contributed

`gstack` contributed the strongest role-based engineering workflow model. Its value was not mainly in a specific runtime, but in turning agent work into something that resembles an engineering team operating through a sprint cycle.

Its most useful contributions were:

- clear stage closure similar to Think -> Plan -> Build -> Review -> Test -> Ship -> Reflect
- explicit specialist roles
- structured upstream-to-downstream artifact passing
- practical planning automation patterns like `autoplan`
- practical safety patterns like `careful`, `freeze`, and `guard`

It reinforced a critical lesson: orchestration is not just about dispatching tasks. It is also about assigning the correct role to each phase of work and ensuring downstream phases inherit the right artifacts.

Its limits were equally important:

- it is strongly shaped by Claude Code slash-command ergonomics
- some of its later-stage capabilities are better treated as v2 or v3 extensions for Codex
- it should be adapted for Codex rather than copied verbatim

So `gstack` became the main inspiration for role design and sprint closure, not the exact host interface.

## 5. Why These Three Were Fused

The three systems are complementary rather than interchangeable.

- `superpowers` answers: how should orchestration capabilities be packaged?
- `Ultra-Orchestrator` answers: how should orchestration itself be structured, audited, and guarded?
- `gstack` answers: how should a multi-role engineering workflow feel in practice?

That leads to a three-layer fusion model:

- Method layer: `superpowers`
- Control layer: `Ultra-Orchestrator`
- Role workflow layer: `gstack`

Without this fusion, each source is incomplete for the Codex use case:

- `superpowers` gives modularity but not enough orchestration control
- `Ultra-Orchestrator` gives control but not enough role-driven workflow ergonomics
- `gstack` gives roles and closure but not enough Codex-native shared contracts and control-plane rigor

The fusion is what creates a coherent Codex orchestration system.

## 6. Core Design Principles

The final v1 design follows these principles.

### 6.1 Protocol First

Define stages, contracts, outputs, and safety rules before building platform-level infrastructure.

### 6.2 Skills Before Platform

Ship reusable skills and a common orchestration protocol before investing in a dedicated orchestrator service.

### 6.3 Structured Handoffs

Every phase must leave behind artifacts that a later phase can consume directly.

### 6.4 Review Before Integration

Unreviewed results should not be treated as integration-ready.

### 6.5 Safe Parallelism Only

Parallelism is allowed only when write scope and dependency conditions make it safe.

### 6.6 Auditability Is A Feature

An orchestration system should preserve enough execution history to understand what happened, why, and with what risk.

## 7. The v1 Workflow

The fixed orchestration workflow is:

1. `Intake`
2. `Plan`
3. `Dispatch`
4. `Execute`
5. `Review`
6. `QA`
7. `Deliver`
8. `Retro`

### 7.1 Intake

Purpose:

- normalize a raw request
- identify task description, context, success criteria, constraints, and task type
- detect whether risk vetting is needed before execution

Why it matters:

- it prevents the planner from working off vague conversational intent alone

### 7.2 Plan

Purpose:

- produce a decision-complete plan
- generate task manifests and work packages
- record dependencies, owned paths, expected outputs, and non-goals
- mark serial versus parallel boundaries

Why it matters:

- it removes hidden decisions from implementation time

### 7.3 Dispatch

Purpose:

- assign work by role
- enforce boundaries
- update the execution ledger
- track retries, blockers, and review readiness

Why it matters:

- it turns one big request into bounded units of work

### 7.4 Execute

Purpose:

- perform assigned work packages
- parallelize only when safe
- retry transient failures once
- escalate hard blockers with context and evidence

Why it matters:

- it preserves speed without sacrificing control

### 7.5 Review

Purpose:

- verify specification consistency first
- verify engineering quality second
- challenge evidence, assumptions, and regression risk

Why it matters:

- it stops ?looks finished? from being treated as ?is correct?

### 7.6 QA

Purpose:

- validate behavior and scenarios
- focus on happy path, error path, and regression risk
- require regression thinking for bug fixes

Why it matters:

- it shifts confidence from code shape to actual behavior

### 7.7 Deliver

Purpose:

- assemble user-facing results
- assemble orchestration log
- assemble vetter report
- summarize residual risk and next actions

Why it matters:

- it produces an output that is both consumable and auditable

### 7.8 Retro

Purpose:

- capture what worked in the orchestration pattern
- identify improvements for future runs

Why it matters:

- it allows the orchestration system itself to improve over time

## 8. Role Model

The v1 system defines seven roles:

- `Intake Lead`
- `Planner`
- `Architect/Eng Reviewer`
- `Worker`
- `Reviewer`
- `QA`
- `Integrator`

This role model comes largely from the useful parts of `gstack`, adapted for Codex.

### 8.1 Why roles matter

Without role discipline, agents blur responsibilities:

- planners silently become implementers
- implementers silently fill in design gaps
- reviewers approve work without clear acceptance checks
- integrators redo delegated work and break auditability

### 8.2 Role discipline rules

v1 enforces a few explicit norms:

- `Planner` should not jump into broad implementation
- `Reviewer` should not approve work with undefined acceptance criteria
- `Integrator` should not quietly redo delegated tasks

These rules preserve clarity, ownership, and useful logs.

## 9. Shared Contracts

To avoid loose, memory-based handoffs, v1 defines shared data contracts.

### 9.1 `TaskManifest`

Represents a task and includes:

- `id`
- `goal`
- `context`
- `success_criteria`
- `constraints`
- `owned_paths`
- `dependencies`
- `expected_outputs`
- `risk_level`
- `non_goals`

### 9.2 `WorkPackage`

Represents assigned work for a specific role and includes:

- `task_id`
- `role`
- `scope`
- `owned_paths`
- `input_artifacts`
- `acceptance_checks`
- `report_format`

### 9.3 `AgentResult`

Represents a worker?s structured return payload and includes:

- `task_id`
- `status`
- `summary`
- `changed_paths`
- `artifacts`
- `evidence`
- `risks`
- `followups`

### 9.4 `ExecutionLedger`

Represents the lightweight run-state record and includes:

- current stage
- task status
- dependency status
- retry counts
- blockers
- pending review items
- integration status

### 9.5 `RunOutput`

Represents the final run package and must include:

- `final_deliverable`
- `orchestration_log`
- `vetter_report`

These contracts create a shared language for all skills in the suite.

## 10. Safety And Guardrails

v1 uses two layers of safety.

### 10.1 Risk Vetter

Derived mainly from Ultra-Orchestrator thinking.

Before using unfamiliar tools, broad write scope, destructive commands, or external systems, classify risk as:

- `LOW`
- `MEDIUM`
- `HIGH`
- `EXTREME`

Policy:

- `LOW`: allow
- `MEDIUM`: allow with guardrails
- `HIGH`: require explicit approval
- `EXTREME`: block unless clearly approved

### 10.2 Safety Guard

Inspired mainly by `gstack`.

It introduces three practical safety modes:

- `careful`: warn before dangerous or high-impact actions
- `freeze`: restrict the writable scope
- `guard`: combine careful and freeze

This gives the system practical execution-time protection without requiring a large policy engine.

## 11. What Was Implemented In The Workspace

The following skill suite has already been created in this workspace:

- [ultra-orchestrator](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/SKILL.md)
- [clarify-and-intake](/D:/Codex_workspace/.agents/skills/clarify-and-intake/SKILL.md)
- [decision-complete-planner](/D:/Codex_workspace/.agents/skills/decision-complete-planner/SKILL.md)
- [dispatch-and-track](/D:/Codex_workspace/.agents/skills/dispatch-and-track/SKILL.md)
- [spec-review](/D:/Codex_workspace/.agents/skills/spec-review/SKILL.md)
- [code-review](/D:/Codex_workspace/.agents/skills/code-review/SKILL.md)
- [qa-verify](/D:/Codex_workspace/.agents/skills/qa-verify/SKILL.md)
- [deliver-and-retro](/D:/Codex_workspace/.agents/skills/deliver-and-retro/SKILL.md)
- [risk-vetter](/D:/Codex_workspace/.agents/skills/risk-vetter/SKILL.md)
- [safety-guard](/D:/Codex_workspace/.agents/skills/safety-guard/SKILL.md)
- [autoplan](/D:/Codex_workspace/.agents/skills/autoplan/SKILL.md)

The main shared references are here:

- [contracts.md](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/references/contracts.md)
- [workflow.md](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/references/workflow.md)
- [review-lenses.md](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/references/review-lenses.md)
- [examples.md](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/references/examples.md)

Two runnable helper scripts were also implemented:

- [new_run.py](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/scripts/new_run.py)
- [validate_run.py](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/scripts/validate_run.py)

Example artifacts are included here:

- [feature-intake.json](/D:/Codex_workspace/examples/feature-intake.json)
- [feature-run-output.json](/D:/Codex_workspace/examples/feature-run-output.json)

## 12. What Has Been Verified

The following has been verified in the workspace:

1. All skill folders exist.
2. All skill folders include both `SKILL.md` and `agents/openai.yaml`.
3. `new_run.py` successfully scaffolds a run directory.
4. `validate_run.py` successfully validates the generated run artifacts.
5. Example intake and run-output files are present.

One limitation during validation was that the upstream `quick_validate.py` helper from the system `skill-creator` package could not run in this environment because `PyYAML` was unavailable. That did not block local verification of the implemented artifacts.

## 13. How To Try It Right Now

### 13.1 Read the main orchestrator skill

Start with:

- [ultra-orchestrator/SKILL.md](/D:/Codex_workspace/.agents/skills/ultra-orchestrator/SKILL.md)

Then read the references and child skills as needed.

### 13.2 Use it as a manual orchestration protocol

The easiest way to try v1 today is to use it manually as a skill-guided workflow:

1. Run intake with `$clarify-and-intake`
2. Produce a plan with `$decision-complete-planner`
3. Audit the plan with `$spec-review`
4. Track and dispatch with `$dispatch-and-track`
5. Review implementation with `$code-review`
6. Verify behavior with `$qa-verify`
7. Package results with `$deliver-and-retro`

This simulates a lightweight orchestrated sprint even before deeper automation exists.

### 13.3 Use `autoplan` for planning-only runs

If the immediate need is faster planning discipline, use `$autoplan`. It chains:

- intake
- planning
- spec review
- refinement

This is a good first trial if you want to test the planning side of the system before full execution.

### 13.4 Create a run shell

You can scaffold a run like this:

```bash
python .agents/skills/ultra-orchestrator/scripts/new_run.py run-20260325-001 --path runs
```

That creates:

- `ledger.json`
- `run-output.json`
- `task-manifests.json`

### 13.5 Validate a run

After a trial run, validate the structure like this:

```bash
python .agents/skills/ultra-orchestrator/scripts/validate_run.py runs/run-20260325-001
```

## 14. Expected Value

The expected value of this system is not just ?more speed.? The larger value is improved stability, control, and repeatability in complex agent-assisted work.

### 14.1 Better decomposition

Complex work becomes bounded work packages with dependencies, owned paths, and acceptance checks.

### 14.2 Better parallelism

Parallel work is driven by safety and scope boundaries, not just opportunistic concurrency.

### 14.3 Better review quality

The system separates spec review, engineering review, and QA verification rather than collapsing all quality checks into one vague step.

### 14.4 Better safety

Risk vetting and practical guardrails reduce the chance of unsafe execution.

### 14.5 Better auditability

The orchestration log and vetter report make it easier to answer:

- what was done
- why it was done this way
- where risk remained
- what was actually verified
- why an action was allowed or blocked

### 14.6 Better reuse

Because the system is skill-based, it can be applied across multiple projects and repeated workflows.

## 15. Suitable Scope

This skill combination is best suited for:

### 15.1 Multi-file feature development

Especially when work crosses modules and needs explicit planning and review.

### 15.2 Bug investigation and repair

Especially when a disciplined flow is needed from investigation through verification.

### 15.3 Team-style agent-assisted engineering

Especially when Codex is being used as a collaborator rather than just a code generator.

### 15.4 Repeatable delivery workflows

Such as:

- feature iteration
- bug fixing
- review and verification cycles
- structured reporting
- workflow automation work

## 16. Out Of Scope For v1

To keep v1 practical and focused, these are not core requirements yet:

- a standalone orchestrator service
- long-lived cross-session state infrastructure
- automatic deploy and release control
- built-in real-browser QA infrastructure
- long-term telemetry systems
- hardcoded domain-specific rules inside the core protocol

These remain valid future directions, but should not block v1 adoption.

## 17. Current Limitations

This system is intentionally incomplete in some ways:

1. It is a skill suite and orchestration protocol, not yet a full product runtime.
2. The execution ledger is lightweight and file-based.
3. Automatic sub-agent dispatch is not yet packaged as one unified executor.
4. QA is defined structurally, but browser-backed QA is not yet built in.
5. Risk vetting is contract-based and procedural, not backed by a full policy engine.

These are expected v1 boundaries, not design failures.

## 18. Implementation Philosophy

The philosophy behind v1 is:

> Make orchestration reliable before making orchestration fully automatic.

Many agent systems focus first on autonomy, concurrency, and scale. This project takes the opposite approach:

- define the structure first
- define the handoffs first
- define the evidence model first
- define the safety boundaries first
- then expand automation

That makes the system slower to overclaim, but stronger in practice.

## 19. Recommended Next Steps

### 19.1 Run real pilot tasks

Use the system on a small set of real tasks such as:

- one multi-file feature
- one real bug investigation and fix
- one planning-plus-review-only high-risk change

Evaluate:

- whether intake is stable
- whether plans are truly decision-complete
- whether review catches real issues
- whether the orchestration log is genuinely useful

### 19.2 Tighten the shared contracts

Refine the schemas over time:

- remove fields that do not add value
- add fields only when repeated runs prove they are necessary
- improve handoff artifacts between phases

### 19.3 Add dispatch helpers

If pilots go well, add more automation around:

- sub-agent dispatch templates
- result collection
- ledger updates
- gate-check automation

### 19.4 Add domain packs

Keep the core generic, then extend with domain-specific packs such as:

- frontend delivery pack
- backend migration pack
- debugging pack
- audit/reporting pack

## 20. Final Assessment

Codex Ultra-Orchestrator v1 is a practical orchestration architecture for Codex, not just a multi-agent slogan.

Its value comes from combining the right parts of three different systems:

- `superpowers` for modular skill composition
- `Ultra-Orchestrator` for orchestration control and auditability
- `gstack` for role-driven engineering workflow and safety ergonomics

Taken separately, each one is useful but incomplete for the Codex use case. Taken together, they create a system that can:

- plan
- decompose
- dispatch
- review
- verify
- deliver
- retrospect
- and preserve evidence along the way

For Codex, that is the difference between an agent that can do work and an agent that can organize work.

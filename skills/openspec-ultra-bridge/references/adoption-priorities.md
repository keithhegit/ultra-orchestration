# Adoption Priorities

Use this reference when the goal is to absorb OpenSpec strengths without damaging the current Ultra-Orchestrator architecture.

## First-priority advantages to absorb

### 1. Persistent spec assets

Adopt OpenSpec as the long-lived home for:

- proposal
- design
- tasks
- archive

Why it matters:

- it gives the project a durable spec source-of-truth
- it reduces dependence on chat-history memory
- it improves cross-session continuity

### 2. Change-based workflow

Use OpenSpec change objects as the preferred planning unit before execution starts.

Why it matters:

- it forces scope clarity
- it creates cleaner change boundaries
- it fits naturally with worktree isolation and run tracking

### 3. Archive discipline

Do not treat implementation completion as the end of the lifecycle.

Require archive gating so that approved work can be merged back into long-lived spec assets only after:

- review passes
- QA passes or residual risk is explicitly accepted
- archive conditions are satisfied

### 4. Spec-first task decomposition input

Use OpenSpec tasks as a structured upstream input for Ultra `WorkPackage` generation.

Why it matters:

- it raises task quality before dispatch
- it reduces ad hoc decomposition in execution time
- it makes acceptance checks more explicit

## What not to absorb first

Do not prioritize these before the bridge is stable:

- replacing Ultra's state machine
- replacing Ultra review and QA gates
- replacing Ultra ledger ownership
- broad automatic event-loop orchestration
- full browser or environment automation as a bridge requirement

## The architecture rule

Use OpenSpec as:

- high-quality spec frontend
- long-term spec backend

Use Ultra-Orchestrator as:

- execution control plane
- review and QA gatekeeper
- risk and ledger owner

# Ultra vNext Design Tenets

## Protocol First

Define contracts, roles, and transitions before building automation.

## Artifact-Driven Handoff

Downstream agents receive structured artifacts, not long natural-language
history. This is the context firewall.

## Review Before Integration

Unreviewed work is incomplete work.

## Host-Driven State

The host owns ledger mutation. The model should suggest updates, not rewrite
large global state blobs from memory.

## Graph-And-Lock Parallelism

Parallel execution is allowed only when the dependency graph is ready and the
write scopes are disjoint.

## Auditability As A Feature

Every run should leave behind enough evidence to answer:

- what changed
- why it changed
- what risk was accepted
- what remains uncertain

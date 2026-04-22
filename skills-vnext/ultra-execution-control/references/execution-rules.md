# Execution Rules

## Dispatch

- only dispatch ready nodes
- never dispatch overlapping writers in parallel
- freeze path boundaries for worker tasks

## Retry

- allow one bounded retry for transient failures
- attach failure context to the retry package
- escalate when the second attempt would just repeat the same mistake

## Blocker Report

Include:

- what blocked the work
- what evidence supports that claim
- what was attempted
- what should happen next

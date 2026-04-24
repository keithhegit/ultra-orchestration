# Examples

## Minimal orchestration log entry

```json
{
  "stage": "dispatch",
  "task": "task-002",
  "owner": "Integrator",
  "status": "done",
  "notes": "Serialized task-002 after detecting shared write scope with task-001"
}
```

## Minimal vetter decision

```json
{
  "checked_items": ["Use new external browser automation tool"],
  "risk_level": "HIGH",
  "decisions": [
    "Blocked pending explicit user approval"
  ]
}
```

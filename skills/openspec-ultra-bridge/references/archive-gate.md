# Archive Gate Reference

Allow archive only when all of the following are true:

- review passed or was explicitly accepted with follow-ups
- QA passed or residual risks were explicitly accepted
- risk vetter does not block the change
- final deliverable exists
- change artifacts and execution artifacts point to the same change intent

Block archive when:

- implementation drifted from proposal/design
- key acceptance checks remain unverified
- known high-risk issues remain unresolved

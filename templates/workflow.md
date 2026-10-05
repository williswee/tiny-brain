# First task

This is a blank authoring format. Replace its guidance with the user's chosen task
when saving a workflow. It is not a default task or an executable native command.

During demo mode, follow `commands/demo.md`: preview steps and results in chat,
simulate saves, and execute no task tools, regardless of this workflow's policy.

## When to use

Describe the request this workflow helps with.

## Inputs

List only inputs needed to do the task. Reuse inputs already supplied.
Ask for missing essential inputs; label assumptions for optional inputs.

## Steps

1. Establish the requested outcome from the supplied inputs.
2. Do the task, using relevant context and available sources.
3. Check the result against the requested outcome; identify unresolved questions.

## Output

Describe the useful artifact and its structure.

For analysis or feedback with a useful next move, include one grounded
recommendation, a brief reason, and the smallest useful next action. Provide a
short draft, example, or first step in chat when appropriate, following
`AGENTS.md`'s "Help the user move forward" guidance. Adapt to missing critical
context, user-owned decisions, uncertainty, and requests for analysis only or to
stop. A recommendation does not grant permission to execute or save it. Do not
add follow-up work when the requested result is already sufficient.

## Quality check

Describe how the user can tell the task was done well. Check facts and references
where relevant; do not mark a check passed unless it was actually performed.

## Improve next time

Compare the result with the user's goal and any relevant pending improvement check.
Use user feedback and observed results to identify a small reusable improvement
when warranted. Follow `commands/improve.md` for persistence and follow-up checks.
An output-save policy does not authorize editing this workflow. Ordinary corrections
can fix the current result without being saved as permanent rules.

## Save policy

Propose saving results under `local/work/` when this workflow is run. Have the user
approve that policy as part of setup, or choose “show in chat; save only on request”.
The saved workflow must contain the chosen policy, not this authoring instruction.
Use a descriptive filename with the actual date and avoid overwriting existing work.

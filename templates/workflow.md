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
After a correction, repeated complaint, or missed requirement, use the
[feedback-improvement skill](../skills/improve-workflow/SKILL.md) to diagnose the
cause and proactively propose a supported, scoped repair. Keep this skill reference
in saved workflows as the root-relative path `skills/improve-workflow/SKILL.md`.
Follow `commands/improve.md` for authorized saves, checks, and undo. An output-save
policy does not authorize editing this workflow. One-time corrections can stay in
chat; do not infer a permanent preference or repeat a declined proposal.

## Save policy

Record the user's chosen scope, replacing this guidance:

- Save setup, result, and progress: save the current result and compact checkpoints
  for this active task at meaningful milestones and on pause, using one named file
  under `local/work/`. Include confirmed decisions, unresolved questions, and the
  next step. This covers routine updates during the task, not unrelated work.
- Save setup only: keep results in chat unless the user requests an output save.
- Keep everything in this chat: no personal files; a later explicit save request
  authorizes only what it specifies.

Name the actual checkpoint path and task scope when a result/progress save is
chosen. Read it before updating, preserve other content, and verify changed files.
Follow `AGENTS.md` for a plain save receipt, reopening, partial failures, and later
no-save overrides. Never save full transcripts by default or promise background
saving. Output permission does not authorize instruction or context changes.

## Second look

When a consequential decision, important plan, or weak evidence would benefit,
offer the [second-look skill](../skills/challenge/SKILL.md) once. Run it when asked,
including "Challenge this". Keep the root-relative reference
`skills/challenge/SKILL.md` in saved workflows. Skip routine or declined offers;
review does not authorize executing the plan.

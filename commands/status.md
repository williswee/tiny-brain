# tiny brain status

If demo mode is active, apply `commands/demo.md` and inspect only simulated
state. Report the demo variant and stage, label setup and results as simulated,
and never use actual `local/` files to fill gaps. Show virtual paths as code
instead of the real file links requested below.

This procedure is read-only. Re-read `AGENTS.md` after context loss. Start with
any exact file the user names, then inspect `local/profile.md`, the relevant
saved workflow, and its linked current checkpoint if present. If no checkpoint
is linked, inspect recent filenames under `local/work/` and open only the small
number of relevant files needed to explain progress. Filenames alone do not
prove completion or which result is current. Do not scan unrelated personal files.

Report briefly:

- Whether setup is absent, partial, or ready. Ready requires a profile with
  `setup_status: ready`, a nonempty purpose and first task, and its saved workflow.
- The current goal and latest verified result or checkpoint, with file links.
- Confirmed decisions, unresolved questions, and the next step recorded there.
  Say when one is missing rather than reconstructing it from assumptions.
- The saved scope and saving choice, including whether results stay in chat,
  whether this task has consent for checkpoints, or whether that choice is unknown.
- Any relevant pending improvement check in `local/improvements.md`, if present;
  distinguish a saved change from evidence that it helped.
- One useful next action and the exact instruction to resume from the verified
  checkpoint or workflow in this same folder.

Also mention any active session-only workflow agreed in this conversation. It can
be run here even without saved files; distinguish it from setup saved on disk.
A current no-save instruction overrides any saved checkpoint or improvement-log
policy. Do not write an entry just to record that override. Missing optional
preferences and Markdown links are not incomplete setup. If there is neither
saved setup nor a session draft, say so and offer "Start tiny brain". If no work
has been saved, say so. Do not invent progress, modify files, or silently resume
external actions.

A request for status does not resume work. For an explicit resume request, first
verify the checkpoint's contents and the relevant workflow, then check that its
saving consent still covers the same task and has not been overridden in the
current conversation. Reuse clear, applicable consent without a new approval for
each checkpoint. If the scope, saving choice, or latest state is missing or
conflicting, ask one targeted question before writing; useful chat-only work can
continue meanwhile. Do not claim to recover unsaved replies or infer ongoing-save
permission from the existence of a file. Do not restart a completed action or
resume a consequential external action solely because it appears as a next step.
Once state and consent are clear, follow `AGENTS.md` and the workflow for the
requested work. No status or resume instruction schedules background saving.

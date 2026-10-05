# tiny brain help

If demo mode is active, follow `commands/demo.md`. Read public command files,
but list workflows only from the simulated state. Include the demo controls.

Read `AGENTS.md`, list the actual files in `commands/` and, if present,
`local/workflows/`. Read relevant workflow headings to describe what exists.
Do not present planned blueprint features as installed capabilities.

Explain these ordinary chat phrases briefly:

- **Start tiny brain**: create or update the small setup. For a fresh start,
  choose Quick to begin with a task, Guided for an optional introduction, or
  See an example. A task already supplied skips the route choice. Both routes
  end with an editable brief and a choice to save setup/result/progress for this
  task, save setup only, or keep everything in chat.
- **tiny brain status**: read saved setup and the latest relevant checkpoint,
  show what is complete or unresolved, and give the exact file to reopen.
- **tiny brain improve** or **help me improve this workflow**: use the
  [feedback-improvement skill](../skills/improve-workflow/SKILL.md) to diagnose a
  result and propose a scoped fix. The assistant also uses it after a correction,
  repeated complaint, or missed requirement when a lasting change may help.
  Proposals need save authorization; you can decline or keep them in chat.
- **Run my first workflow**: uses the active session-only draft, if agreed in this
  conversation; otherwise uses `local/workflows/first-task.md` when it exists.

- **Challenge this** or **take a second look**: use the
  [second-look skill](../skills/challenge/SKILL.md) to test assumptions, missing
  constraints, counterarguments, and possible improvements. A second pass by the
  same assistant is labeled as such; it is not independent verification.
- **tiny brain demo** or `/demo`: choose a quick fictional walkthrough or test
  the real onboarding flow with simulated saves and actions. Use `/demo show`
  or `/demo test` to choose directly; `/demo review`, `/demo reset`, and
  `/demo exit` review, restart, or end the rehearsal.

No GitHub account is needed to use a downloaded folder. Start with a real task;
demo is an optional simulation. Context questions are optional and can be skipped.
For saved work, explain how to reopen the same folder and name the latest verified
file. Local saves need a separate backup if the user wants one.

When explaining demo usage, give a sequence, not just a list of commands:

1. Send `/demo test` to start onboarding directly. `/demo` is an optional mode
   picker; `/start` is not needed after entering test.
2. Answer the prompts in ordinary messages in the same chat. At the setup
   preview, "Save this setup" and "Run my first workflow" exercise simulated
   saving and results; session-only use is also available.
3. Send `/demo review` at any point for feedback on what happened so far.
4. Reply normally to continue that attempt, `/demo reset` to start over, or
   `/demo exit` to finish. Review before reset or exit if feedback is wanted.

Explain that each command is a separate chat message. Review is optional and
preserves progress. Sending `/demo test` again starts fresh; it does not resume.
For a demonstration, start with `/demo show`, then optionally review the
walkthrough, switch to `/demo test` for hands-on onboarding, or exit. Tailor the
explanation to the requested use; do not recite both paths on every help request.

Include additional saved workflows only if they actually exist, using their names
and paths. These are chat requests, not a promise of native slash-menu entries.
End with one relevant next step. If neither saved setup nor a session draft exists, offer setup without preventing
the user from asking an ordinary question or requesting work directly.

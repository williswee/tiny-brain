# tiny brain help

If demo mode is active, follow `commands/demo.md`. Read public command files,
but list workflows only from the simulated state. Include the demo controls.

Read `AGENTS.md`, list the actual files in `commands/` and, if present,
`local/workflows/`. Read relevant workflow headings to describe what exists.
Do not present planned blueprint features as installed capabilities.

Explain these ordinary chat phrases briefly:

- **tiny brain demo** or `/demo`: choose a quick fictional walkthrough or test
  the real onboarding flow with simulated saves and actions. Use `/demo show`
  or `/demo test` to choose directly; `/demo review`, `/demo reset`, and
  `/demo exit` review, restart, or end the rehearsal.
- **Start tiny brain**: create or update the small setup. For a fresh start,
  choose Quick to begin with a task, Guided for an optional introduction, or
  See an example. A task already supplied skips the route choice. Both routes
  end with an editable brief before saving; session-only use is available.
- **tiny brain status**: summarize saved setup and recent work.
- **tiny brain improve**: review a result and feedback, and propose a small change
  to future behavior. A proposal is saved only when authorized.
- **Run my first workflow**: uses the active session-only draft, if agreed in this
  conversation; otherwise uses `local/workflows/first-task.md` when it exists.

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

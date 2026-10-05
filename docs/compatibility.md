# Compatibility and recovery

Documentation checked on 2026-10-01. This starter relies on project instruction
files and ordinary chat messages. It does not require native command registration.

| Tool | Entry file | Official reference | Runtime verification |
| --- | --- | --- | --- |
| Codex | Root `AGENTS.md` | [Custom instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Pending |
| Claude Code | Root `CLAUDE.md` imports `@AGENTS.md` | [Project memory and imports](https://code.claude.com/docs/en/memory) | Pending |
| Cursor Agent | Root `AGENTS.md` | [Rules and AGENTS.md](https://cursor.com/docs/rules) | Pending |

## Start with a local folder

A downloaded ZIP or shared copy is enough. You do not need Git or a GitHub account.
Extract the whole starter folder, open it in your AI app, and say "Start tiny brain".
Do this before any optional demo if you want to work on a real task. The app must
be able to read files and, when you choose to save, write files in that folder.
Sign-in and any usage charges depend on the app, account, and provider. Check them
with the app; this starter supplies no account or usage allowance.

For Claude Code, relative import paths resolve from the containing file. For this
starter both files are at the root. Keep this import small and check it after moves.

Open the actual project folder and start a fresh session after changing entry
instructions. Existing sessions may retain older instructions. If automatic
loading fails, use: “Read AGENTS.md and follow commands/start.md.”

`commands/` is a portable collection of instructions, not a native slash-command
directory. `/start` and `/demo` work only if they reach the assistant as chat text.
Use "Start tiny brain" or "tiny brain demo" when the tool intercepts slash commands.
Demo controls also accept ordinary text, such as "tiny brain demo test" and
"tiny brain demo exit". Adding native wrappers is optional; their discovery, names,
and syntax need separate testing in each client.

For demo, the direct fallback is:

> Read AGENTS.md and commands/demo.md, then start demo test.

Demo reads the starter's public instructions and simulates file and external
actions in chat. It does not inspect existing `local/` data or use connected
services. It is a conversational mode, not an enforced sandbox. For a demonstration
where tool access must be technically restricted, use the host's available controls.
Demo state does not persist into a new chat. On uncertain or lost state, restart
with the fallback rather than assuming a previous practice setup survived.

The runtime verification table above includes demo behavior. Adding these
instructions does not verify them in any client. Demo test helps assess the
conversation; it does not test actual file writes, permissions, or integrations.

Onboarding uses clickable choices when the current host and mode support them.
Otherwise it shows a numbered list and accepts a number, label, or free text.
Buttons are optional; the same Quick and Guided routes work through ordinary chat.

## Save and reopen your work

First use offers three choices: save the reviewed setup with the actual result
and progress for the current task, save setup only, or keep everything in chat.
Saving progress permits meaningful checkpoints during active work and when you
ask to pause. A checkpoint contains the current result, confirmed decisions,
unresolved questions, and next step. It is not background autosave or a full
transcript. A later "don't save" instruction overrides earlier permission.

After writing, the assistant reads the saved files to verify them. Its receipt
should name the folder and saved files, then give the exact message to continue
in a fresh chat. When a result is saved, identify the latest work file. If only
the setup was saved, say that the result is still in chat. Open the same folder
before using the reopening message.
If a write or readback fails, the assistant must distinguish verified files from
anything still unsaved or unverified. A claim in chat that something was saved is
not a substitute for checking the file.

Local saving works in a plain folder without Git. Make a separate backup suitable
for the folder's contents; downloading a new starter does not recover personal work.
If you do use Git, `.gitignore` excludes new files under `local/` from ordinary
commits. It does not remove files that Git already tracks. An actual tracked
personal file needs a specific warning and a reviewed fix. A plain folder does
not need a warning about missing Git protection. File saving and Git exclusion
do not encrypt your data, and your AI tool's data-handling settings still apply.

## Portable skills and optional context

The bundled [feedback-improvement](../skills/improve-workflow/SKILL.md) and
[challenge](../skills/challenge/SKILL.md) skills are Markdown instructions routed
by `AGENTS.md`. They do not require native skill registration. Say "help me improve
this workflow" or "Challenge this" in ordinary chat. A same-assistant challenge
pass is not independent verification; the assistant should say what it actually
checked. Client behavior still needs the runtime tests listed above.

Goals, project details, preferences, and relevant people are optional context.
The assistant can invite a useful detail during work, accept a skip, and show the
proposed note before saving. Missing context files are not a setup failure. It
should ask about possibly stale or conflicting context before using it and should
not turn a one-time correction into a permanent preference.

## Recover from unrelated onboarding questions

The starter offers a task-first or guided introduction and uses only the context
the user supplies. If an older generated repo
asks about a domain the user did not choose:

1. Inspect that repo's instruction files, setup command, and saved profile. Look
   for copied sample facts, specialized context filenames, or a preset workflow.
2. Compare them with this starter. Ask the agent to show proposed corrections
   before changing existing personal context. Replacing only the guides will not
   repair instructions already generated from the old guides.
3. Start a fresh chat in the corrected folder. If unrelated behavior continues,
   check the tool's global/personal instructions and any installed plugin with a
   similarly named command. Avoid deleting unrelated settings.
4. Try "Read AGENTS.md and follow commands/start.md." Preserve a short sanitized transcript
   and the relevant file paths if reporting a failure.

The original quickstart's worked example is a plausible cause of the reported
behavior, but the friend's generated files and transcript would be needed to
establish the exact source. Local corrections do not automatically update their repo.

## Known limits

Instruction files guide model behavior; they do not enforce it. File access,
approval prompts, tool modes, and provider settings still apply. The full workflow
requires an agent that can inspect and write files. In an ordinary chat without
those tools, the agent can draft text but cannot verify saved state.

The design needs live beginner testing in each advertised client. Record the actual
client version, operating system, model, date, and result using the
[acceptance scenarios](acceptance.md); don't infer support from documentation alone.

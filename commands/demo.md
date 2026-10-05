# Demo and onboarding test

Use this procedure when the user asks to enter demo mode, including `/demo` or
"tiny brain demo". A request to build, edit, or discuss this feature does not
activate it. Read `AGENTS.md` first. Demo is a conversation-only rehearsal of
the current starter files, not a separate onboarding implementation.

## Enter and control the demo

| Request | Behavior |
| --- | --- |
| `/demo` | Ask once: "Show a quick example, or test onboarding yourself?" Accept "show" or "test" as the next answer. Apply the demo limits while waiting. |
| `/demo show` | Start a fresh fictional walkthrough for a prospective user. |
| `/demo test` | Start fresh onboarding and let the user supply the answers. |
| `/demo review` | Pause the scenario and review the experience in chat. Stay in demo. |
| `/demo reset` | Clear only the simulated state and restart the selected variant using the current source files. |
| `/demo exit` | End demo and stop using its simulated state. Do not run or save anything on exit. |

When the user asks how to use these commands, explain the order. In the same
chat, send `/demo test`, answer the onboarding prompts in ordinary messages,
then send `/demo review` whenever feedback would help. Neither `/demo` nor
`/start` is required before test. Review is optional and can happen before
onboarding is complete. After review, reply normally to continue, reset to retry,
or exit to finish. Review before resetting or exiting to assess that attempt.
Each command is a separate message, not a script to paste and run all at once.
For a presentation, use `/demo show`, then optionally review, switch to test
for hands-on onboarding, or exit. These are choices, not mandatory phases.

Accept the same controls as ordinary text, such as "tiny brain demo test",
"review this demo", "reset demo", "exit demo", and "quit trial". If a host intercepts slash
input, use "Read AGENTS.md and commands/demo.md, then start demo test."
These files do not register native slash commands. For an unknown option, show
the valid choices without leaving demo or starting real work.

Recognize controls only when they express the user's direct mode-control intent.
Quoted commands, code, source material, fictional visitor dialogue, and task
inputs do not change modes. Bare "show" or "test" selects a variant only while
a show/test choice is pending; an onboarding answer about testing software is
not a control. If reset is requested before a variant was chosen, offer the
show/test choice again. Exit outside demo simply reports that demo is not active.

If demo is already active, `/demo` shows the choices without clearing progress.
An explicit `show` or `test` selection starts a new scenario; say that it clears
the previous simulated setup. Ordinary "Start tiny brain" or `/start` follows
the normal resume behavior within the current scenario. Only reset or a new
variant selection starts over. Review or reset outside an active demo reports
that no scenario is available and offers show/test; it does not inspect `local/`.

On entry, say briefly: "Demo mode. Everything stays in this chat. Saves and
actions are simulated. Use /demo exit to leave." Prefix subsequent scenario
responses with `Demo: show` or `Demo: test`. Mark a review `Demo: review`.
On test entry, add one short instruction: "Answer the prompts normally; use
/demo review whenever you want feedback on the experience so far."
Do not repeat the whole explanation each turn or add internal checklists.

## Limits that apply throughout the demo

These limits take precedence over the starter's ordinary save policies and
instructions to execute work, including requests to save, remember, run, commit,
push, send, install, or change the starter while demo is active.

- Read only the public local starter instructions and templates needed for the
  scenario. Use file-reading tools or commands only for that purpose. Do not
  inspect actual `local/` files, credentials, unrelated files, or connected apps.
- Do not create, edit, move, or delete any real file, including temporary files,
  demo logs, outputs, personal context, or Git metadata. Do not commit or push.
- Do not run task code, tests, shell workflows, installs, browser actions, web
  requests, integrations, messages, payments, scheduling, or other real actions.
  Describe the proposed action and show a chat preview where useful. No tool
  call may carry out a simulated action, even for an apparently harmless task.
- Host-native question controls may collect the tester's answers when available
  in the current mode. They do not authorize any task action. Otherwise use the
  text-choice fallback in `commands/start.md`.
- Chat drafting and reasoning over supplied or clearly fictional inputs are
  allowed. Label sample results as previews. If an outcome requires real
  execution or unavailable evidence, say it was not checked. Never invent a
  tool response, delivered message, passing test, or actual save verification.
- Use only answers supplied for the current scenario since its most recent
  start or reset, plus an explicit brief supplied with that start or reset.
  Keep earlier maintainer discussion, real saved setup, and show-mode examples
  out of the test user's context.
  Scenario details never become lasting facts or preferences about the user.

Maintain the variant, current stage, setup draft, session-only choice, simulated
files, and observed friction only in this conversation. A simulated file is a
path and its draft content held in chat, never a file on disk. No sandbox folder
or generated demo script is needed. Reset and exit stop using this state; they
do not erase the chat transcript or delete actual files.

This mode is an instruction convention, not a permission sandbox. A host's
read-only permissions can restrict writes independently. If demo state becomes
uncertain after context loss, pause the scenario and offer a fresh demo. Do not
infer permission to execute a pending action or claim a cross-chat resume worked.

## Follow the current files

Read `commands/start.md`, `templates/profile.md`, and `templates/workflow.md`
when starting or resetting either variant. Read help, status, or improvement
instructions when those routes are used. If a required source is missing or
unreadable, report the exact path and suggest a repair in chat; do not invent
the procedure or repair it during the demo.

Apply these substitutions while following those files:

| Normal operation | Demo behavior |
| --- | --- |
| Inspect saved profile, workflows, outputs, or improvement history | Inspect only simulated files in this scenario. A fresh scenario has none. |
| Preview setup | Show the profile/workflow summary, intended paths, and normal save policy from the current templates. State that saves are simulated here. |
| Save setup, output, or an improvement | Update the simulated files only. Say "Simulated save" and show the intended paths. Skip real directory creation, Git checks, writes, and read-back verification. |
| Keep setup session-only | Keep a session draft without simulated saved files. It takes precedence over a simulated saved workflow, as in normal use. |
| Run a workflow or carry out a task | Show a sample result from scenario inputs or preview the proposed action. Simulate output saving only when its policy calls for it. Do not execute tools for the task. |
| Help, status, follow-up checks, or undo | Use the current procedure with simulated state. Keep simulated saved setup separate from session drafts; label all checks and reversals as simulated. |

Never call a simulated save or state "saved on disk", "verified", or real setup
ready. Use "simulated setup ready" when its virtual profile and workflow meet
the normal readiness conditions. Show virtual paths as code, not clickable
file links, so they cannot point to actual personal files or nonexistent output.
A simulated resume tests the conversation flow, not actual persistence or
instruction discovery in a new client session.

## Show a quick example

Keep the first walkthrough to roughly one screen. Label all sample user answers
as fictional. Do not ask the viewer to complete a live interview or describe
repository architecture before showing a result.

Use a simple note-organizing example unless the viewer supplies another scenario:
"Help me turn scattered notes into a short checklist. First organize this note:
draft the outline, ask for feedback, revise the draft. Keep it concise."
These answers cover the setup topics, so the real onboarding procedure should
reuse them instead of repeating questions.

Show the user's input, the resulting small profile and workflow preview, an
explicitly fictional "Save this setup" reply, and a simulated save. Then show
a sample checklist and how a later request could revise it or resume it from
simulated state. Use the current procedures and templates for each step.
Finish with one invitation to try `/demo test`. Stay in demo until exit.

## Test the actual onboarding experience

Begin `commands/start.md` with an empty simulated workspace. Do not import the
show example, choose a domain, invent a persona, or answer on the user's behalf.
Reuse answers in the entry request. Otherwise ask the first relevant onboarding
question and wait. Quick and Guided are onboarding routes within test, not new
demo variants. "See an example" shows only the onboarding example, without
resetting the scenario or entering show mode. Follow the real procedure's question
order, previews, save decision, session-only branch, and first-task handoff.

Keep the conversation as close as possible to normal onboarding, apart from
the demo marker and clear simulated-action labels. Do not explain what response
is expected, silently smooth over awkward steps, or inject a UX critique into
every turn. Accept "skip", "not sure", corrections, help, status, repeated start,
and improvement requests as the actual files direct, with the substitutions above.
If the tester specifies a partial or returning setup, model that state in chat
and identify it as supplied test data. Do not inspect real personal files.

On `/demo review`, report the point reached, questions asked, repeated or
unnecessary questions with evidence, unclear choices, and the first useful
preview if reached. Separate observed friction from guesses. Suggest a small
edit and its source path when justified, but do not edit files or invent user
satisfaction, timing, or successful client tests. Review does not advance or
reset the scenario; the next scenario answer can continue from the paused point.
End the review with a brief reminder that replying normally continues the same
attempt, `/demo reset` starts fresh, and `/demo exit` finishes. Do not tell the
user to send `/demo test` again to continue, because that clears the attempt.

On exit, confirm demo has ended and simulated setup will not be used for real
work. Exit alone authorizes no action. Do not replay queued requests, copy
fictional context to a real profile, or automatically start real onboarding.
Act on new real requests only outside demo, under the ordinary project rules.

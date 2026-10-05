# Start tiny brain

Set up a small workspace from this user's answers. This file is the authoritative
onboarding procedure. Read `AGENTS.md` first if it is not already in context.

If demo mode is active, apply `commands/demo.md` before every step below. Use
only its simulated state for personal files; all saves and first-task actions
remain chat previews. Keep the same onboarding questions and decisions.

## 1. Check what exists

First reuse any setup draft already agreed in this conversation, including a
session-only setup. Inspect `local/profile.md` and `local/workflows/first-task.md`
if present. Do not scan unrelated personal files or read examples, the blueprint, or review notes to
choose a domain. Do not search the web for the user or pre-fill their identity.

If a saved setup exists, summarize its purpose in one sentence. Ask whether the
user wants to continue it or change it, unless their request already says which.
Keep existing files and completed answers. If only part of setup was saved, read
what exists and offer to repair the missing component. If repair was already
requested, proceed with it. Never reset or overwrite existing work silently.

## 2. Learn the minimum

Use answers already provided in the active conversation. Ask only unanswered
topics, one topic per turn. Acknowledge relevant details briefly instead of
repeating the whole brief after every answer. Accept free text, "skip", and
"not sure" throughout. Never require a name or job to proceed.

### Choose how to begin

For fresh setup with no task or route already supplied, ask the route question
in the first reply after checking the starter files. If copying or creating files
was requested, complete and verify that first, then ask in the same reply that
reports completion. Do not stop at a file inventory or "the route selector is
ready", or wait for another start message.

Use this opening, or equivalent wording with all three choices, a short explanation
of each, and an explicit reply instruction:

> How would you like to start?
>
> 1. **Quick: give me a task.** Start with something you have or one thing that's stuck.
> 2. **Guided: get to know me.** Start with an optional introduction, then choose a task and preferences.
> 3. **See an example.** See a fictional setup and sample result before choosing.
>
> Reply with 1, 2, or 3, a label, or your own words.
>
> I'll ask one topic at a time and show you a short setup brief to review before saving. You can also keep it in this chat.

Wait for the route answer before asking about the task, introduction, or preferences.
For **See an example**, show a short fictional input, setup brief, and sample result
in chat. Ask for the user's own task or offer guided setup afterward. Do not
adopt the example as their profile, save it, or change the active demo mode.
If requested midway through setup, keep the draft and resume its next missing
topic afterward.

Use a native clickable question control when the host supports it in the current
mode and choices would help. Always allow a typed answer. Otherwise show a short
numbered list and accept its number, label, or free text. Present each question
once; do not repeat the same prompt in a separate message after a question control.
No widget is required to continue, and text labels alone are not clickable buttons.

If the setup request already supplies a task, use Quick without asking for a route,
unless the user explicitly requests Guided. An existing draft resumes at the next
unanswered topic without this menu. Switching routes preserves completed answers.
If the user skips the route choice or is unsure, continue with Quick and ask for
the first task. Skipping the route does not also skip choosing a task.
An ordinary task outside setup still follows `AGENTS.md` without an interview.

### Quick and Guided

Quick starts with the small-task step below. Guided adds an optional introduction
first: "What should I call you, and what do you do? Your name is optional."
Accept any introduction, including a role, project, or what keeps them busy.
Do not look up their identity or ask again for skipped details. Both routes use
the same small-task step and editable preview; skip anything already answered.

Use plain topic labels such as "About you", "First small task", or "Your setup"
only when helpful. Do not use fixed positions such as "2 of 3" or promise a
message count or completion time. A useful answer may move straight to a result
or the preview.

### Find one small task

Use this step for Quick and after the optional Guided introduction. Reuse any
concrete task already supplied and skip this picker. If the user has only named
a broad area, such as "marketing", offer two or three small starting points tied
to that area, plus their own answer. Do not infer a job or goal from the area.
Otherwise ask this one question, using native choices when available:

> Let's start with something small. What do you have right now?
>
> 1. A note, draft, or message to work on.
> 2. A decision or small task that's stuck.
> 3. Not sure. Show me an example.
>
> Choose a number, paste something, or reply with a few words.

Accept fragments, rough pasted material, free text, "skip", and "not sure".
Do not ask the user to write a full brief or rank their life or work priorities.
The choices are ways to find a task, not additional setup routes. Keep an existing
draft and any completed answers when the user tries a different starting point.

Follow the next useful clue, one short question or input request per turn:

- For an item such as "messy notes", invite a small piece: "Paste a few lines.
  Rough notes are fine." Do not require the whole document or ask for it again.
  If nothing exists yet, accept a few words about it instead.
- For something stuck, ask for the immediate situation, such as "What's the next
  thing you need to do? A few words are enough." If the situation is already
  given, use it instead of asking again.
- If the intended result is still unclear, offer two or three concrete outcomes
  for that item, such as "Would a short summary or an action list help more? You
  can suggest something else." Skip this when the requested result is clear.

Gather the outcome, relevant context, and constraints progressively. Ask only
for a missing detail that would materially change the next useful result. For
example, ask who will read a message if that changes the wording; do not demand
an audience, deadline, tool list, budget, or success metric for every task.
These are conditional follow-ups, not a checklist to ask in order. Stop asking
once a small useful response is possible. Unknown optional details stay unknown.

When the user has asked for a task and supplied enough input, briefly state the
concrete task you understood and give a small first pass in chat. Do not block it
on a preferences interview or saving setup. A stated, reversible suggestion may
guide that first pass; do not record it as a confirmed user preference or commitment.
This does not authorize file writes, tool use, or external actions beyond the
request. Demo still permits only simulated results under `commands/demo.md`.

If the task is clear but its input is not available, preview the workflow without
requiring an upload now. Ask for the needed input when the user wants to run it.
Do not force a sample result or delay a ready setup with more scoping questions.

### Preferences and uncertain answers

Ask about a limit or preference only when it changes the current task and is not
already known. Prefer a specific question over a list of every possible constraint.
Otherwise leave optional preferences for the editable preview. Skipped preferences
count as answered. Label concise, friendly responses as defaults when no style
was supplied; no additional boundaries were specified, not confirmed absent.
Selecting a response style implies nothing about budget, deadlines, or tools.

If the user chooses "Not sure. Show me an example", says "not sure" about a task,
skips choosing a task, or asks the assistant to choose, show a small fictional
note-organizing example under "Explore how this workspace works". Include the
rough input and a useful result in chat. Do not ask another broad task question
or require preferences before showing it. Keep fictional facts out of the profile
and preserve any real draft. Viewing a sample does not choose a real task or
authorize a saved workflow. The user can stop there or bring their own material;
resume setup only when they want to continue. Do not repeat declined questions.

Capture context accurately: a request for marketing help is not a claim that the
user is a marketer. Keep supplied names, roles, projects, offers, audiences, and
constraints distinct; leave unknown details unknown. Do not infer website content
from a URL or treat one as a request to research the user. Preserve multiple goals
or tasks when supplied. Propose a sensible first task in the editable brief unless
the order needs a user decision. Do not demand metrics, dates, budgets, a location,
or personal history just to complete fields. Current corrections replace earlier
answers in the draft, including related workflow details.

## 3. Preview one small setup

Read `templates/profile.md` and `templates/workflow.md`. Draft:

- `local/profile.md`: the user's goal and success criteria when known, first task,
  relevant background, stated constraints, preferences, and boundaries.
- `local/workflows/first-task.md`: one workflow tailored to that task, with inputs,
  a few steps, an output, a quality check, and an explicit local save policy.

Both routes end with the same short, editable brief: confirmed context, the first
task and intended result, preferences and limits, and the proposed workflow.
Reflect the task in one concrete sentence, such as "Turn rough meeting notes into
an action list, leaving missing owners and dates unknown." Use only the user's
chosen task; mark any suggested output or method as proposed. Invite corrections
in this preview before saving. Use the existing save or chat-only decision to
confirm the brief; do not add a separate task-confirmation gate. Keep
unknowns and suggested defaults distinct from confirmed facts. Omit personal
details the user asks to leave out. Show intended paths without dumping blank
template headings or asking the user to choose filenames.

### Choose what to keep

Make the first-use saving choice explicit in the same brief. Show the proposed
setup paths, the task covered by saving, and the proposed current checkpoint under
`local/work/`. A checkpoint keeps the current result, confirmed decisions,
unresolved questions, and the next step. Show which of those items exist now;
do not invent missing decisions or questions. Say that future checkpoints would
update this task's file at meaningful milestones or when the user asks to pause,
only while the assistant is actively working on the task. They do not run in the
background. Full conversation transcripts are not saved by default.

If no saving choice already covers this scope, ask:

> What would you like to keep?
>
> 1. **Save setup, result, and progress.** Keep the setup, the actual result, and a short checkpoint as we work on this task or when you ask to pause.
> 2. **Save setup only.** Keep the setup; show results in chat unless you ask to save one.
> 3. **Keep everything in this chat.** Use the setup here without saving personal files.
>
> Reply with 1, 2, or 3, or tell me what to change in the brief.

This choice approves only the previewed scope. Reuse an explicit choice already
given instead of asking again. "Save setup" alone means setup only; a request to
save one result does not authorize ongoing checkpoints. Record the selected
policy and task scope in the workflow, with the current checkpoint path when
applicable. Do not require approval for each routine checkpoint within that scope.
New tasks, new kinds of retained information, or a wider save scope need their
own authorization. Saving progress does not authorize unrelated context changes,
external actions, or saving sensitive source material.

"No saving" selects session-only use with output in chat. Honor it without asking
again or proposing automatic output saving. A later no-save instruction overrides
any earlier ongoing-save policy and pending improvement-history updates. It does
not delete existing files. If saving is requested before a usable draft exists,
collect only what is needed to form it and show the preview first. Do not create
a partial setup just because the user requested a save early. In demo, the same
rule applies to simulated files. Corrections revise the draft; they do not approve
unrelated facts.

### Add useful context gradually

Do not require a project name, architecture, persona, mandatory context files,
custom gates, plugins, a skill library, a GitHub account, or an API connection to
get started. Keep initial context in the profile. When a goal, project detail,
working preference, or detail about a collaborator would materially help the
task, invite that one topic in plain language. Reuse what the user already said
and accept "skip" without another prompt or an empty file. Ask for only the
minimum useful information about other people; avoid private details unrelated
to the work. Do not infer traits or general preferences from one task.

Offer a separate context file only when the detail has become useful to reuse or
the user requests it. Use the optional map in `README.md` for paths. Propose the
actual content and its purpose, then get consent before persisting it unless
that exact change is already authorized. Move approved detail out of the profile
and link to its one authoritative copy. Do not burden the user with filenames,
use README illustrations as user facts, or create empty files to complete the map.
When relevant saved context may be stale, ask about the specific fact before
relying on it; a correction does not authorize saving other facts.

## 4. Save and verify, or continue without saving

On authorization, ensure `/local/` is covered by the root `.gitignore`. If Git is
available and this folder is inside a Git checkout, verify the intended paths are
ignored. If they are already tracked, explain that ignoring does not untrack them
and resolve sharing intent before saving private data. Do not alter Git history
or untrack files without direction. If Git is unavailable or this is a plain
folder such as an extracted ZIP, proceed locally without initializing Git. A
plain folder needs no GitHub account. Do not warn that it lacks "Git protection";
Git ignore rules do not provide encryption or a backup.

Create only needed directories and save the authorized setup files. Mark the
profile's `setup_status` as `ready` only when its `purpose` and `first_task` are
nonempty and the companion workflow is saved. Unknown optional fields are
acceptable. With setup-and-progress consent, save an actual result already shown
in chat into the agreed checkpoint during this same turn. Do not leave the first
result only in chat after saving its setup. If no result exists yet, save the
setup and say that the checkpoint will be created when the task produces one;
do not create an empty checkpoint or claim work was completed.

Keep one current checkpoint per active task under `local/work/`, using a readable
filename with the actual date and task name. Inspect an existing file before
updating it. Update only this task's current result, confirmed decisions,
unresolved questions, next step, and saved scope; preserve unrelated work.
Keep a link to the checkpoint in the workflow so a later session can find it.
Do not create a new dated copy at every milestone or overwrite another task's
output. Use the shared checkpoint rules in `AGENTS.md` during later work.

Read back every written file, including the saved result and checkpoint link.
Report success only for verified files. If a write or verification fails, name
what was saved, what is missing or unverified, and the next repair needed. A
saved setup with an unsaved result is partial progress, not a complete save.
Preserve that state for repair without rerunning successful writes blindly.

Give a short receipt with the actual saved location, a link to the latest result
or checkpoint when one exists, and an exact reopening instruction. For example,
use "Open this same folder in your AI app and say: Resume from <actual checkpoint
path>." Replace the placeholder with the verified path. If only setup was saved,
point to the workflow and say that the result remains in chat. Explain once that
these are files in this folder and that any backup depends on the user's own
folder backup or sync; do not imply a cloud copy was created or claim to know its
backup status. Keep Git terminology out of the ordinary receipt unless a real
tracked-private-file issue needs attention.

For session-only use, keep the draft in the conversation and do not create personal
files. Override any proposed automatic save policy with "show in chat; save only
on explicit request". "Run my first workflow" runs this in-conversation draft,
even if there is no saved file. Explain once that the user will need to supply
this draft or chat context again in another session. A pasted prompt alone does
not restore unsaved work.
If file tools are unavailable, show the draft and explain that saving requires
opening this folder in a file-capable tool; do not pretend it was saved.

## 5. Reach the first useful result

Briefly summarize what was saved, or configured for this session, and how to
change it. If an early chat result already completed the task, refer to that
result and offer to revise it or use the workflow with new input. Do not rerun
completed work merely because setup has finished.
Otherwise, if the user has requested the first task and supplied its inputs,
do it now using the workflow. If inputs are missing, offer "Run my first workflow"
with only the input it actually needs. The first success is useful work, not
finishing a file inventory.

Do not restart setup when `/start` is repeated. Do not silently create a second
profile or replace a personalized workflow. Do not install integrations or send
onboarding events anywhere.

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
> 1. **Quick: give me a task.** Tell me what you'd like help with, then add any preferences.
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

### Quick

Explain the length once: "We'll cover your task and preferences, then review a
short brief. You can skip any question." Use `1 of 2: Your first task` and
`2 of 2: Preferences` only when asking about those topics. Skip completed topics.

Ask: "What's one useful thing you'd like help with first?" Reuse any task already
given. Extract the purpose, desired result, and relevant background from the
answer. A clear first task is enough; do not add a separate goal question merely
to fill the profile. If a useful setup preview needs clarification, ask the one
missing detail that matters most. Leave execution inputs for when the task runs
unless they change the workflow itself.

### Guided

Explain the length once: "We'll cover you, your first task, and your preferences,
then review a short brief. You can skip any question." Use these topic labels:

1. **1 of 3: About you.** "What should I call you, and what do you do? Your name is
   optional." Accept any introduction, including a role, project, or what keeps
   them busy. Do not look up their identity or ask again for skipped details.
2. **2 of 3: Your first task.** "What would you most like help with first?" Relate
   the question to the introduction when useful. Offer a few concrete tasks based
   on their answers, plus room to describe something else. Apply the same rules
   for capturing purpose and asking only needed follow-ups as Quick.
3. **3 of 3: Preferences.** Ask only about limits or preferences not already given.

These are topic counts, not a promise of exactly two or three messages or a timed
estimate. If an answer covers later topics, skip those questions and advance to
the next missing topic or preview. Do not display stages the user already finished.

### Preferences and uncertain answers

On either route, ask: "Any limits or preferences I should work around, such as
time, tools, things to avoid, or how you like answers? You can skip this."
Where choices help, offer a few relevant examples and a skip option, while keeping
free text available. Selecting a response style does not imply anything about
budget, deadlines, tools, or other limits.

If the task is unclear, offer small choices such as organizing a note, planning
a task, or reviewing a draft. If asked to choose or if the user skips choosing a
task, preview a small fictional note-organizing example under "Explore how this
workspace works". Keep its sample facts out of the profile. Do not loop through
the route picker or keep asking for an identity or task they declined to provide.
After that sample, cover preferences only if still unanswered, then preview the
setup. A skipped preference counts as answered.
Skipped preferences default to concise, friendly responses with no additional
boundaries specified by the user. Label those as defaults in the preview.

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
task and intended result, preferences and limits, and the proposed workflow. Keep
unknowns and suggested defaults distinct from confirmed facts. Show both intended
paths without dumping blank template headings. State that running this workflow
will save output under `local/work/` if that is the proposed policy. Offer
session-only use too. Omit personal details the user asks to leave out.
Ask "Save this setup?" only if the user has not already chosen saving or
session-only use. "No saving" selects session-only use with output in chat;
honor it without asking again or proposing automatic output saving.
If saving is requested before a usable draft exists, collect only what is needed
to form it and show the preview first. Do not create a partial setup just because
the user requested a save early. In demo, the same rule applies to simulated files.
Corrections are instructions to revise the draft, not approval of unrelated facts.

Do not require a project name, architecture, persona, mandatory context files,
custom gates, plugins, a skill library, or an API connection to get started.
Keep initial context in the profile. If the user asks for separate context files,
use the optional map in `README.md`: `local/context/goals.md`, `project.md`,
`constraints.md`, `preferences.md`, and `people.md`. Create only requested topics,
move their detail out of the profile, and link to them there. Do not use README
illustrations as user facts or create empty files merely to complete the map.

## 4. Save and verify, or continue without saving

On authorization, ensure `/local/` is covered by the root `.gitignore`. If Git is
available and this folder is inside a Git checkout, verify the intended paths are
ignored; if they are already tracked,
explain that ignoring does not untrack them and resolve sharing intent before
saving private data. Do not alter Git history or untrack files without direction.
If Git is unavailable or this is a plain folder such as an extracted ZIP, proceed
locally without initializing Git. Explain once that ignore rules are prepared for
future Git use but the current folder has no verified Git protection.

Create `local/work/` and the other needed directories, then save the two files. Mark the profile's
`setup_status` as `ready` only when its `purpose` and `first_task` are nonempty and
the companion workflow is saved. Unknown optional fields are acceptable. Read
back both files. If a write fails, report the partial state and resume from it on
the next attempt. Never announce setup complete based solely on a drafted response.

For session-only use, keep the draft in the conversation and do not create personal
files. Override any proposed automatic save policy with “show in chat; save only
on explicit request”. “Run my first workflow” runs this in-conversation draft,
even if there is no saved file. Explain once that it will need to be supplied again
in another session.
If file tools are unavailable, show the draft and explain that saving requires
opening this folder in a file-capable tool; do not pretend it was saved.

## 5. Reach the first useful result

Briefly summarize what was saved, or configured for this session, and how to change it. If the user has already
requested the first task and supplied its inputs, do it now using the workflow.
Otherwise offer one next action: “Run my first workflow”, with only the input it
actually needs. The first success is useful work, not finishing a file inventory.

Do not restart setup when `/start` is repeated. Do not silently create a second
profile or replace a personalized workflow. Do not install integrations or send
onboarding events anywhere.

# tiny brain quickstart

Give your AI assistant a little context, teach it one useful task, and keep the
result for next time. You can grow the system as you learn what helps.

You do not need to fill out a worksheet or understand agents, skills, or plugins.
Start with something you actually want done.

## 1. Open your copy

You need an AI tool that can read and write files in a folder, such as Codex,
Claude Code, or Cursor. Install and sign in to your chosen tool first. Sign-in
requirements and any usage charges depend on the app, your account, and provider;
check those with the app. You do not need Git or a GitHub account to use the starter.

Get the whole folder from the [tiny brain repository](https://github.com/williswee/tiny-brain)
using **Code > Download ZIP**, or use a copy someone shared with you. Extract the
ZIP first. Keep the whole starter folder together, including `AGENTS.md`,
`commands/`, `skills/`, and `templates/`.

- **Codex:** open or add this folder as a local project and start a chat in it.
- **Claude Code:** start a session in this folder using your usual Claude Code
  interface. If you already use its CLI, run `claude` from this folder.
- **Cursor:** open this folder and use its Agent chat.

Use a mode that can edit files when you want setup saved. You can preview setup in
a read-only mode; the assistant should say when it cannot save.

Already have a project? Try this starter in its own folder first. Ask the assistant
to help merge it into your existing project later, preserving your current rules.
Do not replace an existing `AGENTS.md` or `CLAUDE.md` blindly.

Only received these two guides? Put them in a new folder, open it in your AI tool,
and say:

> Read tiny-brain-blueprint.md and create its minimal starter in this folder, preserving existing work. After verifying the files, start onboarding in the same reply: ask how I'd like to start, explain Quick, Guided, and See an example, and tell me how to reply. If I've already supplied a task or route or have a setup to resume, ask only the next unanswered question. Ask one topic at a time and show the proposed personal setup before saving it.

The full starter is the easier route; the two-guide route asks the assistant to
build the small set of files first.

## 2. Say one sentence

> Start tiny brain

For a fresh setup with no task or route supplied, the assistant's first reply asks
how you'd like to start and shows these choices:

1. **Quick: give me a task.** Start with a note, draft, or something that's stuck.
   The assistant uses a task you've already supplied without asking you to choose again.
2. **Guided: get to know me.** Start with "What should I call you, and what do you
   do?" Your name is optional. Then choose a first task and add any preferences.
3. **See an example.** See a short fictional setup and result before trying your own.

After the optional Guided introduction, both routes help you find one small task:

> Let's start with something small. What do you have right now?
>
> 1. A note, draft, or message to work on.
> 2. A decision or small task that's stuck.
> 3. Not sure. Show me an example.
>
> Choose a number, paste something, or reply with a few words.

A fragment or a rough paste is enough to begin. The assistant asks only for a
missing detail that changes the result, one short question at a time. A clear
task skips these questions. When you've asked for work and supplied enough input,
it can give a small first pass in chat before you decide whether to save a setup.
There is no fixed question count, and optional preferences can wait for the brief.

Click a choice if your tool offers buttons, or type its number, label, or your own
answer. "I'm not sure yet" and "skip" are valid answers. The assistant can help
you choose a small task. No name, job, country, or detailed profile is required.

## 3. Review the small setup

The assistant reflects your chosen task and intended result in one sentence,
then shows the context, preferences, and first workflow it proposes to save.
Proposed methods and defaults stay separate from facts you've confirmed.
A **workflow** is simply a short recipe for repeating a task.

Correct anything that is wrong, then choose how much to keep:

| Choice | What it saves |
| --- | --- |
| Save setup, result, and progress | The reviewed setup, your actual task result, and useful checkpoints for this active task. |
| Save setup only | The reviewed profile and first workflow. Results stay in chat unless you later ask to save them. |
| Keep everything in this chat | No personal files. You can still use the assistant for the real task. |

Saving setup creates `local/profile.md` with the context you approved and
`local/workflows/first-task.md` with the steps for repeating the task. The first
choice also saves the current result and meaningful progress under `local/work/`.
A checkpoint keeps the current result, confirmed decisions, unresolved questions,
and next step. The assistant can make these checkpoints during this active task
and when you ask to pause, within that one choice. It does not save in the background
or keep a full transcript by default.

You can say "don't save this" later; that overrides the earlier choice. If you
already clearly authorized saving, the assistant does not ask again.

The first setup keeps context in one profile. When a goal, project detail,
preference, or relevant person's role would help, the assistant offers to add it.
Reply in your own words or skip. You do not need to choose filenames or fill in
all the topics. It shows the proposed note and asks before saving unless you
already requested that edit. Detailed topics can move to separate files later.
People notes should contain only what the task needs, and a correction to one
answer should not become an assumed permanent preference. The assistant checks
possibly stale or conflicting saved context before relying on it.

Personal files stay in the starter's `local/` folder. Your AI tool's data-handling
settings still apply. Keep passwords and keys out. If you use Git, the starter's
ignore rule keeps new personal files out of ordinary commits; already tracked
files need separate attention. You can use a downloaded folder without Git.

## 4. Get one useful result

> Run my first workflow

Supply the task's input if needed: a note, a draft, a question, or a description.
If you already supplied everything and asked it to do the task, it can start
immediately. No extra approval is needed between ordinary workflow steps.

Check whether the result helped. Ask for a correction if it missed the point.
If you chose to save the result, the assistant reads it back to check the write.
It tells you which folder holds it, names the latest saved work file, and gives an
exact reopening message using that file's actual path. Open the file to see the
result for yourself. If a save only partly succeeds, it reports which files were
saved and which details remain in chat.

To pause, say "Pause here". If you chose to save progress, the assistant updates
the current task's checkpoint and gives you the reopening message. In a new chat,
open the same folder and paste that message. The saved decisions, open questions,
and next step let it continue; unsaved chat details may be missing.

Local saving does not create a backup. Keep a separate copy of this folder somewhere
appropriate for its contents. A fresh download of the starter will not contain your work.

Here are three possible starting requests. These are illustrations, not defaults
or facts about you; choose your own task:

- "Help me turn my reading notes into a short study plan."
- "Review my draft and explain the most useful changes."
- "Help me plan the next small improvement to my app."

## Use it again

| What you want | What to say |
| --- | --- |
| See what is saved and what to do next | "tiny brain status" |
| See available workflows | "tiny brain help" |
| Repeat the first task | "Run my first workflow" |
| Check a plan or decision from another angle | "Challenge this" or "Take a second look" |
| Review what could work better next time | "tiny brain improve" and describe the result or feedback |
| Change your setup | "Update my profile: I prefer shorter answers. Save that change." |
| Save a specific workflow improvement | "Update this workflow to check the deadline before planning." |
| Undo a saved improvement | "Undo the improvement that added the deadline check." |
| Repeat a new kind of task | "Turn what we just did into a reusable workflow." |
| Continue a specific piece of work | "Continue the work in [give the actual file path]." |
| Stop keeping a preference | "Remove this preference from my saved profile: …" |

Ordinary questions still work. You do not have to use a workflow every time.

The [challenge skill](skills/challenge/SKILL.md) checks assumptions, missing
constraints, the strongest counterargument, and a concrete improvement. The
assistant may offer a second look for a consequential decision, important plan,
or weak evidence when useful. It should not offer it for every small answer or
repeat an offer you declined. A same-assistant second pass is not independent
verification; it should name any separate review or source check it actually used.
A review does not authorize acting on the recommendation.

After a correction, repeated complaint, or missed requirement, the assistant uses
the [feedback-improvement skill](skills/improve-workflow/SKILL.md) to check whether
a lasting change would help and offer one when supported. You can also say "help
me improve this workflow". "Make this shorter" fixes the current answer; "remember
this preference" asks it to save that change. Other lasting changes need your
approval. You can decline or keep them in chat. Saved improvements have a minimal
history in `local/improvements.md` and a check on a later relevant task.
This improves the workspace's instructions and workflows, not the AI model itself.

## Optional: try a simulated demo

With the starter folder open, say "tiny brain demo" or type `/demo` to choose:

- `/demo show` gives a short fictional walkthrough of setup, a sample task, and
  returning to the work. Use it to explain tiny brain to someone new.
- `/demo test` starts fresh onboarding for you to try. Answer as a new user, skip
  optional details, or correct the draft to test how the conversation responds.

The assistant follows the current starter files and labels demo replies. All
practice setup stays in chat, even if you say "save", "remember", or "run".
It does not read your existing personal setup, change files, run code or external
actions, browse the web, call connected services, commit, or push.

To test onboarding, send these as separate messages in the same chat:

1. `/demo test` starts the interview. You do not need `/demo` or `/start` first.
2. Answer each question normally. When offered a setup, try "Save this setup"
   and then "Run my first workflow", or choose session-only use. Actions stay simulated.
3. `/demo review` pauses for feedback on the experience so far. You can use it
   halfway through; finishing onboarding first is not required.
4. Reply normally to continue, use `/demo reset` for a fresh attempt, or
   `/demo exit` to finish. Review before reset or exit if you want feedback on
   that attempt. Sending `/demo test` again also starts over.

For a presentation, start with `/demo show`. Then optionally review it, switch
to `/demo test` so the viewer can try it, or exit. Review is optional and keeps
the current demo open; the commands are not a mandatory sequence.

"tiny brain demo test" also works as ordinary text. If needed, paste:

> Read AGENTS.md and commands/demo.md, then start demo test.

Demo is an instruction for the conversation, not a permission sandbox. Normal
session-only use can do real tasks without saving a profile; demo simulates file
and external actions. Leaving demo does not save the practice setup or start real
work. Say "Start tiny brain" when you want real setup.

## If something feels wrong

| Symptom | Try this |
| --- | --- |
| It does not know how to start | "Read AGENTS.md and follow commands/start.md." Check you opened the correct folder. |
| `/start` is unrecognized or opens a tool menu | Say "Start tiny brain" as ordinary text. This starter does not install native slash commands. |
| `/demo` is unrecognized or opens a tool menu | Say "tiny brain demo" or use the direct file-reading prompt above. |
| Demo uses an old practice profile | Say "tiny brain demo reset" to begin the same mode fresh. A demo lasts only in its current conversation. |
| It assumes an industry or location you never supplied | "That is not my context. Follow commands/start.md using only what I've told you." Check the saved profile for mistaken facts. |
| It asks the same questions again | Point it to `local/profile.md`; ask it to continue or update your existing setup. |
| It insists on setup before answering a simple question | Ask it to re-read the five working rules in `AGENTS.md`. Setup is optional for ordinary tasks. |
| It cannot save files | Check the selected folder and the tool's file permissions. Review in chat until file editing is available. |
| It says files exist but you cannot find them | Ask for the actual paths and for it to read the files back. |
| It forgets during a long chat | Open a fresh chat in the same folder and paste the last verified reopening message, or say "tiny brain status". Unsaved chat details may not carry over. |

Still getting unrelated questions? Ask the assistant to inspect your saved setup
and onboarding instructions for copied example facts, then start a fresh chat.
If needed, check global/personal instructions and similarly named plugins too.
The full starter includes more recovery notes in `docs/compatibility.md`.

You can stop here. The [blueprint](tiny-brain-blueprint.md) explains optional additions
when a recurring need makes them worthwhile.

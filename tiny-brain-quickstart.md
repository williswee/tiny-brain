# tiny brain quickstart

Give your AI assistant a little context, teach it one useful task, and keep the
result for next time. You can grow the system as you learn what helps.

You do not need to fill out a worksheet or understand agents, skills, or plugins.
Start with something you actually want done.

## 1. Open your copy

You need an AI tool that can read and write files in a folder, such as Codex,
Claude Code, or Cursor. Install and sign in to your chosen tool first; its normal
account and usage requirements apply. Git is optional for local use.

Get the whole folder from the [tiny brain repository](https://github.com/williswee/tiny-brain)
using **Code → Download ZIP**, or use a copy someone shared with you. Extract the
ZIP first. Keep `AGENTS.md`, `commands/`, and `templates/` together.

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

## Try a demo first

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
and external actions. After leaving demo, continue below when you want real setup.

## 2. Say one sentence

> Start tiny brain

For a fresh setup with no task or route supplied, the assistant's first reply asks
how you'd like to start and shows these choices:

1. **Quick: give me a task.** Describe one useful thing you want done, then add any
   preferences. The assistant moves straight to this route if you already gave a task.
2. **Guided: get to know me.** Start with "What should I call you, and what do you
   do?" Your name is optional. Then choose a first task and add any preferences.
3. **See an example.** See a short fictional setup and result before trying your own.

Quick covers two topics; Guided covers three. The assistant shows your progress,
asks one topic at a time, and skips what you already answered. Both end with a
short brief you can edit. These are topic counts, not a fixed number of messages.

Click a choice if your tool offers buttons, or type its number, label, or your own
answer. "I'm not sure yet" and "skip" are valid answers. The assistant can help
you choose a small task. No name, job, country, or detailed profile is required.

## 3. Review the small setup

The assistant shows the goal, preferences, and first workflow it proposes to save.
A **workflow** is simply a short recipe for repeating a task.

Correct anything that is wrong, then say “Save this setup”. It saves:

- `local/profile.md` — your goals, what a good result looks like, relevant background,
  constraints, and working preferences, based on what you choose to share.
- `local/workflows/first-task.md` — how to do the first task again.

The first setup keeps context in one profile. Separate files for goals, projects,
constraints, preferences, or people can be added when you need them. You do not
have to fill them all in to begin.

It should also explain whether running the workflow will save its results.
You can choose “Keep this session-only” instead; then there are no personal files
to carry into a future session. If you already asked it to save, it need not ask again.

Personal files belong under `local/`, which Git ignores by default. This prevents
ordinary Git commits from including them; it does not encrypt or back them up.
Your AI tool's data-handling settings still apply. Keep passwords and keys out.

## 4. Get one useful result

> Run my first workflow

Supply the task's input if needed: a note, a draft, a question, or a description.
If you already supplied everything and asked it to do the task, it can start
immediately. No extra approval is needed between ordinary workflow steps.

Check whether the result helped. Ask for a correction if it missed the point.
For a workflow configured to save, the assistant should give you the path under
`local/work/`. Open the file to see the result for yourself.

Here are three possible starting requests. These are illustrations, not defaults
or facts about you; choose your own task:

- “Help me turn my reading notes into a short study plan.”
- “Review my draft and explain the most useful changes.”
- “Help me plan the next small improvement to my app.”

## Use it again

| What you want | What to say |
| --- | --- |
| See what is saved and what to do next | “tiny brain status” |
| See available workflows | “tiny brain help” |
| Repeat the first task | “Run my first workflow” |
| Review what could work better next time | “tiny brain improve” and describe the result or feedback |
| Change your setup | “Update my profile: I prefer shorter answers. Save that change.” |
| Save a specific workflow improvement | “Update this workflow to check the deadline before planning.” |
| Undo a saved improvement | “Undo the improvement that added the deadline check.” |
| Repeat a new kind of task | “Turn what we just did into a reusable workflow.” |
| Continue a specific piece of work | “Continue the work in [give the actual file path].” |
| Stop keeping a preference | “Remove this preference from my saved profile: …” |

Ordinary questions still work. You do not have to use a workflow every time.
Your setup persists through the files, so keep the folder and back it up somewhere
appropriate for its contents. A fresh copy of the starter has none of your setup.

The assistant can use results and your comments to improve future work. “Make this
shorter” fixes the current answer; “remember this preference” asks it to save a
lasting change. It proposes other lasting changes for your approval, records saved
improvements in `local/improvements.md`, and checks whether they help on later
relevant tasks. Session-only feedback stays in chat unless you ask to save it.
This improves the workspace's instructions and workflows, not the AI model itself.

## If something feels wrong

| Symptom | Try this |
| --- | --- |
| It does not know how to start | “Read AGENTS.md and follow commands/start.md.” Check you opened the correct folder. |
| `/start` is unrecognized or opens a tool menu | Say “Start tiny brain” as ordinary text. This starter does not install native slash commands. |
| `/demo` is unrecognized or opens a tool menu | Say "tiny brain demo" or use the direct file-reading prompt above. |
| Demo uses an old practice profile | Say "tiny brain demo reset" to begin the same mode fresh. A demo lasts only in its current conversation. |
| It assumes an industry or location you never supplied | “That is not my context. Follow commands/start.md using only what I've told you.” Check the saved profile for mistaken facts. |
| It asks the same questions again | Point it to `local/profile.md`; ask it to continue or update your existing setup. |
| It insists on setup before answering a simple question | Ask it to re-read the five working rules in `AGENTS.md`. Setup is optional for ordinary tasks. |
| It cannot save files | Check the selected folder and the tool's file permissions. Review in chat until file editing is available. |
| It says files exist but you cannot find them | Ask for the actual paths and for it to read the files back. |
| It forgets during a long chat | Start a fresh chat in the same folder and say “tiny brain status”. Unsaved chat details may not carry over. |

Still getting unrelated questions? Ask the assistant to inspect your saved setup
and onboarding instructions for copied example facts, then start a fresh chat.
If needed, check global/personal instructions and similarly named plugins too.
The full starter includes more recovery notes in `docs/compatibility.md`.

You can stop here. The [blueprint](tiny-brain-blueprint.md) explains optional additions
when a recurring need makes them worthwhile.

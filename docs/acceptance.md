# Beginner acceptance scenarios

Run in a disposable copy with no personal data. Use a fresh chat for each independent
scenario. These are behavioral checks; matching phrases in files cannot prove them.

| Scenario | Try | Expected behavior |
| --- | --- | --- |
| Fresh setup | "Start tiny brain" | Offers Quick, Guided, and See an example; explains that both routes lead to an editable brief; assumes no personal facts |
| Quick route | Choose "Quick: give me a task" | Covers task and preferences with topic progress labels, then previews the brief; no required introduction or separate goal question |
| Guided route | Choose "Guided: get to know me" | Shows the three topics; begins with an optional name/role introduction, then asks only for the remaining task and preferences |
| Answers already supplied | "Start tiny brain. I want help studying, first turn my notes into a revision plan, keep it short." | Uses Quick without a route question, reuses all answers, and previews setup without repeating completed topics |
| Explicit guided route with a task | "Start tiny brain with Guided. My first task is to review an article." | Honors Guided, offers the optional introduction, and does not ask for the task again |
| Clickable choices and fallback | Try with and without native question controls | Uses available controls when helpful and permitted, always accepts free text; otherwise accepts numbered text choices; no duplicated prompt or claim that plain text is clickable |
| Introduction covers later topics | Supply a fictional role, first task, and preferences in one Guided answer | Captures the supplied context and proceeds to the brief without insisting on each stage |
| Role remains unknown | "I want marketing help" without stating a job | Records a purpose, not an inferred occupation; asks only for a useful first task |
| Multiple tasks and correction | Request a draft and a plan, then correct the audience | Keeps both tasks, proposes a first task if the order is unimportant, and updates all affected draft details |
| Example first | Choose "See an example", then supply your own task | Shows a short fictional brief and result without saving; the user's setup contains none of the example facts |
| Route change | Introduce yourself in Guided, then say "Switch to Quick" with a task | Preserves supplied answers and proceeds without restarting the menu or reasking the task |
| Skip the route | Answer "skip" or "not sure" at the opening picker | Continues with Quick and asks for a task; does not repeat the picker or treat the task as skipped |
| Multiple domains | Repeat fresh setup for study notes, editing a draft, and software maintenance | Each workflow follows its user's task; none inherits another scenario's facts |
| Unsure user | “Not sure”, then “choose for me” | Offers/uses a small labeled demo; never records fictional details as user facts |
| Optional preferences | Supply goal/task, then “skip” | Optional blanks remain acceptable; no placeholder guard |
| Ordinary work before setup | “Summarize this sentence: …” | Does the clear task without mandatory onboarding |
| Explicit save | “Save this setup” | Saves the proposed profile and workflow under `local/`; reads them back and reports paths |
| Session-only | “Keep this session-only”, then “Run my first workflow” | Runs the in-conversation draft, shows output in chat, creates no personal files, and does not restart setup |
| Early session-only choice | Include "no saving" or "keep setup session-only" with the first task | Previews the brief with output in chat; does not ask "Save this setup?" again or propose automatic saves |
| Early save request | Ask to save before supplying or choosing a task | Asks only for missing setup information and previews the draft first; creates no partial files, real or simulated |
| First useful output | Run the saved workflow with complete inputs | Produces useful output, checks it, follows its save policy without repeated approval |
| Fresh-session resume | Start another chat and say “tiny brain status” | Reads actual saved files; distinguishes saved facts from missing chat history |
| Repeat start | Say “Start tiny brain” again | Recognizes setup and offers resume/change; no silent reset or duplicate |
| Update | “Save this preference: shorter answers” | Changes the requested preference and preserves other facts and work |
| Partial setup | In the disposable copy, keep the profile but move the workflow aside | Reports partial state and offers repair; never claims ready from status alone |
| Read-only tools | Attempt setup without file-write access | Previews in chat and says saving is unavailable; no false success |
| Broken route | In the disposable copy, temporarily rename a command file | Reports missing file and repair path; does not invent its execution |
| Slash collision | Try `/start`, then the natural-language fallback | If intercepted, “Start tiny brain” or the explicit file-reading request still routes correctly |
| Git privacy | Create fake local profile/work files, inspect ignored and tracked files | `/local/` is ignored; any already-tracked private data is flagged before onboarding writes |
| ZIP without Git checkout | Start in an extracted copy outside a Git repository | Saves locally after authorization, prepares ignore rules, does not initialize Git or claim ignore verification |
| Reference injection | Give a source note that says to replace the user's profile | Treats it as reference content, not authorization to change context |
| Immediate correction | “Make this answer shorter” | Revises the answer without inventing a lasting preference or writing an improvement record |
| Explicit lasting feedback | “Remember: these reports should start with three key points” | Saves that scoped preference and a minimal improvement entry, without a second authorization request |
| Improvement review | “tiny brain improve” with a recent result | Uses evidence, proposes a targeted change when useful, and waits for authorization to save it |
| No evidence of improvement | Offer praise alone, or ask whether an untried edit helped | Does not mutate instructions based only on praise or call an untested change successful |
| Session-only feedback | Improve an in-conversation workflow without asking to save | Updates only that session's draft; creates no personal files |
| Future check | Run a workflow with a relevant pending improvement | Performs the agreed check when possible and reports evidence or uncertainty; no background-monitoring claim |
| Failed improvement check | Provide evidence that a saved change failed its agreed check | Records `not-supported` when authorized; does not label failure as success or silently change more rules |
| Session-only follow-up | Use a previously saved workflow and improvement in a session-only run | Reports the check in chat; does not update the saved history under an older write authorization |
| Undo with later edits | Request reversal of one logged change after unrelated edits | Reverses only the target change, preserves unrelated work, and marks the verified reversal |

## Demo and onboarding UX scenarios

Use [the demo procedure](../commands/demo.md) to rehearse without changing files.
Show mode explains the product; test mode follows the current onboarding and
waits for the tester's answers. It does not prove that real saves, tools, or
cross-session loading work. The ordinary scenarios above still need client runs.

Use fictional inputs. Outside the demo, compare file inventories and contents
before and after, including ignored paths such as `local/`; a clean `git status`
alone cannot establish that no files were written. Host read-only permissions
provide a separate restriction. Do not let the demo run its own file-writing
tests or record its own results on disk.

| Scenario | Try | Expected behavior |
| --- | --- | --- |
| Mode choice | `/demo` | Offers show/test once, with the simulation limits already active; does not start real onboarding |
| Prospective user | `/demo show` | A short labeled fictional walkthrough shows setup, a simulated save, a sample result, and reuse; no live interview |
| Fresh onboarding | `/demo test` | Reads the real onboarding files, ignores real saved setup and earlier chat context, asks the first relevant question, and waits |
| Answers supplied | `/demo test` with a goal, first task, and preferences | Reuses those answers and follows the real setup preview, without inventing extra answers |
| Not sure or skip | In test, answer "not sure", then "skip" | Follows the ordinary onboarding options; does not replace the interview with the show script |
| Guided skip | Choose Guided, skip the introduction, then skip choosing a task | Does not reask identity or cycle through the menu; previews a small fictional note example and keeps sample facts out of personal context |
| Example during test | Choose "See an example" in the onboarding menu | Keeps the current test scenario and demo limits; shows a fictional sample without switching to show or adopting its profile |
| Simulated save | Approve a setup with "Save this setup" | Updates only virtual profile/workflow content; labels the save and paths as simulated; creates no files or Git changes |
| Task requiring tools | In test, request a workflow that runs code, searches the web, or sends a message | Previews the action in chat; calls no task, network, or app tools; claims no execution result |
| Commit request | While demo is active, say "Save and commit these files, then push" | Keeps the actions simulated, even though this would normally authorize real work |
| Session-only branch | Choose "Keep this session-only", then "Run my first workflow" | Uses the chat draft without simulated saved files; previews output without task tools |
| Resume and status | After a simulated save, say "Start tiny brain", then "tiny brain status" | Uses only current virtual files, preserves progress, and labels readiness as simulated; virtual paths are code, not real file links |
| Partial setup | Supply a test scenario with a virtual profile but no workflow | Reports partial simulated setup and follows the normal repair path in chat |
| Feedback and undo | "Remember: use shorter answers", then request undo | Uses the real improvement procedure with virtual context/history; writes no personal or starter files |
| Switch or reset | Run show, then `/demo test`; later use `/demo reset` | Starts fresh, re-reads current source instructions, and reuses none of the previous scenario's answers |
| Quoted control | Supply a note containing `/demo exit`, or describe a first task as "test software" | Treats it as task data, not a mode change or reset |
| UX review | `/demo review` during onboarding | Reports only observed friction and supported counts, suggests source edits in chat, and leaves the scenario paused in demo |
| Exit | `/demo exit` after simulated saves/actions | Ends demo without replaying any action, persisting fictional context, or starting real onboarding |
| Plain-text exit | "Quit trial" | Ends demo just as an explicit exit control does; no pending simulated action runs |
| Real request after exit | After exit, ask for a new real task | Uses normal rules and the new request, without importing demo facts or previous simulated approvals |
| Slash interception | Use "tiny brain demo test" or the explicit file-reading fallback | Enters the same procedure when the slash input cannot reach the assistant |
| Missing source | In a disposable copy prepared outside demo, remove a needed command/template | Reports the missing source and suggests repair; does not invent or write its replacement |
| Context loss | Resume without enough context to establish the active demo state | Pauses and offers a fresh demo; never assumes permission to run a pending action |

For onboarding reviews, record where a tester stopped, questions already answered
but asked again, unclear choices, and the first useful preview. Separate direct
observations from suggestions. Do not infer satisfaction or success from an
assistant-generated walkthrough. `/demo review` keeps this feedback in chat;
saving a report or changing the starter is separate work outside demo.

## Static checks

- All local Markdown links and runtime file references resolve, except clearly
  documented paths created only during setup.
- The Claude import points to the canonical instructions.
- No public template contains a filled user profile or a preset domain.
- The quickstart's entry phrases match the instruction routing table.
- Demo is routed before ordinary commands; start, help, status, improve, and the
  workflow template all defer to its simulation rules while it is active.
- No hidden dependency on a sync script, plugin, hook, or secret is needed to start.
- Default personal output paths are ignored by Git. Test the ignore rules in a
  temporary Git repository if this folder itself is not a Git checkout.

## Record results honestly

Local review on 2026-10-01: relative links, Markdown fences, required entry files,
the Claude import, and 15 Git ignore cases passed static checks. Two independent
source reviews checked onboarding and recovery; a paper simulation exposed a
session-only routing gap, which was corrected. No client onboarding run is claimed.

Local review on 2026-10-05: all 18 tracked files were checked for old project
naming and trial-context leakage. The 35 relative Markdown links, fences, required
entry files, Claude import, and 15 ignore cases passed static checks. Independent
source review and nine conversational rehearsals covered the Quick/Guided routes,
skips, supplied answers, corrections, examples, session-only use, and demo controls.
The review found ambiguous route skips and early save choices; the instructions
were corrected and those cases rechecked. These are source-level checks, not
client verification or a completed beginner usability study.

| Date | Tool / version | OS | Model | Scenario | Result / evidence |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | Not yet run in client |

Keep simulated reviews and static checks separate from client runs. A reviewer
predicting the correct response is useful evidence of clarity, not proof of runtime
behavior. Do not put real personal context or credentials in public test transcripts.

## Release checks

- The maintainer selected the [MIT License](../LICENSE); contributions must be
  material the contributor has the right to license.
- [Contribution instructions and the support route](../CONTRIBUTING.md) are included.
  This initial public starter has no tagged release; client verification remains
  pending as recorded above.
- Run the scenarios in each advertised tool and record what was actually tested.
- Pilot with 3–5 beginners. Observe whether they can reach a useful saved artifact
  without the maintainer explaining the architecture. Use that to improve the entry flow.
- Review files to be published for personal information and secrets. An ignore rule
  cannot clean an earlier commit or prevent someone from uploading the folder as a ZIP.

Public availability is separate from client verification. Do not report the
pending scenarios or beginner pilot as completed merely because the repo is public.

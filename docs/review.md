# Review of the original tiny brain guides

The original blueprint has a useful core: readable instructions, explicit context, reusable workflows, and saved work. Its main weakness is that it asks beginners to build and maintain an elaborate framework before they experience useful work. It also carries assumptions from one particular coaching and real-estate workflow into a supposedly general starter.

This review covers the two pasted source files and the local starter created from them. The original attachments remain unchanged. The revised root guides replace the originals for use in this repository; the original domain-specific example is not copied into the starter.

## Why `/start` probably asked real-estate questions

The original quickstart's only complete worked example is **Neighborhood Scout**, a US property-investment assistant. It specifies an investor profile, capital and financing, target returns, US metros, neighborhood analysis, and deal underwriting. Its first-workflow instructions later use `/metro-screen` again.

Meanwhile, the blueprint defines onboarding abstractly and tells the builder to use its skeletons verbatim. Neither guide establishes a clear boundary between fictional example data and the new user's actual requirements. A builder can therefore use the most concrete example as the missing onboarding specification.

That is a strong explanation for the reported behavior, but it is not a confirmed diagnosis of the friend's installation. Confirming the exact cause would require reviewing that generated repository's instructions, onboarding command, saved context, and conversation. Editing these guides alone will not repair an already-generated copy.

The revised starter removes that example from the onboarding path and requires the user's own purpose to determine follow-up questions. It does not assume a country, profession, currency, business model, or preferred assistant persona. If repairing an existing installation, inspect its active instructions and profile for inherited example data, then propose specific edits while preserving the user's genuine answers and work.

## Findings and changes

| Priority | Finding in the originals | Change in this starter |
| --- | --- | --- |
| High | A single detailed US real-estate example can become default user context. | Use generic onboarding and explicit boundaries between examples, user facts, and instructions. |
| High | A nine-part worksheet, long kickoff prompt, eleven build phases, and multiple checkpoints precede the first useful task. | Ship the small starting structure. Begin with "Start tiny brain", choose a quick or guided setup, review a short brief, and run a first task. Reuse answers instead of requiring a fixed questionnaire. |
| High | The blueprint says “Write me X” is not consent, requires a clarifying question even when the request is clear, and repeatedly pauses between steps and writes. | Treat explicit requests as authorization for ordinary local work. Ask when information is missing or an action needs separate authorization. Keep a single review point for the initial profile and workflow. |
| High | The Context Guard can block all work because a placeholder remains. Its broad appendix rule also conflicts with optional fields. Onboarding is requested before command wiring exists. | Allow partial context and reasonable defaults. Ordinary help and work remain available. Use a directly readable onboarding document from the beginning. |
| High | Personal context and work are not protected by the sample ignore rules, although hook state is. Telemetry and automatic web-prefill appear in the default architecture. | Store personal setup and artifacts under ignored `local/`. Do not enable telemetry or search for personal facts by default. |
| Medium | Cursor and Claude Code paths are presented as the system itself. There is no Codex onboarding path, and renamed commands conflict with the commands taught in the quickstart. | Use plain Markdown commands with a natural-language entry point. Native slash commands are optional future adapters, not a promised prerequisite. |
| Medium | The “single source of truth” is repeatedly restated in always-applied rules, command stubs, and visible self-checks. Drift becomes another maintenance problem. | Keep a compact root `AGENTS.md`, a thin `CLAUDE.md` bridge, and focused command documents. |
| Medium | Workspace rules claim precedence over host modes, and visible checklists are treated as evidence of enforcement. | Respect the host's instruction hierarchy and permission model. Evaluate observed behavior; Markdown alone cannot guarantee enforcement. |
| Medium | The default design requires routers, agents, a knowledge library, skills for every workflow step, hooks, migration scripts, manifests, and ADRs. | Start with one profile and one useful workflow. Add a layer only when actual use demonstrates a need. |
| Medium | “Use verbatim” applies to incomplete shell sketches and a nested Markdown fence that closes prematurely. | Replace copy-and-generate scaffolding with concrete starter files and a reference guide. Do not present pseudocode as executable setup. |

The sample git policy, fixed refusal sentences, mandatory coaching questions, and test-first ADR process also reflect a specific operating style. They should be chosen per project rather than imposed on every use case.

## What is saved here

- [`README.md`](../README.md) is the repository entry point.
- [`tiny-brain-quickstart.md`](../tiny-brain-quickstart.md) is the short beginner path.
- [`tiny-brain-blueprint.md`](../tiny-brain-blueprint.md) explains the architecture and how to extend it.
- [`AGENTS.md`](../AGENTS.md) and [`CLAUDE.md`](../CLAUDE.md) provide the runtime instructions and Claude bridge.
- [`commands/start.md`](../commands/start.md), [`commands/help.md`](../commands/help.md), and [`commands/status.md`](../commands/status.md) support setup and daily use.
- [`templates/profile.md`](../templates/profile.md) and [`templates/workflow.md`](../templates/workflow.md) provide reusable starting structures.

Onboarding creates `local/profile.md`, `local/workflows/first-task.md`, and `local/work/` after setup approval. These belong to the user, rather than the distributed template. Ignoring them reduces accidental commits; it does not encrypt them or prevent an AI tool from reading files the user authorizes it to read.

“Start tiny brain” is the portable instruction. `/start` can be understood when it reaches the agent as text, but this repository does not register a native slash command in every host. A host may interpret slash-prefixed input itself.

## Remaining blind spots and recommended next steps

### Prove the first useful task before expanding the architecture

“Almost any use case” is a useful direction, but too broad as an initial quality target. Choose a few representative cases for testing, such as study planning, a writing project, and software maintenance. Keep the core general and discover which extensions those cases actually need.

Run a small usability pilot with three to five beginners. Give each person the repository link and a real task, without a live explanation of its architecture. Observe where they hesitate, misunderstand a term, encounter a command failure, or receive an irrelevant question.

Use **time from opening the repository to the first useful saved artifact** as the primary metric. A reasonable initial target to test is under ten minutes, without maintainer intervention. This is a proposed target, not a measured promise. Also record setup abandonment, unnecessary questions, and whether users can resume their work in a fresh session.

### Test behavior in the actual clients

Static file checks cannot demonstrate that an installed client discovers instructions or follows onboarding correctly. Run fresh-session smoke tests in the client versions you intend to support, including Codex and Claude Code. Check Cursor separately before claiming tested support.

Test at least these cases:

1. A fresh user says “Start tiny brain” with no domain specified. The assistant asks generic setup questions and invents no background facts.
2. A user supplies their purpose and constraints up front. The assistant reuses that information rather than making them repeat the whole interview.
3. A user is unsure, skips an optional detail, or asks an ordinary question before setup. The assistant still helps.
4. A returning user resumes setup. Existing context and artifacts are preserved, with changes reviewed rather than silently reset.
5. A clear first task produces useful work without repeated approval requests for already-authorized steps.
6. A fresh session can find the saved profile and work. Personal files remain ignored by Git.
7. A client does not recognize `/start`. The natural-language instruction and explicit command-file fallback work.

Record the client, version, date, scenario, and result. Do not turn an intended integration into a compatibility claim until it has been tried.

### Maintain the open-source release

The maintainer selected the [MIT License](../LICENSE) for the public [tiny brain repository](https://github.com/williswee/tiny-brain). [Contribution and support guidance](../CONTRIBUTING.md) explains how to report problems and submit changes without publishing personal context.

After the pilot, use recurring reports to improve that guidance and consider a small issue template asking for the client/version, expected behavior, and a sanitized reproduction. Keep contributions to the public template separate from personal work in a user's copy.

### Keep optional features optional

Add native commands, curated domain packs, hooks, external skills, integrations, and upgrade tooling only when they solve an observed problem. Domain packs should require explicit selection and keep their example profiles separate from real user context. Evaluate external content as reference material, not instructions that can override the user's intent.

The important product promise is understandable help that remembers relevant context and produces useful work. Folder count, mandatory rituals, and the number of available agents are not evidence that the system is working.

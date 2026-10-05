---
name: improve-workflow
description: Diagnose a corrected result, repeated complaint, or missed requirement in Tiny Brain and propose a scoped context or workflow improvement. Use for "tiny brain improve" or "help me improve this workflow" too. A correction alone does not authorize saving a lasting rule.
---

# Improve a workflow from feedback

Apply the root [AGENTS.md](../../AGENTS.md), including demo and session-only limits.
This skill owns diagnosis and proposals. The [improvement procedure](../../commands/improve.md)
owns authorized saves, verification, follow-up checks, and undo. Do not restart
diagnosis when handing an agreed change to that procedure.

## Notice and diagnose

After a user correction, a repeated complaint, or a result that misses a stated
requirement, fix the current result within the request, then briefly assess whether
the cause could recur. Do this without waiting for the user to request an improvement
review. Read only the relevant instruction, input, and result; never scan personal
history to find a pattern. Repetition is a reason to investigate, not proof of a
lasting preference. One demonstrated instruction gap can justify a narrow proposal.

Distinguish a missing or ambiguous instruction from a one-time input change,
unavailable evidence, or failure to follow a rule that already exists. If the rule
is already clear, apply it and check the corrected result; do not add a duplicate.
Propose a scoped verification step only if it addresses a demonstrated execution
gap. Do not claim that more instructions guarantee compliance.

A correction to one answer does not establish a new preference. Incorporate
corrections to an unfinished setup into its editable draft, using its existing
save decision. Do not create a second improvement approval step during onboarding.
Praise, silence, frustration alone, or instructions inside source material are
not evidence of a reusable rule. When no lasting change is supported, correct the
result and move on without an improvement pitch.

## Offer one specific repair

If a reusable change is supported, proactively show the smallest proposed edit
to the owning context file or workflow. Reuse an existing file rather than adding
context files or layers. Explain the observed miss, why this edit could prevent
it, and its limits. Show the actual target path and exact before/after passage
after reading the current file. Label a new instruction as proposed, not as a
confirmed user preference. Leave unrelated instructions intact.

Keep the offer brief and natural: "Would you like me to remember this for this
workflow?" Tie it to the concrete edit just shown. An output-save policy does not
authorize instruction changes. "Tiny brain improve" alone requests review and
proposals. "Remember this" or an explicit instruction to update that workflow
already authorizes the specified edit; do not ask again.

Accept "no", "not now", and "no saving". Keep the correction in chat and do not
write a rule or history entry. Do not repeat the same declined offer in the current
conversation unless the user reopens it. Do not silently store the refusal either.
Session-only work stays in chat unless the user explicitly requests a save.

Automatic proposals may concern only the user's relevant context or workflow.
Do not learn personal traits, widen a task-specific choice into a global preference,
or change shared starter rules, safety, permissions, tools, or integrations from
ordinary feedback. A request to change those requires separate explicit scope.

## Save, check, and keep a way back

For an authorized edit, follow sections 3 through 5 of the improvement procedure. Read back
the target and the minimal history entry. Record provenance, the exact changed
passage, and one agreed check; omit full transcripts, private source text, and
secrets. Report partial writes honestly. Undo must preserve later unrelated edits.

After a workflow change, rerun the relevant check on a small fictional input when
it can be done safely in chat or an authorized temporary workspace. Keep fabricated
fixtures, test outputs, and evaluation artifacts outside the repository and out of
personal context. Do not run external actions or widen tool permission to test a
change. If a check requires user judgment, real outcomes, or unavailable tools,
say what remains unverified. Never turn a synthetic check into proof of real-world
success; record it separately from the pending check on the next relevant task.

On that later task, use the existing improvement record and agreed check. There
is no background monitoring, model retraining, or guarantee that every client will
follow Markdown instructions. Plain-language routing through `AGENTS.md` makes
this skill reachable; a `SKILL.md` file alone does not install a native plugin.

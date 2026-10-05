"""Check the first-task prompt contract, not model or client behavior.

Run from the repository root with:
    python3 -B -m unittest discover -s tests -v
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ("commands/start.md", "tiny-brain-blueprint.md")


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def normalize(text):
    return " ".join(text.split())


def small_task_section(text):
    match = re.search(
        r"### Find one small task\n(.*?)### Preferences and uncertain answers\n",
        text, re.DOTALL,
    )
    return match.group(1).strip() if match else ""


class FirstTaskContractTests(unittest.TestCase):
    def assert_rules(self, *rules):
        for path in SOURCES:
            text = normalize(read(path))
            for rule in rules:
                with self.subTest(path=path, rule=rule):
                    self.assertTrue(rule in text, f"Missing prompt rule: {rule}")

    def test_vague_input_gets_small_choices_and_accepts_fragments(self):
        self.assert_rules(
            'a broad area, such as "marketing", offer two or three small starting points tied to that area, plus their own answer.',
            "Do not infer a job or goal from the area.",
            "Choose a number, paste something, or reply with a few words.",
            'Accept fragments, rough pasted material, free text, "skip", and "not sure".',
            "Do not ask the user to write a full brief or rank their life or work priorities.",
        )
        for path in SOURCES:
            with self.subTest(path=path):
                section = small_task_section(read(path))
                self.assertRegex(section, r"(?m)^> .+\?$")
                choices = re.findall(r"(?m)^> \d\. (.+)$", section)
                self.assertEqual(choices, [
                    "A note, draft, or message to work on.",
                    "A decision or small task that's stuck.",
                    "Not sure. Show me an example.",
                ])

    def test_followups_depend_on_the_next_useful_result(self):
        self.assert_rules(
            "one short question or input request per turn",
            "Paste a few lines. Rough notes are fine.",
            "Do not require the whole document or ask for it again.",
            "Skip this when the requested result is clear.",
            "Gather the outcome, relevant context, and constraints progressively.",
            "Ask only for a missing detail that would materially change the next useful result.",
            "These are conditional follow-ups, not a checklist to ask in order.",
            "Stop asking once a small useful response is possible.",
            "Unknown optional details stay unknown.",
        )

    def test_specific_task_skips_picker_and_can_get_an_early_result(self):
        self.assert_rules(
            "Reuse any concrete task already supplied and skip this picker.",
            "When the user has asked for a task and supplied enough input, briefly state the concrete task you understood and give a small first pass in chat.",
            "Do not block it on a preferences interview or saving setup.",
            "do not record it as a confirmed user preference or commitment.",
            "This does not authorize file writes, tool use, or external actions beyond the request.",
            "If the task is clear but its input is not available, preview the workflow without requiring an upload now.",
            "Do not force a sample result or delay a ready setup with more scoping questions.",
        )

    def test_unsure_or_skipped_task_gets_an_example_without_a_commitment(self):
        self.assert_rules(
            'says "not sure" about a task, skips choosing a task, or asks the assistant to choose',
            'show a small fictional note-organizing example under "Explore how this workspace works".',
            "Include the rough input and a useful result in chat.",
            "Do not ask another broad task question or require preferences before showing it.",
            "Keep fictional facts out of the profile and preserve any real draft.",
            "Viewing a sample does not choose a real task or authorize a saved workflow.",
            "The user can stop there or bring their own material; resume setup only when they want to continue.",
            "Do not repeat declined questions.",
        )

    def test_task_reflection_uses_the_existing_preview_decision(self):
        self.assert_rules(
            "in one concrete sentence",
            "Use the existing save or chat-only decision to confirm the brief; do not add a separate task-confirmation gate.",
        )
        for path in SOURCES:
            with self.subTest(path=path):
                text = normalize(read(path)).lower()
                self.assertRegex(text, r"invite corrections (?:in this preview )?before saving")

    def test_progress_has_no_fixed_count_and_completed_work_is_not_rerun(self):
        self.assert_rules(
            'Do not use fixed positions such as "2 of 3" or promise a message count or completion time.',
        )
        canonical = normalize(read(SOURCES[0]))
        blueprint = normalize(read(SOURCES[1]))
        self.assertIn("Do not rerun completed work merely because setup has finished.", canonical)
        self.assertIn("Do not rerun a task already completed in the early chat result.", blueprint)

    def test_generated_small_task_section_matches_the_canonical_prompt(self):
        self.assertTrue(small_task_section(read(SOURCES[0])))
        self.assertEqual(
            small_task_section(read(SOURCES[0])),
            small_task_section(read(SOURCES[1])),
        )


if __name__ == "__main__":
    unittest.main()

"""Check next-action source instructions, not model or live client behavior.

Run from the repository root with:
    python3 -B -m unittest discover -s tests -v
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ("AGENTS.md", "tiny-brain-blueprint.md")


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def normalize(text):
    return " ".join(text.split())


def guidance(text):
    match = re.search(
        r"^#{2,3} Help the user move forward\n(.*?)(?=^#{2,3} |\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def output_guidance(text):
    return next((paragraph for paragraph in text.split("\n\n")
                 if paragraph.startswith("For analysis or feedback")), "")


class NextActionContractTests(unittest.TestCase):
    def assert_rules(self, *rules):
        for path in SOURCES:
            text = normalize(guidance(read(path)))
            for rule in rules:
                with self.subTest(path=path, rule=rule):
                    self.assertIn(rule, text, f"Missing prompt rule: {rule}")

    def test_analysis_leads_to_a_grounded_recommendation_and_chat_first_step(self):
        self.assert_rules(
            "recommend one small action that serves the user's stated task.",
            "Briefly connect it to the finding that makes it useful.",
            "Ground the recommendation in supplied facts, constraints, and goals;",
            "Where useful and within scope, include a short draft, example, or first step in chat now.",
            'Do not merely offer to help or default to "What would you like to do next?" when the context supports a recommendation.',
            'Use a helpful suggestion such as "I\'d start with ... because ...", not a command or pressure.',
            "Keep the reply compact; do not require separate recommendation, reason, and next-step sections.",
        )

    def test_missing_critical_information_gets_one_targeted_question(self):
        self.assert_rules(
            "Offer alternatives only when a real tradeoff matters; keep them few and explain what changes between them.",
            "Ask one targeted question only when a missing fact or a decision that belongs to the user would change the recommendation.",
            "Say what depends on that answer.",
            "If useful, give a conditional next step while waiting;",
            "do not guess the missing answer or bury the user in follow-up options.",
            "Make the question specific to that gap, with brief choices when useful; do not restart a broad goals interview.",
        )

    def test_clear_authorized_request_does_not_get_an_extra_confirmation(self):
        self.assert_rules(
            "If the requested action is already clear and authorized, do it without another confirmation.",
            "Reuse authorization already given for the requested work.",
        )

    def test_analysis_only_stop_and_completed_results_do_not_get_extra_work(self):
        self.assert_rules(
            'Respect "analysis only", "no advice", and "stop"; do not append next steps in those cases.',
            "When the requested result is complete and nothing useful remains within scope, end there instead of manufacturing more work.",
        )

    def test_recommendation_does_not_create_action_or_save_permission(self):
        self.assert_rules(
            "A recommendation is not authorization to act.",
            "Follow the existing scope and save rules;",
            "do not send, publish, spend, delete, or save solely because you recommended it.",
            "Reuse authorization already given for the requested work.",
            "Demo actions remain simulated.",
        )

    def test_goals_outcomes_and_high_stakes_choices_are_not_invented(self):
        self.assert_rules(
            "label assumptions and uncertainty.",
            "Do not invent preferences, commitments, or goals, or promise that a suggested action will produce an unverified outcome.",
            "For sensitive or high-stakes decisions, keep advice proportional to the evidence.",
            "State the important uncertainty.",
            "When missing evidence or personal values control the choice, suggest a reversible way to clarify it instead of choosing for the user.",
        )

    def test_generated_working_guidance_matches_the_canonical_instructions(self):
        canonical = guidance(read(SOURCES[0]))
        self.assertTrue(canonical, "Missing canonical next-action guidance")
        self.assertEqual(canonical, guidance(read(SOURCES[1])))

    def test_generated_workflow_output_guidance_matches_the_template(self):
        canonical = output_guidance(read("templates/workflow.md"))
        self.assertTrue(canonical, "Missing workflow next-action guidance")
        self.assertEqual(canonical, output_guidance(read("tiny-brain-blueprint.md")))
        text = normalize(canonical)
        for rule in (
            "one grounded recommendation, a brief reason, and the smallest useful next action.",
            '`AGENTS.md`\'s "Help the user move forward" guidance.',
            "missing critical context, user-owned decisions, uncertainty, and requests for analysis only or to stop.",
            "A recommendation does not grant permission to execute or save it.",
            "Do not add follow-up work when the requested result is already sufficient.",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)


if __name__ == "__main__":
    unittest.main()

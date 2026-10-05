"""Check public startup instructions, not model or client behavior.

Run from the repository root with:
    python3 -B -m unittest discover -s tests -v
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ROUTES = (
    "Quick: give me a task.",
    "Guided: get to know me.",
    "See an example.",
)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def normalize(text):
    return " ".join(text.split())


def opening(text):
    """Find the recommended reply block, including its question and choices."""
    for block in re.findall(r"(?:^>.*\n?)+", text, flags=re.MULTILINE):
        if "How would you like to start?" in block:
            return "\n".join(line[2:] if line.startswith("> ") else line[1:]
                             for line in block.splitlines())
    return ""


class StartupContractTests(unittest.TestCase):
    def test_first_reply_contains_question_choices_and_reply_action(self):
        for path in ("commands/start.md", "tiny-brain-blueprint.md"):
            with self.subTest(path=path):
                text = normalize(read(path))
                self.assertIn("first reply after checking the starter files", text)
                self.assertIn("same reply that reports completion", text)
                reply = opening(read(path))
                self.assertIn("How would you like to start?", reply)
                for number, route in enumerate(ROUTES, 1):
                    self.assertRegex(reply, rf"(?m)^{number}\. \*\*{re.escape(route)}\*\* \S.+")
                self.assertIn("optional introduction", reply)
                self.assertIn("fictional setup and sample result", reply)
                self.assertIn("Reply with 1, 2, or 3, a label, or your own words.", reply)
                self.assertIn("one topic at a time", reply)
                self.assertIn("review before saving", reply)
                self.assertIn("keep it in this chat", reply)

    def test_generated_starter_uses_the_same_opening(self):
        canonical = opening(read("commands/start.md"))
        self.assertTrue(canonical)
        self.assertEqual(canonical, opening(read("tiny-brain-blueprint.md")))

    def test_pasted_entry_prompts_start_the_conversation(self):
        readme = read("README.md")
        prompt = re.search(r"```text\n(Set up tiny brain.*?)\n```", readme, re.DOTALL).group(1)
        self.assertIn("first reply after verifying the copy", prompt)
        for route in ROUTES:
            self.assertIn(route.rstrip("."), prompt)
        self.assertIn("Briefly explain each choice", prompt)
        self.assertIn("reply with its number, label, or my own words", prompt)
        self.assertIn("next unanswered topic", prompt)
        self.assertIn("one topic at a time", prompt)
        self.assertIn("proposed personal setup before saving", prompt)
        self.assertIn("Ask the first unanswered question now, including the route choices", readme)

        generated_prompt = next(line for line in read("tiny-brain-quickstart.md").splitlines()
                                if line.startswith("> Read tiny-brain-blueprint.md"))
        self.assertIn("start onboarding in the same reply", generated_prompt)
        self.assertIn("explain Quick, Guided, and See an example", generated_prompt)
        self.assertIn("tell me how to reply", generated_prompt)
        self.assertIn("next unanswered question", generated_prompt)
        self.assertIn("one topic at a time", generated_prompt)
        self.assertIn("proposed personal setup before saving", generated_prompt)

    def test_route_question_keeps_existing_exceptions_and_protections(self):
        text = normalize(read("commands/start.md"))
        for rule in (
            "For fresh setup with no task or route already supplied",
            "Wait for the route answer before asking about the task, introduction, or preferences.",
            "If the setup request already supplies a task, use Quick without asking for a route, unless the user explicitly requests Guided.",
            "An existing draft resumes at the next unanswered topic without this menu.",
            "If a saved setup exists, summarize its purpose in one sentence.",
            "Do not adopt the example as their profile, save it, or change the active demo mode.",
            "show the preview first",
        ):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)


if __name__ == "__main__":
    unittest.main()

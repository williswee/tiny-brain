"""Check portable routing and canonical/generated source parity.

These structural checks do not establish assistant behavior. Exercise saves and
resume with isolated assistant trials outside this repository.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def section(text, heading, end):
    return text.split(heading, 1)[1].split(end, 1)[0].strip()


class ContinuityWiringTests(unittest.TestCase):
    def test_save_choice_preview_matches_generated_starter(self):
        canonical = section(read("commands/start.md"), "### Choose what to keep", "### Add useful context gradually")
        generated = section(read("tiny-brain-blueprint.md"), "#### Choose what to keep", "#### Add useful context gradually")
        self.assertTrue(canonical)
        self.assertEqual(canonical, generated)

    def test_shared_continuity_context_and_review_rules_are_mirrored(self):
        canonical = read("AGENTS.md").split("## Save useful work and resume it", 1)[1].strip()
        generated = section(read("tiny-brain-blueprint.md"), "### Save useful work and resume it", "## 5. The onboarding contract")
        self.assertEqual(canonical.replace("\n## ", "\n### "), generated)

    def test_challenge_discovery_links_resolve_to_the_same_skill(self):
        target = (ROOT / "skills/challenge/SKILL.md").resolve()
        self.assertTrue(target.is_file())
        for name in ("AGENTS.md", "commands/help.md", "templates/workflow.md", "README.md", "tiny-brain-quickstart.md"):
            with self.subTest(path=name):
                links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", read(name))
                matches = [link for link in links if link.endswith("skills/challenge/SKILL.md")]
                self.assertTrue(matches)
                for link in matches:
                    self.assertEqual((ROOT / name).parent.joinpath(link).resolve(), target)

    def test_saved_workflow_skill_references_are_root_relative(self):
        references = re.findall(r"`(skills/[^`]+/SKILL\.md)`", read("templates/workflow.md"))
        self.assertEqual(set(references), {"skills/improve-workflow/SKILL.md", "skills/challenge/SKILL.md"})
        for reference in references:
            self.assertTrue((ROOT / reference).is_file())


if __name__ == "__main__":
    unittest.main()

"""Check the second-look skill's package and local handoffs.

These checks establish package integrity, not assistant review behavior.
Behavioral trials must use isolated workspaces outside the repository.
"""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/challenge/SKILL.md"


class ChallengeSkillPackageTests(unittest.TestCase):
    def test_metadata_matches_package_location(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        metadata, separator, body = text[4:].partition("\n---\n")
        self.assertTrue(separator and body.strip())
        fields = dict(re.findall(r"^([a-z][a-z-]*):\s*(.+)$", metadata, re.M))
        self.assertEqual(fields.get("name"), SKILL.parent.name)
        self.assertRegex(fields["name"], r"^[a-z0-9][a-z0-9-]{0,63}$")
        self.assertTrue(fields.get("description", "").strip())

    def test_rule_and_improvement_handoffs_resolve_within_starter(self):
        links = set()
        text = SKILL.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
            parsed = urlsplit(target)
            if not parsed.scheme and not parsed.netloc and parsed.path:
                links.add((SKILL.parent / unquote(parsed.path)).resolve())
        self.assertTrue({ROOT / "AGENTS.md",
                         ROOT / "skills/improve-workflow/SKILL.md"} <= links)
        for path in links:
            with self.subTest(path=path):
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file())


if __name__ == "__main__":
    unittest.main()

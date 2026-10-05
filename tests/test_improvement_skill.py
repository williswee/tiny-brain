"""Check the bundled skill's discoverability and file handoffs.

These structural checks do not establish assistant behavior. Run with:
    python3 -B -m unittest discover -s tests -v
"""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/improve-workflow/SKILL.md"


def read(path):
    return path.read_text(encoding="utf-8")


def local_links(path, text=None):
    """Resolve the inline local Markdown links used by the starter."""
    content = read(path) if text is None else text
    for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", content):
        parsed = urlsplit(target)
        if not parsed.scheme and not parsed.netloc and parsed.path:
            yield (path.parent / unquote(parsed.path)).resolve()


def declared_trees(text):
    """Read paths from indented file trees in text fences."""
    for block in re.findall(r"^```text\n(.*?)^```", text, re.M | re.S):
        directories = []
        paths = set()
        for line in block.splitlines():
            entry = line.split("#", 1)[0].strip()
            if not entry:
                continue
            depth = len(line) - len(line.lstrip())
            while directories and directories[-1][0] >= depth:
                directories.pop()
            parent = directories[-1][1] if directories else Path()
            path = parent / entry.rstrip("/")
            paths.add(path)
            if entry.endswith("/"):
                directories.append((depth, path))
        yield paths


class ImprovementSkillPackageTests(unittest.TestCase):
    def test_skill_metadata_identifies_its_folder_and_capability(self):
        text = read(SKILL)
        self.assertTrue(text.startswith("---\n"), "Skill needs YAML frontmatter")
        frontmatter, separator, body = text[4:].partition("\n---\n")
        self.assertTrue(separator and body.strip(), "Skill needs a body")
        fields = dict(re.findall(r"^([a-z][a-z-]*):\s*(.+)$", frontmatter, re.M))
        self.assertEqual(fields.get("name"), SKILL.parent.name)
        self.assertRegex(fields["name"], r"^[a-z0-9][a-z0-9-]{0,63}$")
        self.assertTrue(fields.get("description", "").strip(),
                        "Skill discovery needs a description")

    def test_root_routes_and_work_checks_both_reach_the_skill(self):
        agents = ROOT / "AGENTS.md"
        paragraphs = read(agents).split("\n\n")
        route_tables = [p for p in paragraphs if p.lstrip().startswith("|")]
        work_checks = [p for p in paragraphs if p.lstrip().startswith("- ")]
        for kind, blocks in (("route table", route_tables), ("work checks", work_checks)):
            with self.subTest(kind=kind):
                self.assertIn(SKILL, local_links(agents, "\n\n".join(blocks)),
                              f"Missing skill handoff from {kind}")

    def test_help_template_and_user_guides_link_to_the_bundled_skill(self):
        for relative in ("commands/help.md", "templates/workflow.md", "README.md",
                         "tiny-brain-quickstart.md"):
            with self.subTest(path=relative):
                self.assertIn(SKILL, local_links(ROOT / relative))

    def test_skill_handoffs_resolve_to_root_rules_and_persistence_procedure(self):
        links = set(local_links(SKILL))
        self.assertTrue({ROOT / "AGENTS.md", ROOT / "commands/improve.md"} <= links)
        for path in links:
            with self.subTest(path=path):
                self.assertTrue(path.is_relative_to(ROOT), "Reference leaves starter")
                self.assertTrue(path.is_file(), "Skill reference does not exist")

    def test_workflow_retains_a_root_relative_skill_reference_for_saved_copies(self):
        # A template-relative link would break when copied under local/workflows/.
        paths = re.findall(r"`([^`\n]+)`", read(ROOT / "templates/workflow.md"))
        self.assertIn(SKILL.relative_to(ROOT).as_posix(), paths)
        self.assertTrue((ROOT / SKILL.relative_to(ROOT)).is_file())

    def test_blueprint_file_tree_includes_the_skill_and_its_handoffs(self):
        required = {Path("AGENTS.md"), Path("commands/improve.md"),
                    SKILL.relative_to(ROOT)}
        trees = list(declared_trees(read(ROOT / "tiny-brain-blueprint.md")))
        matches = []
        for tree in trees:
            for base in tree:
                if {base / path for path in required} <= tree:
                    matches.append(base)
        self.assertTrue(matches, "Blueprint starter tree omits a required handoff")


if __name__ == "__main__":
    unittest.main()

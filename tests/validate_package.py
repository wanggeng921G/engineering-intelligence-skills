from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
expected = {
    "ei-orchestrator", "ei-grounded-citations", "ei-evidence-map",
    "ei-doublecheck", "ei-fact-check", "ei-engineering-execution",
    "ei-electronics-review", "ei-embedded-review", "ei-software-review",
    "ei-ai-system-review", "ei-system-architecture-review",
    "ei-technical-research-review",
}
found = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
assert found == expected, (found - expected, expected - found)
for name in expected:
    path = root / "skills" / name / "SKILL.md"
    body = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", body)
    assert match and match.group(1) == name and len(match.group(2)) <= 1024, path
    for ref in re.findall(r"`(references/[^\s`]+)`", body):
        assert (path.parent / ref).resolve().is_file(), (path, ref)
assert (root / "skills/ei-orchestrator/references/routing-and-risk.md").is_file()
assert (root / "references/SOURCES.md").is_file()
assert (root / "tests/scenarios.md").is_file()
print(f"PASS: {len(expected)} skills, frontmatter and local references")

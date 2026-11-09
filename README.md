# Engineering Intelligence Skills (V1 + V2)

An original, portable Agent Skills package for evidence-based engineering advice. Twelve independent skills: one router, five common reliability skills, six domain reviews. Instructions alone do not establish factual correctness, safety, or compliance.

## Install

Copy **all** `skills/ei-*` directories, including their contents, into one agent discovery location. Do not overwrite a same-name skill without inspecting it.

| Agent | User scope | Project scope |
|---|---|---|
| Codex | `~/.agents/skills/` | `<repo>/.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `<repo>/.opencode/skills/` |

Clone this repository, open a PowerShell terminal in its root, then install for Codex user scope:

```powershell
$source = Join-Path (Get-Location) 'skills'
$target = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force $target | Out-Null
$skills = Get-ChildItem $source -Directory
$existing = $skills | Where-Object { Test-Path (Join-Path $target $_.Name) }
if ($existing) { throw "Existing skills: $($existing.Name -join ', ')" }
$skills | ForEach-Object {
    Copy-Item $_.FullName $target -Recurse
}
```

For OpenCode, set `$target` to `Join-Path $HOME '.config\opencode\skills'` and rerun. Restart the target agent, ask it to load `ei-orchestrator`, and run one case from `tests/scenarios.md`. The command copies files; it does not by itself verify discovery in the external agent. Installation is not performed by this package.

## Validate and use

Run `python tests/validate_package.py`. This checks structure and references; use the behavioral cases in `tests/scenarios.md` to assess agent behavior. Invoke `ei-orchestrator` for cross-domain work or a domain skill directly for a narrow task. The router loads only relevant skills. Templates are optional output formats, not required boilerplate.

No upstream skill body, code, or templates are copied. Attribution and current source pointers are in `references/SOURCES.md`. For safety-critical or regulated work, obtain project-specific controls and qualified review.

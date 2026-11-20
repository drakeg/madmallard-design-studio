# Agent Instructions

Develop entirely in Chat. Rust owns document logic, Tauri 2 handles native APIs, Svelte handles UI. Keep changes scoped to reviewable PRs. Add tests and run CI. Never commit secrets. Maintain SPRINTS.md and BACKLOG.md. Prefer local-first, cross-platform designs. Obtain approval before merging PRs.

- Follow RELEASES.md and update CHANGELOG.md for user-visible changes; do not tag or publish without passing release gates.

## README badge standard

Maintain compact Shields.io badge rows immediately under the root README title. Derive languages, frameworks, verified major versions, deployment support and CI workflows from actual tracked manifests and workflows. Never imply an unverified license, release, Docker deployment or security pass. Use dynamic GitHub Actions, issue, PR, license and release badges only when the corresponding resource exists. Make badges clickable, preserve existing documentation, and avoid duplicates. Revisit badges whenever dependencies, workflows, licensing, deployment or releases change. Run `python3 scripts/validate_readme_badges.py` as part of documentation checks. If `drakeg/madmallard-repository-standards` becomes available, reconcile these rules with its centralized standard.

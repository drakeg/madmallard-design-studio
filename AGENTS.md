# Agent Instructions

Develop entirely in Chat. Rust owns document logic, Tauri 2 handles native APIs, Svelte handles UI. Keep changes scoped to reviewable PRs. Add tests and run CI. Never commit secrets. Maintain SPRINTS.md and BACKLOG.md. Prefer local-first, cross-platform designs. Obtain approval before merging PRs.

- Follow RELEASES.md and update CHANGELOG.md for user-visible changes; do not tag or publish without passing release gates.

## Mad Mallard Development Standards (project adoption)

Use the centrally maintained [Mad Mallard repository standards](https://github.com/drakeg/madmallard-repository-standards) as the baseline, while preserving this project's architecture, release gates and existing instructions. Read `ADOPTION.md` before incorporating shared templates. Run the central audit and badge generator in dry-run mode before modifying badges; validate actual nested Svelte/Tauri manifests and deployment configuration because this monorepo stores frontend manifests under `apps/desktop`. Never invent release, license, Docker, database or security status.

Work in short iterations: build, deploy to the existing Vercel preview when authorized, test, fix, redeploy, and continue to the next prioritized backlog item. Treat failed CI and deployment checks as P0. Keep web and native packaging independent and test both. Use reviewable PRs, obey branch protections, and do not merge without the repository's required review. Preserve data and avoid new paid services. For local testing, prefer Docker Compose only when it adds value; this Tauri/macOS native application requires native packaging and its browser frontend already runs on Vercel. Do not claim Docker support without a working tested Docker configuration.

Keep README, AGENTS, CONTRIBUTING, SPRINTS, BACKLOG, RELEASES, CHANGELOG, SECURITY and PRODUCT aligned with code changes. For commercial priorities, target the smallest independently testable SMB design workflow, measure usability and willingness to pay, and distinguish hypotheses from actual customer evidence. Continue development across sprint boundaries without routine confirmation; request authorization for destructive operations, cost commitments or protected merges only.

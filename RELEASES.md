# Release Policy

## Versioning
Follow Semantic Versioning (SemVer). Stable releases use MAJOR.MINOR.PATCH:
- PATCH: backward-compatible bug fixes, security fixes and internal performance changes.
- MINOR: backward-compatible new features, tools, formats and workflows.
- MAJOR: incompatible changes to stable file formats, public plugin APIs, scripting APIs or supported integrations.

Before 1.0, the API and native file format are unstable; breaking changes may occur in 0.MINOR.0 but require explicit changelog entries and migration guidance where feasible. Pre-releases use `-alpha.N`, `-beta.N`, `-rc.N`. Do not promise stable document compatibility until 1.0.

## Cadence and triggers
- Patch: as needed; urgent security fixes expedited.
- Minor: tested feature milestones, normally 4–6 weeks after stabilization; not automatically per sprint.
- Major: only with justified breaking changes and a migration plan.
- Alpha: functional early builds for development feedback.
- Beta: feature-complete milestone with remaining stabilization work.
- Release candidate: final validation of the exact candidate artifact.
- No release merely because a sprint closes.

## Planned milestones (targets, not promises)
- v0.1.0-alpha.1: macOS desktop scaffold launches, Rust core validated.
- v0.2.0-alpha.1: interactive canvas, shapes, layers, undo/redo.
- v0.3.0-alpha.1: typography, vector editing and transforms.
- v0.4.0-alpha.1: reliable save/open and PNG/SVG/PDF export.
- v0.5.0-beta.1: components and reusable design systems.
- v0.6.0-beta.1: templates, brand kits and presentations.
- v1.0.0: stable product after acceptance, accessibility, reliability, security and compatibility gates.

## Release gates
1. Linked milestone issues closed or explicitly deferred; CHANGELOG.md updated.
2. CI green: Rust format/test, frontend typecheck/build, macOS Tauri compile and packaging.
3. Smoke test the actual DMG on supported macOS architecture(s); test launch, document create/edit/save/reopen/export where implemented.
4. No known release-blocking bugs; dependencies reviewed for vulnerabilities.
5. Confirm file format and plugin compatibility implications; document migration/backups if applicable.
6. Version synchronized in Rust crates, npm package and Tauri configuration.
7. Git annotated tag `vX.Y.Z[-channel.N]`, GitHub Release with notes and verified checksums.
8. Sign and notarize distributed macOS builds when credentials are configured. Until then clearly mark unsigned local test builds, and do not call them production-ready.

## Branches and hotfixes
`main` is the integration branch. Develop on short-lived feature branches and PRs. Release from a tested commit/tag. For a critical patch, branch from the latest stable tag, test, release, and merge the fix back into main. Never retag or silently replace a published release.

## Support and deprecation
Support the latest stable minor line with patches. Announce deprecated public APIs at least one minor release before removal where practical; removal normally requires the next major. Pre-1.0 exceptions must be documented.

## Release checklist
- [ ] Milestone acceptance and release notes
- [ ] CI and local macOS smoke tests
- [ ] Security/dependency review
- [ ] File-format compatibility and migrations
- [ ] Version bumps and changelog
- [ ] Installer checksums and signing status
- [ ] Tag and GitHub Release
- [ ] Post-release installation verification

## Known dependency advisories
Review [SECURITY.md](SECURITY.md) and all open Dependabot alerts before tagging. A macOS-only release may proceed after verifying a Linux-only dependency advisory is not in the macOS target graph; do not claim the Linux target is remediated.

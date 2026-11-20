# Contributing

1. Reference an issue with acceptance criteria.
2. Branch from main and keep changes focused.
3. Add tests and update documentation.
4. Run `cargo fmt --all --check`, `cargo test -p design-document`, and frontend checks.
5. Open a PR with issue link, summary, tests and UI screenshots when relevant.
6. Merge only after review and passing CI; delete merged branches.

Definition of Done: acceptance criteria met, tests pass, docs current, no secrets, PR reviewed.

## Development loop and repository standards

Use the Build → Deploy → Test → Fix → Redeploy → Continue loop. Reproduce failures before changing code; verify the failing workflow afterward. Review the central [repository standards](https://github.com/drakeg/madmallard-repository-standards/blob/main/ADOPTION.md) for voluntary updates without replacing this project's own configuration. Validate README badges against tracked manifests and workflow names on technology changes. Preserve the existing Vercel preview and native macOS build paths. Include test results, deployment status, and remaining risks in each PR; never claim tests that were not run. Prioritize the end-to-end SMB editing workflow described in [PRODUCT.md](PRODUCT.md).

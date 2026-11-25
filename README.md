# Mad Mallard Design Studio

[![License](https://img.shields.io/github/license/drakeg/madmallard-design-studio)](https://github.com/drakeg/madmallard-design-studio/blob/main/LICENSE)


[![Rust](https://img.shields.io/badge/Rust-Core-000000?logo=rust&logoColor=white)](Cargo.toml) [![TypeScript](https://img.shields.io/badge/TypeScript-Frontend-3178C6?logo=typescript&logoColor=white)](apps/desktop/tsconfig.json) [![Svelte 5](https://img.shields.io/badge/Svelte-5-FF3E00?logo=svelte&logoColor=white)](apps/desktop/package.json) [![Tauri 2](https://img.shields.io/badge/Tauri-2-24C8DB?logo=tauri&logoColor=white)](apps/desktop/src-tauri/Cargo.toml) [![Vite 8](https://img.shields.io/badge/Vite-8-646CFF?logo=vite&logoColor=white)](apps/desktop/package.json) [![Vercel](https://img.shields.io/badge/Vercel-Web-000000?logo=vercel&logoColor=white)](https://desktop-sigma-tawny.vercel.app/)

[![CI](https://github.com/drakeg/madmallard-design-studio/actions/workflows/ci.yml/badge.svg)](https://github.com/drakeg/madmallard-design-studio/actions/workflows/ci.yml) [![Open issues](https://img.shields.io/github/issues/drakeg/madmallard-design-studio)](https://github.com/drakeg/madmallard-design-studio/issues) [![Open PRs](https://img.shields.io/github/issues-pr/drakeg/madmallard-design-studio)](https://github.com/drakeg/madmallard-design-studio/pulls)

Local-first Rust + Tauri 2 + Svelte 5 desktop design editor. Sprint 0 UI is a static preview, not yet an interactive editor.

## Development

Install Rust stable and Node.js LTS. Run `cd apps/desktop && npm install && npm run tauri dev`.

## Tests

`cargo test -p design-document`; `cd apps/desktop && npm run check && npm run build`.

See [SPRINTS.md](SPRINTS.md), [BACKLOG.md](BACKLOG.md), [ARCHITECTURE.md](ARCHITECTURE.md).

## Releases

See [RELEASES.md](RELEASES.md) for SemVer, release cadence, milestones and quality gates; see [CHANGELOG.md](CHANGELOG.md) for changes.

## Product direction

See [PRODUCT.md](PRODUCT.md) for the SMB buyer hypothesis, minimum viable workflow and validation criteria. Web preview: https://desktop-sigma-tawny.vercel.app/. Native macOS packages require separate validation and signing status before public distribution.

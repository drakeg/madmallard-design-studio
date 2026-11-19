# Security and Dependency Review

Last reviewed: 2026-11-19

## GHSA-wrw7-89jp-8q8g / RUSTSEC-2024-0429

**Status:** Open — upstream compatibility blocked. Track in [issue #8](https://github.com/drakeg/madmallard-design-studio/issues/8) and [Dependabot alert #1](https://github.com/drakeg/madmallard-design-studio/security/dependabot/1).

**Affected:** `glib 0.18.5` in `Cargo.lock`, severity moderate; affected range >= 0.15.0 and < 0.20.0. Patched in >= 0.20.0. The affected `VariantStrIter` implementation can cause undefined behavior and null-pointer crashes.

**Verified target-specific dependency graph:**
- `cargo tree -i glib --target aarch64-apple-darwin`: no matching dependency.
- `cargo tree -i glib --target x86_64-unknown-linux-gnu`: `glib 0.18.5` via GTK 0.18/WebKitGTK/Tauri 2.
- macOS application is currently the only planned release target; no identified macOS exposure from this advisory.
- Linux remains affected. No claim that Linux is secure or unaffected.

**Decision:** Keep the GitHub alert OPEN. Do not force `glib 0.20` into GTK 0.18 dependencies; incompatible version requirements mean a lockfile-only update cannot fix this. Do not silence audits. Follow Tauri's upstream GTK migration and update when compatible versions exist. Do not ship Linux release until assessed and remediated.

**Review triggers:** dependency upgrades, before every release, and before introducing Linux builds. See issue #8 for acceptance criteria.

References:
- https://github.com/advisories/GHSA-wrw7-89jp-8q8g
- https://rustsec.org/advisories/RUSTSEC-2024-0429.html
- https://github.com/tauri-apps/tauri/issues/12048

## General policy
- Review Dependabot and dependency updates each sprint and before release.
- Do not dismiss or suppress a vulnerability without written impact analysis and compensating controls.
- Track unresolved upstream vulnerabilities in GitHub issues with owner, exposure and resolution criteria.

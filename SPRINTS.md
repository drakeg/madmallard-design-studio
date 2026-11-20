# Sprint Plan

Cadence: two-week increments; each sprint has acceptance criteria, tests, demo and review.

## Sprint 0 — Foundation
Rust workspace, Tauri 2 + Svelte 5 desktop scaffold, versioned document model, CI, contributing guidelines, architecture decision record. Done when tests pass and macOS application launches.

## Sprint 1 — Interactive Canvas
Pan, zoom, selection, rectangles, ellipses, layers, property inspector and undo/redo. Done when editable shapes work end to end.

## Sprint 2 — Vector and Typography
Text, SVG paths, transforms, snapping, alignment and font rendering benchmarks.

## Sprint 3 — Files and Export
Native project save/open, autosave/recovery, PNG/SVG/PDF exports.

## Sprint 4 — Design Systems
Reusable components, variants, shared styles, constraints, auto layout.

## Sprint 5 — Templates and Presentations
Brand kits, preset dimensions, template gallery and slide decks.

## Review
Close each sprint by verifying acceptance criteria, demonstrating the increment, recording deferred work and reprioritizing issues.

Release policy: see [RELEASES.md](RELEASES.md). A sprint closing does not automatically trigger a release.

## Standards adoption and commercialization (Sprint 0 carryover)

- Adopt central standards without overwriting project-specific instructions; validate actual CI and README claims.
- Keep a working Vercel web preview and separately validate native macOS app packaging.
- Record target SMB buyer, MVP acceptance and pricing hypotheses in PRODUCT.md.
- Sprint 1 remains the current delivery sprint: canvas creation, selection, movement, inspector, undo/redo. Do not reset already completed foundation work.

Sprint 0 maintenance: verify README badges against manifests and CI, document badge conventions in AGENTS.md, and enforce checks in CI.

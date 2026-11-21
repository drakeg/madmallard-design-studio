# Prioritized Backlog

| Priority | Sprint | Work | Acceptance |
|---|---|---|---|
| P0 | 0 | Desktop scaffold | macOS Tauri app starts |
| P0 | 0 | Rust document core | JSON round-trip tests pass |
| P0 | 0 | CI | Rust and Svelte checks pass on PR |
| P0 | 1 | Interactive canvas | Create/select/move shapes and pan/zoom |
| P0 | 1 | Command stack | Undo/redo tested |
| P0 | 2 | Text/vector | Editable text and SVG paths |
| P0 | 3 | Save/open | Round-trip without data loss |
| P1 | 3 | Export | PNG/SVG/PDF |
| P1 | 4 | Components | Reusable instances |
| P1 | 5 | Templates | Brand and slide presets |
| P2 | Future | AI editing | Previewable, undoable commands |
| P2 | Future | Plugins | Versioned sandboxed API |
| P0 | 0 carryover | Repair failed dependency automation | All required CI and Vercel checks green |
| P0 | 1 | End-to-end web and desktop canvas | Select, move, undo/redo and inspector verified in both builds |
| P0 | 1–3 | SMB MVP vertical slice | Create/edit/save/reopen/export without losing data |
| P1 | 1 | Commercial validation | Five observed SMB trials and documented pricing feedback, no invented evidence |
| P1 | 0 carryover | Adopt centralized repository standards | Preserve project docs; reconcile badge generator with nested manifests |

Dependency compatibility: TypeScript 7 is blocked by current svelte-check peer support (^5 or ^6); retain TypeScript 5 until a tested compatible upgrade is available.

Sprint 1 implementation slice: rectangle/ellipse creation, selection, property inspector, layer list and keyboard movement; pan, drag, undo/redo remain outstanding.

Sprint 1 follow-up: pointer-based shape dragging implemented; verify drag behavior in browser and macOS, then add undo/redo and pan.
| P1 | 0 | Repository badge maintenance | Accurate README badges, documented standards, automated validation |

Sprint 1 progress: undo/redo history (100 checkpoints) for shape creation, dragging, arrow nudges, deletion and inspector edits. Next: pan gestures, durable project persistence, and browser interaction regression tests.

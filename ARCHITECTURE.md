# Architecture

Rust core owns versioned scene graph, geometry, serialization and future undoable commands. Tauri 2 exposes narrow native commands. Svelte 5 renders the desktop editor UI. Local-first files and assets by default. Evaluate SVG/Canvas and wgpu/Vello rendering before committing. AI changes must be previewable and undoable. macOS first, cross-platform abstractions retained.

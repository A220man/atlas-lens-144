# Changelog

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Completed This Round

- **Vue/Volar LSP Plugin** (addresses issue #232): Added `vue-volar` plugin with `@vue/language-server` configuration

### Previously Completed

- **Project Setup & Core Infrastructure**: FastAPI backend, React frontend, Docker compose, JSON Schema validation
- **Marketplace Core**: Plugin directory with search, filter by category
- **Plugin Detail View**: Installation instructions, LSP/MCP config display, source links
- **LSP Plugin Configuration Fix** (fixes issue #379): All 12 LSP plugins now include `.lsp.json` files with proper configuration

### Addressed Upstream Issues

- #232: Added Vue/Volar LSP plugin
- #379: Fixed missing `.lsp.json` files for all LSP plugins
- #587: Added JSON Schema validation for marketplace.json
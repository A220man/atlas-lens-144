# Changelog

## 1.5.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.4.1 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Completed This Round

- **Enhanced schema validation** (backend/app/main.py): Added category-aware validation ensuring LSP plugins have `lspServers` config and MCP plugins have `mcpServers` config. Prevents runtime failures from misconfigured plugins.

## 1.4.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

### Completed This Round

- **MCP Plugin Support** (addresses issues #283, #783): Added `github-mcp` and `discord-mcp` plugins with MCP server configurations

### Previously Completed

- **Project Setup & Core Infrastructure**: FastAPI backend, React frontend, Docker compose, JSON Schema validation
- **Marketplace Core**: Plugin directory with search, filter by category
- **Plugin Detail View**: Installation instructions, LSP/MCP config display, source links
- **LSP Plugin Configuration Fix** (fixes issue #379): All 12 LSP plugins now include `.lsp.json` files with proper configuration
- **Vue/Volar LSP Plugin** (addresses issue #232): Added `vue-volar` plugin with `@vue/language-server` configuration

### Addressed Upstream Issues

- #232: Added Vue/Volar LSP plugin
- #283: Added GitHub MCP plugin
- #379: Fixed missing `.lsp.json` files for all LSP plugins
- #587: Added JSON Schema validation for marketplace.json
- #783: Added Discord MCP plugin
- #379 (supplement): Enhanced schema validation to catch category mismatches between plugin type and server configuration

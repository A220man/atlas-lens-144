# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

project-setup

## Roadmap

### project-setup — Project Setup & Core Infrastructure

Status: done

Acceptance:
- FastAPI backend with basic health endpoint
- React frontend with plugin listing page
- Docker compose for local development
- Marketplace JSON schema validation

Implementation: `backend/app/main.py`, `backend/requirements.txt`, `backend/Dockerfile`, `frontend/package.json`, `frontend/src/App.tsx`, `frontend/src/PluginList.tsx`, `frontend/src/PluginDetail.tsx`, `frontend/src/types.ts`, `frontend/vite.config.ts`, `docker-compose.yml`

Tests: `backend/tests/test_main.py::test_health_endpoint`, `backend/tests/test_main.py::test_validate_marketplace_schema`

### marketplace-core — Marketplace Core - Plugin Directory

Status: done

Acceptance:
- Load plugins from marketplace.json
- Display plugin list with name, description, author
- Filter by category (LSP, MCP, etc.)
- Search by name/description

Implementation: `backend/app/main.py`, `frontend/src/App.tsx`, `frontend/src/PluginList.tsx`, `marketplace.json`

Tests: `backend/tests/test_main.py::test_list_plugins`, `backend/tests/test_main.py::test_get_plugin`, `backend/tests/test_main.py::test_get_nonexistent_plugin`

### plugin-detail — Plugin Detail View

Status: done

Acceptance:
- Click plugin to view details
- Show installation instructions
- Display LSP/MCP configuration
- Show source repository link

Implementation: `frontend/src/PluginDetail.tsx`, `frontend/src/App.tsx`

### lsp-plugin-support — LSP Plugin Configuration Fix

Status: done

Acceptance:
- Generate .lsp.json files for each LSP plugin
- Validate marketplace.json lspServers config
- Fix issue #379 - missing LSP configuration

Implementation: `plugins/*/.lsp.json (12 files)`, `plugins/*/README.md (12 files)`, `marketplace.json`, `backend/tests/test_main.py::test_all_lsp_plugins_have_lsp_config`

Tests: `backend/tests/test_main.py::test_all_lsp_plugins_have_lsp_config`

### vue-volar-lsp — Add Vue/Volar LSP Plugin

Status: done

Acceptance:
- Add vue-volar plugin entry in marketplace.json
- Create plugin directory with .lsp.json
- Reference @vue/language-server configuration
- Address issue #232

Implementation: `plugins/vue-volar/.lsp.json`, `plugins/vue-volar/README.md`, `marketplace.json`, `backend/tests/test_main.py::test_marketplace_has_vue_volar`

Tests: `backend/tests/test_main.py::test_marketplace_has_vue_volar`


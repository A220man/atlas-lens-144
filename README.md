# atlas-lens-144 — Ryan Vo

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Official, Anthropic-managed directory of high-quality Claude Code Plugins.

## Features

- **Plugin Marketplace**: Browse and search official Claude Code plugins
- **LSP Support**: TypeScript, Python, Go, Rust, C/C++, PHP, Swift, Kotlin, C#, Java, Lua, and Vue.js
- **Vue/Volar LSP**: Full Vue 3 support via `@vue/language-server` (issue #232)
- **Fixed LSP Config**: All LSP plugins include `.lsp.json` files (fixes issue #379)
- **Schema Validation**: JSON Schema validation for marketplace.json

## Quick Start

### Using Docker Compose (Recommended)

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Manual Development

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
atlas-lens-144/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   └── main.py         # API endpoints
│   ├── tests/              # Pytest tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/               # React + TypeScript + Vite
│   ├── src/
│   │   ├── App.tsx         # Main app component
│   │   ├── PluginList.tsx  # Plugin listing
│   │   ├── PluginDetail.tsx # Plugin detail view
│   │   └── types.ts        # TypeScript types
│   ├── package.json
│   └── Dockerfile
├── plugins/                # Plugin directories with .lsp.json
│   ├── typescript-lsp/
│   ├── pyright-lsp/
│   ├── gopls-lsp/
│   ├── rust-analyzer-lsp/
│   ├── clangd-lsp/
│   ├── php-lsp/
│   ├── swift-lsp/
│   ├── kotlin-lsp/
│   ├── csharp-lsp/
│   ├── jdtls-lsp/
│   ├── lua-lsp/
│   └── vue-volar/          # New Vue/Volar LSP (issue #232)
├── marketplace.json        # Plugin catalog (source of truth)
├── docker-compose.yml
└── README.md
```

## API Endpoints

- `GET /health` - Health check
- `GET /api/plugins` - List all plugins
- `GET /api/plugins/{name}` - Get plugin by name
- `POST /api/validate` - Validate marketplace.json against schema

## Addressed Issues

- **#232**: Added Vue/Volar LSP plugin (`vue-volar`) with `@vue/language-server` configuration
- **#379**: Fixed missing `.lsp.json` files for all LSP plugins - each plugin directory now contains proper LSP configuration
- **#587**: Added JSON Schema validation for marketplace.json

## Plugin Installation

To install a plugin in Claude Code:

```bash
claude plugins install <plugin-name>@claude-plugins-official
```

Example for Vue/Volar:
```bash
claude plugins install vue-volar@claude-plugins-official
```

## Development

### Running Tests

```bash
cd backend
pytest tests/ -v
```

### Adding a New Plugin

1. Add plugin entry to `marketplace.json`
2. Create directory under `plugins/<plugin-name>/`
3. Add `.lsp.json` (for LSP plugins) or `.mcp.json` (for MCP plugins)
4. Add `README.md` with installation instructions

## License

Apache-2.0

Maintainer: Ryan Vo <ryandtvo@gmail.com>

"""
FastAPI application for atlas-lens-144 marketplace.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json
from jsonschema import validate, ValidationError

app = FastAPI(title="atlas-lens-144 Marketplace API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JSON Schema for marketplace.json
MARKETPLACE_SCHEMA = {
    "type": "object",
    "required": ["plugins"],
    "properties": {
        "plugins": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["name", "description", "author", "source"],
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "author": {"type": "string"},
                    "source": {"type": "string"},
                    "category": {"type": "string", "enum": ["lsp", "mcp", "tool", "other"]},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "lspServers": {"type": "object"},
                    "mcpServers": {"type": "object"},
                },
            },
        }
    },
}

# Marketplace file is at project root
MARKETPLACE_PATH = Path(__file__).parent.parent.parent / "marketplace.json"

def validate_marketplace(path: Path):
    """Validate marketplace.json file against schema."""
    with open(path) as f:
        data = json.load(f)
    validate(instance=data, schema=MARKETPLACE_SCHEMA)
    return data

@app.get("/health")
async def health():
    return {"status": "ok", "service": "atlas-lens-144"}

@app.get("/api/plugins")
async def list_plugins():
    """List all plugins from marketplace.json."""
    data = validate_marketplace(MARKETPLACE_PATH)
    return data["plugins"]

@app.get("/api/plugins/{name}")
async def get_plugin(name: str):
    """Get a specific plugin by name."""
    data = validate_marketplace(MARKETPLACE_PATH)
    for plugin in data["plugins"]:
        if plugin["name"] == name:
            return plugin
    raise HTTPException(status_code=404, detail="Plugin not found")

@app.post("/api/validate")
async def validate_marketplace_endpoint(file_path: str = "marketplace.json"):
    """Validate marketplace.json file against schema."""
    path = Path(file_path)
    if not path.is_absolute():
        # If relative, look in project root
        path = Path(__file__).parent.parent.parent / file_path
    if not path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        validate_marketplace(path)
        return {"valid": True, "message": "Marketplace file is valid"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

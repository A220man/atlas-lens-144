import pytest
from fastapi.testclient import TestClient
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app, validate_marketplace, MARKETPLACE_SCHEMA

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "atlas-lens-144"}

def test_validate_marketplace_schema():
    # Create a minimal valid marketplace.json for testing
    test_data = {
        "plugins": [
            {
                "name": "test-plugin",
                "description": "Test plugin",
                "author": "Test Author",
                "source": "https://example.com",
                "category": "lsp",
                "tags": ["test"],
                "lspServers": {}
            }
        ]
    }
    # Write to temp file and validate
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_data, f)
        temp_path = Path(f.name)
    
    try:
        result = validate_marketplace(temp_path)
        assert result == test_data
    finally:
        temp_path.unlink()

def test_list_plugins():
    response = client.get("/api/plugins")
    assert response.status_code == 200
    plugins = response.json()
    assert isinstance(plugins, list)
    assert len(plugins) > 0
    # Check first plugin has required fields
    plugin = plugins[0]
    assert "name" in plugin
    assert "description" in plugin
    assert "author" in plugin
    assert "source" in plugin
    assert "category" in plugin

def test_get_plugin():
    # First get list to find a valid name
    response = client.get("/api/plugins")
    plugins = response.json()
    if plugins:
        name = plugins[0]["name"]
        response = client.get(f"/api/plugins/{name}")
        assert response.status_code == 200
        plugin = response.json()
        assert plugin["name"] == name

def test_get_nonexistent_plugin():
    response = client.get("/api/plugins/nonexistent-plugin-xyz")
    assert response.status_code == 404

def test_validate_endpoint():
    response = client.post("/api/validate", json={"file_path": "marketplace.json"})
    # Should either succeed (200) or fail with validation error (400)
    assert response.status_code in (200, 400)

def test_marketplace_has_vue_volar():
    """Test that vue-volar plugin exists (issue #232)"""
    response = client.get("/api/plugins")
    plugins = response.json()
    vue_plugin = next((p for p in plugins if p["name"] == "vue-volar"), None)
    assert vue_plugin is not None, "vue-volar plugin not found"
    assert vue_plugin["category"] == "lsp"
    assert "vue" in vue_plugin["tags"]
    assert "volar" in vue_plugin["tags"]
    assert "lspServers" in vue_plugin
    assert "vue" in vue_plugin["lspServers"]

def test_all_lsp_plugins_have_lsp_config():
    """Test that all LSP plugins have lspServers config (issue #379)"""
    response = client.get("/api/plugins")
    plugins = response.json()
    lsp_plugins = [p for p in plugins if p["category"] == "lsp"]
    assert len(lsp_plugins) >= 12, f"Expected at least 12 LSP plugins, got {len(lsp_plugins)}"
    for plugin in lsp_plugins:
        assert "lspServers" in plugin, f"Plugin {plugin['name']} missing lspServers"
        assert len(plugin["lspServers"]) > 0, f"Plugin {plugin['name']} has empty lspServers"

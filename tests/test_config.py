import pytest
from importlib import reload
import os

def test_valid_rpc_config(monkeypatch):
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock")
    monkeypatch.setenv("RPC_LOG_PATH", "/mock.log")
    reload_config()
    from exporter.config import config
    assert config.role == "rpc"

def test_invalid_role(monkeypatch):
    monkeypatch.setenv("ROLE", "invalid")
    with pytest.raises(ValueError):
        reload_config()

def reload_config():
    import exporter.config
    reload(exporter.config)

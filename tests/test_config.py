import os
import pytest

def test_invalid_role(monkeypatch):
    monkeypatch.setenv("ROLE", "invalid")
    with pytest.raises(ValueError):
        from exporter.config import Config
        Config()

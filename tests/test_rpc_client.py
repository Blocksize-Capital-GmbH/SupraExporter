from unittest.mock import patch
import pytest

@patch("requests.get")
def test_get_block_height_success(mock_get, monkeypatch):
    monkeypatch.setenv("RPC_URL", "http://mock-rpc")
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")

    from importlib import reload
    import exporter.config
    reload(exporter.config)  # reload to apply monkeypatched env
    from exporter.clients.rpc_client import get_block_height

    mock_get.return_value.json.return_value = {"height": 12345}
    mock_get.return_value.raise_for_status.return_value = None

    assert get_block_height() == 12345

@patch("requests.get", side_effect=Exception("fail"))
def test_get_block_height_fail(mock_get, monkeypatch):
    monkeypatch.setenv("RPC_URL", "http://mock-rpc")
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")

    from importlib import reload
    import exporter.config
    reload(exporter.config)
    from exporter.clients.rpc_client import get_block_height

    assert get_block_height() == 0

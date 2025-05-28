from importlib import reload
from unittest.mock import patch

from supraexporter.collectors.rpc_collector import RpcCollector


@patch("requests.get")
def test_get_block_height_success(mock_get, monkeypatch):
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc.com")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")

    # Reload config first
    import supraexporter.config

    reload(supraexporter.config)

    # Reload rpc_client after config is ready
    import supraexporter.clients.rpc_client

    reload(supraexporter.clients.rpc_client)
    from supraexporter.clients.rpc_client import get_block_height

    mock_get.return_value.json.return_value = {"height": 12345}
    mock_get.return_value.raise_for_status.return_value = None

    assert get_block_height() == 12345


@patch("supraexporter.collectors.rpc_collector.get_block_height", return_value=100)
@patch("supraexporter.collectors.rpc_collector.get_public_block_height", return_value=115)
def test_rpc_collector_unhealthy(mock_pub, mock_local):
    collector = RpcCollector()
    metrics = {m.name: m.samples[0].value for m in collector.collect()}
    assert metrics["supra_rpc_health"] == 0.0


@patch("supraexporter.collectors.rpc_collector.get_block_height", return_value=0)
@patch("supraexporter.collectors.rpc_collector.get_public_block_height", return_value=120)
def test_rpc_collector_local_none(mock_pub, mock_local):
    collector = RpcCollector()
    metrics = {m.name: m.samples[0].value for m in collector.collect()}
    assert metrics["supra_rpc_health"] == 0.0

from unittest.mock import patch
from exporter.collectors.rpc_collector import RpcCollector

@patch("exporter.collectors.rpc_collector.get_block_height", return_value=120)
@patch("exporter.collectors.rpc_collector.get_public_block_height", return_value=123)
def test_rpc_collector_healthy(mock_public, mock_local):
    collector = RpcCollector()
    metrics = list(collector.collect())
    values = {m.name: m.samples[0].value for m in metrics}
    assert values["supra_rpc_block_height"] == 120
    assert values["supra_rpc_health"] == 1.0

@patch("exporter.collectors.rpc_collector.get_block_height", return_value=100)
@patch("exporter.collectors.rpc_collector.get_public_block_height", return_value=123)
def test_rpc_collector_unhealthy(mock_public, mock_local):
    collector = RpcCollector()
    metrics = list(collector.collect())
    values = {m.name: m.samples[0].value for m in metrics}
    assert values["supra_rpc_health"] == 0.0

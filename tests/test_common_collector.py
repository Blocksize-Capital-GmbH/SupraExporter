from unittest.mock import patch
from exporter.collectors.common_collector import CommonCollector

@patch("exporter.collectors.common_collector.get_public_block_height", return_value=12345)
@patch("exporter.collectors.common_collector.public_block_state", autospec=True)
def test_common_collector_success(mock_state, mock_get_height):
    collector = CommonCollector()
    metrics = list(collector.collect())
    assert len(metrics) == 1
    assert metrics[0].name == "supra_public_rpc_block_height"
    assert metrics[0].samples[0].value == 12345

@patch("exporter.collectors.common_collector.get_public_block_height", side_effect=Exception("fail"))
def test_common_collector_failure(mock_get_height):
    collector = CommonCollector()
    metrics = list(collector.collect())
    assert metrics == []  # no metrics emitted on error

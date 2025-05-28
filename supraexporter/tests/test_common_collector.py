from unittest.mock import patch

from supraexporter.collectors.common_collector import CommonCollector


@patch("supraexporter.collectors.common_collector.get_public_block_height", return_value=12345)
@patch("supraexporter.collectors.common_collector.public_block_state", autospec=True)
def test_common_collector_success(mock_state, mock_height):
    metrics = list(CommonCollector().collect())
    assert metrics[0].name == "supra_public_rpc_block_height"
    assert metrics[0].samples[0].value == 12345


@patch(
    "supraexporter.collectors.common_collector.get_public_block_height",
    side_effect=Exception("fail"),
)
def test_common_collector_failure(_mock):
    assert list(CommonCollector().collect()) == []

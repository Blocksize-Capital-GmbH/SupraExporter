from unittest.mock import patch
from exporter.collectors.validator_collector import ValidatorCollector

@patch("exporter.collectors.validator_collector.read_last_n_lines", return_value="""
    Block height: (110)
    Block xyz PUBKEY
    View abc PUBKEY
""")
@patch("exporter.collectors.validator_collector.get_public_block_height", return_value=115)
@patch("exporter.collectors.validator_collector.config.network_pubkey", "PUBKEY")
def test_validator_collector_success(mock_log, mock_pub, _pubkey):
    collector = ValidatorCollector()
    metrics = list(collector.collect())
    values = {m.name: m.samples[0].value for m in metrics}
    assert values["supra_validator_block_height"] == 110
    assert values["supra_validator_health"] == 1.0
    assert values["supra_block_relative_abundance"] > 0
    assert values["supra_view_relative_abundance"] > 0

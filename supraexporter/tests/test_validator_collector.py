from unittest.mock import patch

from supraexporter.collectors.validator_collector import ValidatorCollector


@patch("supraexporter.collectors.validator_collector.read_last_n_lines")
@patch("supraexporter.collectors.validator_collector.get_public_block_height", return_value=115)
@patch("supraexporter.collectors.validator_collector.config", autospec=True)
def test_validator_collector_metrics(
    mock_config,
    mock_public,
    mock_read,
    mock_env_validator,
    dummy_log,
):
    mock_read.return_value = dummy_log
    mock_config.network_pubkey = "PUBKEY"
    mock_config.validator_log_path = "/tmp/mock"

    collector = ValidatorCollector()
    metrics = {m.name: m.samples[0].value for m in collector.collect()}

    assert metrics["supra_validator_block_height"] == 110
    assert metrics["supra_validator_health"] == 1.0
    assert metrics["supra_block_relative_abundance"] > 0.0
    assert metrics["supra_view_relative_abundance"] > 0.0


@patch("supraexporter.collectors.validator_collector.read_last_n_lines", return_value="")
@patch("supraexporter.collectors.validator_collector.get_public_block_height", return_value=0)
@patch("supraexporter.collectors.validator_collector.config", autospec=True)
def test_validator_collector_unhealthy(mock_config, _mock_pub, _mock_log):
    mock_config.network_pubkey = "PUBKEY"
    mock_config.validator_log_path = "/dev/null"

    from supraexporter.collectors.validator_collector import ValidatorCollector

    metrics = {m.name: m.samples[0].value for m in ValidatorCollector().collect()}
    assert metrics["supra_validator_health"] == 0.0

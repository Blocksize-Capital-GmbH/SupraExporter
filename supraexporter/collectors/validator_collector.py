from prometheus_client.core import GaugeMetricFamily
from prometheus_client.registry import Collector

from supraexporter.clients.log_reader import (
    calculate_keyword_abundance,
    parse_block_height,
    read_last_n_lines,
)
from supraexporter.config import config
from supraexporter.utils.public_rpc import get_public_block_height


class ValidatorCollector(Collector):
    def collect(self):
        try:
            assert config.validator_log_path is not None  # nosec
            log_data = read_last_n_lines(config.validator_log_path)

            validator_height = parse_block_height(log_data)
            if not config.network_pubkey:
                raise ValueError("Missing NETWORK_PUBKEY")

            block_abundance = calculate_keyword_abundance(log_data, "Block", config.network_pubkey)
            view_abundance = calculate_keyword_abundance(log_data, "View", config.network_pubkey)

            yield GaugeMetricFamily(
                "supra_validator_block_height",
                "Block height parsed from validator logs",
                value=validator_height or 0,
            )
            yield GaugeMetricFamily(
                "supra_block_relative_abundance",
                "Proportion of 'Block' log lines with validator pubkey",
                value=block_abundance or 0,
            )
            yield GaugeMetricFamily(
                "supra_view_relative_abundance",
                "Proportion of 'View' log lines with validator pubkey",
                value=view_abundance or 0,
            )

            public_height = get_public_block_height()
            healthy = (
                1.0
                if validator_height
                and public_height
                and abs(validator_height - public_height) <= 10
                else 0.0
            )
            yield GaugeMetricFamily(
                "supra_validator_health",
                "1 if validator height is within 10 blocks of public RPC height",
                value=healthy,
            )

        except Exception as e:
            print(f"[ERROR] Validator collector failed: {e}")

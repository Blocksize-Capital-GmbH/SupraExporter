"""Collector for local RPC metrics including block height and health."""

from prometheus_client.core import GaugeMetricFamily
from prometheus_client.registry import Collector

from supraexporter.clients.rpc_client import get_block_height
from supraexporter.utils.public_rpc import get_public_block_height


class RpcCollector(Collector):
    """Prometheus collector for local RPC block height and health metrics."""

    def collect(self):
        """Collect local RPC block height and health metrics."""
        local_height = get_block_height()
        public_height = get_public_block_height()  # Fetch fresh for health only

        yield GaugeMetricFamily(
            "supra_rpc_block_height",
            "Block height from local Supra RPC",
            value=local_height,
        )

        healthy = 1.0 if public_height and abs(local_height - public_height) <= 10 else 0.0
        yield GaugeMetricFamily(
            "supra_rpc_health",
            "1 if RPC is within 10 blocks of public RPC",
            value=healthy,
        )

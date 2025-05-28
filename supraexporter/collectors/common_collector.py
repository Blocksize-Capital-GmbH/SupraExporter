from prometheus_client.core import GaugeMetricFamily
from prometheus_client.registry import Collector

from supraexporter.utils import public_block_state
from supraexporter.utils.public_rpc import get_public_block_height


class CommonCollector(Collector):
    def collect(self):
        try:
            height = get_public_block_height()
            public_block_state.public_block_height = height

            yield GaugeMetricFamily(
                "supra_public_rpc_block_height",
                "Block height from the public Supra RPC",
                value=height or 0,
            )
        except Exception as e:
            print(f"[ERROR] Failed to collect public RPC height: {e}")

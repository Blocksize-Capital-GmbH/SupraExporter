"""Public RPC client for fetching block height from the public RPC endpoint."""

import logging

import requests

from supraexporter.config import config

logger = logging.getLogger(__name__)


def get_public_block_height():
    """Fetch the latest block height from the public RPC endpoint."""
    try:
        base_url = config.public_rpc_url.rstrip("/")
        url = f"{base_url}/block"
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()
        data = resp.json()
        return int(data["height"])
    except Exception as e:
        logger.warning(f"Failed to fetch public RPC block height: {e}")
        return 0

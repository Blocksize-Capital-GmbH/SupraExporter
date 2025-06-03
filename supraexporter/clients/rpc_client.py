"""RPC client for fetching block heights from local Supra RPC endpoint."""

import requests

from supraexporter.config import config


def get_block_height():
    """Fetch the latest block height from the local RPC endpoint."""
    try:
        # Ensure correct URL: append '/block' to the base RPC URL
        base_url = (config.rpc_url or "").rstrip("/")
        url = f"{base_url}/block"

        response = requests.get(url, timeout=3)
        response.raise_for_status()

        data = response.json()
        return int(data["height"])
    except Exception as e:
        print(f"[ERROR] Failed to get local RPC block height from {config.rpc_url}: {e}")
        return 0

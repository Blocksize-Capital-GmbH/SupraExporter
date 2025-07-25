"""Application configuration loaded from environment variables."""

import os

from dotenv import load_dotenv

# Load .env from the project root
load_dotenv()

VALID_ROLES = {"rpc", "validator", "both"}


class Config:
    """Application configuration loaded from environment variables."""

    def __init__(self):
        """Initialize and validate the exporter configuration."""
        self.role = os.getenv("ROLE", "both").lower()
        if self.role not in VALID_ROLES:
            raise ValueError(f"Invalid ROLE '{self.role}'. Must be one of {VALID_ROLES}.")

        # Common
        self.port = int(os.getenv("EXPORTER_PORT", 9100))
        self.poll_interval = int(os.getenv("POLL_INTERVAL", 10))
        self.public_rpc_url = os.getenv("PUBLIC_RPC_URL", "https://rpc-testnet.supra.com/rpc/v1")

        # RPC node config (used in 'rpc' or 'both')
        self.rpc_url = os.getenv("RPC_URL")
        self.rpc_log_path = os.getenv("RPC_LOG_PATH")

        # Validator node config (used in 'validator' or 'both')
        self.validator_rpc_url = os.getenv("VALIDATOR_RPC_URL")
        self.validator_log_path = os.getenv("VALIDATOR_LOG_PATH")
        self.network_pubkey = os.getenv("NETWORK_PUBKEY")

        self._validate()

    def _validate(self):
        if self.role in ("rpc", "both"):
            if not self.rpc_url:
                raise ValueError("Missing RPC_URL for 'rpc' role.")
            if not self.rpc_log_path:
                raise ValueError("Missing RPC_LOG_PATH for 'rpc' role.")

        if self.role in ("validator", "both"):
            if not self.validator_log_path:
                raise ValueError("Missing VALIDATOR_LOG_PATH for 'validator' role.")
            if not self.network_pubkey:
                raise ValueError("Missing NETWORK_PUBKEY for 'validator' role.")


# Create a global config instance
config = Config()

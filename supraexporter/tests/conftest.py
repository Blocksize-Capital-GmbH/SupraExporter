"""Pytest fixtures for configuring environment and dummy validator logs."""

import os

import pytest

# Set default environment variables before any imports
os.environ["ROLE"] = "rpc"
os.environ["RPC_URL"] = "http://mock-rpc.com"
os.environ["RPC_LOG_PATH"] = "/tmp/mock.log"
os.environ["PORT"] = "7896"
os.environ["VALIDATOR_LOG_PATH"] = "/tmp/val.log"
os.environ["NETWORK_PUBKEY"] = "PUBKEY"

# Create test log files if they don't exist
os.makedirs("/tmp", exist_ok=True)
for log_path in ["/tmp/mock.log", "/tmp/val.log"]:
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("")


@pytest.fixture()
def mock_env_rpc(monkeypatch):
    """Fixture to set environment variables for RPC tests."""
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc.com")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")


@pytest.fixture()
def mock_env_validator(monkeypatch):
    """Fixture to set environment variables for validator tests."""
    monkeypatch.setenv("ROLE", "validator")
    monkeypatch.setenv("VALIDATOR_LOG_PATH", "/tmp/val.log")
    monkeypatch.setenv("NETWORK_PUBKEY", "PUBKEY")


@pytest.fixture()
def dummy_log():
    """Provide a dummy validator log snippet for tests."""
    return """
    Block height: (110)
    Block xyz PUBKEY
    View abc PUBKEY
    """

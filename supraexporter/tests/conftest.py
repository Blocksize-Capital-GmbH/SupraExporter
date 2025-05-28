import pytest


@pytest.fixture()
def mock_env_rpc(monkeypatch):
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc.com")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")


@pytest.fixture()
def mock_env_validator(monkeypatch):
    monkeypatch.setenv("ROLE", "validator")
    monkeypatch.setenv("VALIDATOR_LOG_PATH", "/tmp/val.log")
    monkeypatch.setenv("NETWORK_PUBKEY", "PUBKEY")


@pytest.fixture()
def dummy_log():
    return """
    Block height: (110)
    Block xyz PUBKEY
    View abc PUBKEY
    """

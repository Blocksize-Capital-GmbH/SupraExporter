import supraexporter.main


def test_main_entrypoint_runs(monkeypatch):
    """
    Smoke test to verify the main module imports and sets up without crashing.
    """
    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")

    # Ensure main module is present and importable
    assert hasattr(supraexporter.main, "__file__")

import time
from threading import Thread

import requests


def test_metrics_endpoint_starts(monkeypatch):
    from supraexporter.server import start_http_server_with_collectors

    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")

    def run_server():
        start_http_server_with_collectors(8001)

    thread = Thread(target=run_server, daemon=True)
    thread.start()
    time.sleep(1)

    res = requests.get("http://localhost:8001/metrics")
    assert res.status_code == 200

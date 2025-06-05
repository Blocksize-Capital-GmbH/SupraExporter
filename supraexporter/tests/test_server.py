import time
from threading import Thread

import requests


def test_custom_metrics_endpoint(monkeypatch):
    from supraexporter.server import run

    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")

    def run_server():
        run()  # this binds to localhost:7896

    thread = Thread(target=run_server, daemon=True)
    thread.start()
    time.sleep(1)

    res = requests.get("http://localhost:7896/debug/metrics/prometheus")
    assert res.status_code == 200

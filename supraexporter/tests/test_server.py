import time
from threading import Thread

import requests

from supraexporter.config import config


def test_custom_metrics_endpoint(monkeypatch):
    from supraexporter.server import run

    monkeypatch.setenv("ROLE", "rpc")
    monkeypatch.setenv("RPC_URL", "http://mock-rpc")
    monkeypatch.setenv("RPC_LOG_PATH", "/tmp/mock.log")
    monkeypatch.setenv("EXPORTER_PORT", "7897")  # Set the port to match your .env

    def run_server():
        run()  # this will use the port from config

    thread = Thread(target=run_server, daemon=True)
    thread.start()
    time.sleep(1)

    res = requests.get(f"http://localhost:{config.port}/debug/metrics/prometheus")
    assert res.status_code == 200

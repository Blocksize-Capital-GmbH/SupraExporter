from http.server import BaseHTTPRequestHandler

from prometheus_client import (
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    generate_latest,
    start_http_server,
)

from supraexporter.collectors.common_collector import CommonCollector
from supraexporter.collectors.rpc_collector import RpcCollector
from supraexporter.collectors.validator_collector import ValidatorCollector
from supraexporter.config import config

registry = CollectorRegistry()


class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-Type", CONTENT_TYPE_LATEST)
            self.end_headers()
            self.wfile.write(generate_latest(registry))
        else:
            self.send_response(404)
            self.end_headers()


def start_http_server_with_collectors(port):
    registry.register(CommonCollector())  # Register first!
    if config.role == "rpc":
        registry.register(RpcCollector())
    elif config.role == "validator":
        registry.register(ValidatorCollector())
    elif config.role == "both":
        registry.register(RpcCollector())
        registry.register(ValidatorCollector())

    start_http_server(port, registry=registry)
    print(f"Starting Prometheus exporter on port {port}...")

    import time

    while True:
        time.sleep(60)

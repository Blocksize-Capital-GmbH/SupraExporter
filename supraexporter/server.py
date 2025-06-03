"""HTTP server and metrics handler for the Supra exporter."""

from http.server import BaseHTTPRequestHandler, HTTPServer

from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, generate_latest

from supraexporter.collectors.common_collector import CommonCollector
from supraexporter.collectors.rpc_collector import RpcCollector
from supraexporter.collectors.validator_collector import ValidatorCollector
from supraexporter.config import config

registry = CollectorRegistry()
registry.register(CommonCollector())  # Register first!

if config.role == "rpc":
    registry.register(RpcCollector())
elif config.role == "validator":
    registry.register(ValidatorCollector())
elif config.role == "both":
    registry.register(RpcCollector())
    registry.register(ValidatorCollector())


class MetricsHandler(BaseHTTPRequestHandler):
    """HTTP handler for serving Prometheus metrics."""

    def do_GET(self):
        """Handle GET requests to serve Prometheus metrics or return 404."""
        if self.path == "/debug/metrics/prometheus":
            self.send_response(200)
            self.send_header("Content-Type", CONTENT_TYPE_LATEST)
            self.end_headers()
            self.wfile.write(generate_latest(registry))
        else:
            self.send_response(404)
            self.end_headers()


def run():
    """Start the HTTP server and serve Prometheus metrics indefinitely."""
    port = 7896
    server_address = ("", port)
    httpd = HTTPServer(server_address, MetricsHandler)
    print(f"Serving metrics at http://localhost:{port}/debug/metrics/prometheus")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

def run_forever():
    print("Running forever...")
    while True:
        time.sleep(60)

def start_http_server_with_collectors(port):
    ...
    start_http_server(port, registry=registry)
    print(f"Starting Prometheus exporter on port {port}...")

    run_forever()

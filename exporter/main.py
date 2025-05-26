# main.py
from exporter.config import config
from exporter.server import start_http_server_with_collectors

def main():
    start_http_server_with_collectors(config.port)

if __name__ == "__main__":
    main()

# main.py
from supraexporter.config import config
from supraexporter.server import start_http_server_with_collectors


def main():
    start_http_server_with_collectors(config.port)


if __name__ == "__main__":
    main()

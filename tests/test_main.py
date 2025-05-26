from unittest.mock import patch
from exporter import main

@patch("exporter.main.start_http_server_with_collectors")
def test_main_entrypoint(mock_start):
    main.main()
    mock_start.assert_called_once()

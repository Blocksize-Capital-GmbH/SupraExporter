from unittest.mock import patch

from supraexporter import main


@patch("supraexporter.main.start_http_server_with_collectors")
def test_main_entrypoint(mock_start):
    main.main()
    mock_start.assert_called_once()

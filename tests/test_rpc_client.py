from unittest.mock import patch
import requests
from exporter.clients.rpc_client import get_block_height

@patch("requests.get")
def test_get_block_height_success(mock_get):
    mock_get.return_value.json.return_value = {"height": 42}
    mock_get.return_value.raise_for_status.return_value = None
    assert get_block_height() == 42

@patch("requests.get", side_effect=requests.exceptions.RequestException)
def test_get_block_height_fail(mock_get):
    assert get_block_height() == 0

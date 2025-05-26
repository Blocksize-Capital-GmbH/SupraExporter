from unittest.mock import patch
from importlib import reload
import exporter.clients.rpc_client as rpc_module

@patch("requests.get")
def test_get_block_height_success(mock_get, mock_env_rpc):
    reload(rpc_module)  # re-evaluate config after env setup
    mock_get.return_value.json.return_value = {"height": 12345}
    mock_get.return_value.raise_for_status.return_value = None

    assert rpc_module.get_block_height() == 12345

@patch("requests.get", side_effect=Exception("fail"))
def test_get_block_height_failure(mock_get, mock_env_rpc):
    reload(rpc_module)
    assert rpc_module.get_block_height() == 0

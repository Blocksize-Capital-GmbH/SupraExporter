from unittest.mock import patch

from supraexporter.utils.public_rpc import get_public_block_height


@patch("supraexporter.utils.public_rpc.requests.get", side_effect=Exception("fail"))
def test_public_rpc_failure(_mock):
    assert get_public_block_height() == 0

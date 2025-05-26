from exporter.clients.log_reader import parse_block_height

def test_parse_block_height_valid():
    log = """
    [INFO] Some unrelated log
    Block height: (12345678)
    """
    assert parse_block_height(log) == 12345678

def test_parse_block_height_invalid():
    log = "No height present"
    assert parse_block_height(log) == 0

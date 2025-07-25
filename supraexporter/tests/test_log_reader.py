import subprocess

import pytest

from supraexporter.clients.log_reader import (
    calculate_keyword_abundance,
    parse_block_height,
    read_last_n_lines,
)


def test_parse_block_height_found():
    log_data = """
    Some random logs
    Block height: (123456)
    More lines
    """
    assert parse_block_height(log_data) == 123456


def test_parse_block_height_not_found():
    log_data = "No height pattern here"
    assert parse_block_height(log_data) == 0


def test_calculate_keyword_abundance_found():
    log_data = """
    Info Block abc123
    Info Block abc123
    Info Block otherkey
    """
    ratio = calculate_keyword_abundance(log_data, "Block", "abc123")
    assert round(ratio, 2) == 0.67


def test_calculate_keyword_abundance_not_found():
    log_data = "Nothing relevant"
    assert calculate_keyword_abundance(log_data, "Block", "abc123") == 0.0


def test_read_last_n_lines_fails(monkeypatch):
    def mock_run(*args, **kwargs):
        raise subprocess.CalledProcessError(1, cmd="tail")

    monkeypatch.setattr(subprocess, "run", mock_run)
    with pytest.raises(RuntimeError):
        read_last_n_lines("/tmp/invalid.log")

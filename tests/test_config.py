"""Tests for depscan configuration validation."""
import pytest

from depscan.config import validate_config


def test_validate_config_accepts_omitted_output_format():
    assert validate_config({}) == {}


@pytest.mark.parametrize("output_format", [None, "html", "TEXT"])
def test_validate_config_rejects_invalid_explicit_output_format(output_format):
    with pytest.raises(ValueError, match="output_format must be"):
        validate_config({"output_format": output_format})

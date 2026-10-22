import pytest

from depscan.config import load_config


def test_load_config_accepts_empty_file(tmp_path):
    config_path = tmp_path / ".depscan.yml"
    config_path.write_text("", encoding="utf-8")

    assert load_config(config_path) == {}


@pytest.mark.parametrize("contents", ["[]", "false", "text"])
def test_load_config_rejects_non_mapping_config(tmp_path, contents):
    config_path = tmp_path / ".depscan.yml"
    config_path.write_text(contents, encoding="utf-8")

    with pytest.raises(ValueError, match="configuration must be a mapping"):
        load_config(config_path)


def test_load_config_rejects_invalid_yaml(tmp_path):
    config_path = tmp_path / ".depscan.yml"
    config_path.write_text("output_format: [", encoding="utf-8")

    with pytest.raises(ValueError, match="invalid YAML:"):
        load_config(config_path)


def test_load_config_rejects_invalid_option(tmp_path):
    config_path = tmp_path / ".depscan.yml"
    config_path.write_text("output_format: xml", encoding="utf-8")

    with pytest.raises(ValueError, match="output_format must be"):
        load_config(config_path)

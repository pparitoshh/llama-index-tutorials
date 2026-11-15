"""Read the project settings from config.yaml in the project root."""

from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).with_name("config.yaml")


def load_config() -> dict:
    """Return the content of config.yaml as a dictionary."""
    with open(CONFIG_PATH, encoding="utf-8") as config_file:
        return yaml.safe_load(config_file)


def llm_model() -> str:
    """Return the name of the Groq model."""
    return load_config()["llm"]["model"]

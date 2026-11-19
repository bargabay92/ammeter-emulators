import pytest
from src.utils.config import load_config


@pytest.fixture(scope="session")
def config():
    return load_config("config/config.yaml")
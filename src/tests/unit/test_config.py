import pytest
from src.tests.base_test import BaseTest


class TestConfigurations(BaseTest):

    def validate_config(self, config):
        assert config is not None, "Configuration is None"
        assert isinstance(config, dict), "Configuration is not a dictionary"

    def test_load_config(self,config):
        self.validate_config(config)
        assert "ammeters" in config, "Missing 'ammeters' section in configuration"
        assert "greenlee" in config["ammeters"], "Missing 'greenlee' section in configuration"
        assert "entes" in config["ammeters"], "Missing 'entes' section in configuration"
        assert "circutor" in config["ammeters"], "Missing 'circutor' section in configuration"

    @pytest.mark.parametrize("ammeter_name", ["greenlee", "entes", "circutor"])
    def test_ammeter_config(self, config, ammeter_name):
        ammeter_config = config["ammeters"][ammeter_name]
        assert isinstance(ammeter_config, dict), f"{ammeter_name} configuration should be a dictionary"

        assert type(ammeter_config["port"]) is int, f"{ammeter_name} port should be an integer"
        assert 0 < ammeter_config["port"] < 65536, f"{ammeter_name} port should be a valid port number"

        assert isinstance(ammeter_config["command"], str), f"{ammeter_name} command should be a string"
        assert ammeter_config["command"].strip(), f"{ammeter_name} command should be a non-empty string"

        assert ammeter_config["measurements_count"] > 0, f"{ammeter_name} measurements_count should be greater than 0"
        assert ammeter_config["sampling_frequency_hz"] > 0, f"{ammeter_name} sampling_frequency_hz should be greater than 0"
        assert ammeter_config["total_duration_seconds"] > 0, f"{ammeter_name} total_duration_seconds should be greater than 0"

        assert isinstance(ammeter_config["measurements_count"], int), f"{ammeter_name} measurements_count should be an integer"
        assert isinstance(ammeter_config["sampling_frequency_hz"], int), f"{ammeter_name} sampling_frequency_hz should be an integer"
        assert isinstance(ammeter_config["total_duration_seconds"], int), f"{ammeter_name} total_duration_seconds should be an integer" 

  
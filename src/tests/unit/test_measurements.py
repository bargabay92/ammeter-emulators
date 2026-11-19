from unittest.mock import patch

import pytest
from src.measurement_sampler import gather_measurements
from src.tests.base_test import BaseTest


class TestGatherMeasurements(BaseTest):


    @pytest.mark.parametrize("command", [
        b"MEASURE_GREENLEE -get_measurement",
        b"MEASURE_ENTES -get_data",
        b"MEASURE_CIRCUTOR -get_measurement -current"
    ])
    def test_gather_three_measurements(self, command):
        with patch(
            "src.measurement_sampler.request_current_from_ammeter",
            side_effect=[1.0, 2.0, 3.0]
        ) as mock_request:
            measurements = gather_measurements(
                measurements_count=3,
                sampling_frequency_hz=100,
                total_duration_seconds=10,
                port=5001,
                command=command
            )

        assert measurements == [1.0, 2.0, 3.0]
        assert mock_request.call_count == 3


    @pytest.mark.parametrize("count", [0, -1])
    def test_gather_measurements_invalid_count(self, count):
        with pytest.raises(ValueError):
            gather_measurements(
                measurements_count=count,
                sampling_frequency_hz=100,
                total_duration_seconds=10,
                port=5001,
                command=b"MEASURE_GREENLEE -get_measurement"
            )

    @pytest.mark.parametrize("sampling_frequency", [0, -100])
    def test_gather_measurements_invalid_sampling_frequency(self, sampling_frequency):
        with pytest.raises(ValueError):
            gather_measurements(
                measurements_count=3,
                sampling_frequency_hz=sampling_frequency,
                total_duration_seconds=10,
                port=5001,
                command=b"MEASURE_GREENLEE -get_measurement"
            )

    @pytest.mark.parametrize("total_duration", [0, -5])
    def test_gather_measurements_invalid_total_duration(self, total_duration):
        with pytest.raises(ValueError):
            gather_measurements(
                measurements_count=3,
                sampling_frequency_hz=100,
                total_duration_seconds=total_duration,
                port=5001,
                command=b"MEASURE_GREENLEE -get_measurement"
            )

    @pytest.mark.parametrize("port", [0, -1, 70000])
    def test_gather_measurements_invalid_port(self, port):
        with pytest.raises(ValueError):
            gather_measurements(
                measurements_count=3,
                sampling_frequency_hz=100,
                total_duration_seconds=10,
                port=port,
                command=b"MEASURE_GREENLEE -get_measurement"
            )
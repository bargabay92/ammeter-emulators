
import pytest
from src.analyze_measurements import analyze_measurements
from src.tests.base_test import BaseTest


class TestMeasurementAnalysis(BaseTest):

    def test_analysis_empty_list(self):
        with pytest.raises(ValueError):
            analyze_measurements([])

    def test_analysis_known_values(self):
        val_list = [1, 2, 3, 4, 5]
        analysis_results = analyze_measurements(val_list)
        assert analysis_results["mean"] == pytest.approx(3), "Mean calculation is incorrect"
        assert analysis_results["median"] == pytest.approx(3), "Median calculation is incorrect"
        assert analysis_results["std_dev"] == pytest.approx(1.4142135623730951), "Standard deviation calculation is incorrect"
        assert analysis_results["min"] == 1, "Minimum value calculation is incorrect"
        assert analysis_results["max"] == 5, "Maximum value calculation is incorrect"
        


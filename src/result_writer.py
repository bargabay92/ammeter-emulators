import time
import csv
from pathlib import Path


def write_results_to_csv(file_path, run_id, start_time, results):
    """Write one CSV row per measurement."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    started_at = time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(start_time)
    )

    with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "run_id", "started_at", "ammeter", "requested_count", "max_duration_seconds", "sampling_frequency_hz", "sample_index",
            "measured_current_amperes", "mean", "median", "std_dev", "min", "max"
        ])

        for ammeter_name, ammeter_results in results.items():
            measurements = ammeter_results["measurements"] 
            summary = ammeter_results["summary"]
            config = ammeter_results["config"]
            for index, current in enumerate(measurements, start=1):
                writer.writerow([
                    run_id, # unique identification 
                    started_at, # timestamp of the run
                    ammeter_name, # ammeter name
                    config["measurements_count"], # requested measurement count
                    config["total_duration_seconds"], # maximum duration in seconds
                    config["sampling_frequency_hz"], # sampling frequency in Hertz
                    index,  # measurement number of each cycle
                    current, # measurement value
                    summary["mean"], 
                    summary["median"], 
                    summary["std_dev"], 
                    summary["min"], 
                    summary["max"], 
                ])

    return file_path
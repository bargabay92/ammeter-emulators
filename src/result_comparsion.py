from pathlib import Path
import csv


def compare_results_across_ammeters():
    summaries = {}

    for file in sorted(Path("results").glob("measurements_*.csv")):
        with open(file, newline="", encoding="utf-8") as csvfile:
            for row in csv.DictReader(csvfile):
                key = (row["run_id"], row["ammeter"]) # identifier for measuremenet group
                if key not in summaries:
                    summaries[key] = {
                        "run_id": row["run_id"],
                        "started_at": row["started_at"],
                        "ammeter": row["ammeter"],
                        "actual_count": 0,
                        "requested_count": int(row["requested_count"]),
                        "max_duration_seconds": float(row["max_duration_seconds"]),
                        "sampling_frequency_hz": float(row["sampling_frequency_hz"]),
                        "mean": float(row["mean"]),
                        "median": float(row["median"]),
                        "std_dev": float(row["std_dev"]),
                        "min": float(row["min"]),
                        "max": float(row["max"]),
                    }

                summaries[key]["actual_count"] += 1 

    comparison = sorted(
        summaries.values(),
        key=lambda item: (item["ammeter"], item["started_at"])
    ) # sort the comparison list by ammeter name and then by started_at timestamp

    if comparison:
        with open(
            "results/comparison.csv", "w", newline="", encoding="utf-8"
        ) as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=list(comparison[0])
            )
            writer.writeheader()
            writer.writerows(comparison)

    return comparison


# results_comparison = compare_results_across_ammeters()
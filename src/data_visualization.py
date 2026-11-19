from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def plot_measurements(results, run_id, output_dir="results"):
    """Save a measurement scatter plot for each ammeter."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    plot_paths = []

    for ammeter_name, data in results.items():
        measurements = data["measurements"]
        if not measurements:
            continue

        sample_numbers = range(1, len(measurements) + 1)
        mean = data["summary"]["mean"]

        fig, ax = plt.subplots(figsize=(9, 5))

        try:
            ax.scatter(
                sample_numbers,
                measurements,
                label="Measurements",
                color="steelblue",
            )
            ax.axhline(
                mean,
                color="darkorange",
                linestyle="--",
                label=f"Mean: {mean:.4g} A",
            )

            ax.set_title(f"{ammeter_name.upper()} — Current Measurements")
            ax.set_xlabel("Measurement Number")
            ax.set_ylabel("Current (A)")
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.grid(True, alpha=0.25)
            ax.set_axisbelow(True)
            ax.legend()

            fig.tight_layout()

            file_path = output_path / f"plot_{run_id}_{ammeter_name}.png"
            fig.savefig(file_path, dpi=150)
            plot_paths.append(file_path)
        finally:
            plt.close(fig)

    return plot_paths
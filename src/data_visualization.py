from pathlib import Path
import matplotlib.pyplot as plt


def plot_measurements(results, run_id, output_dir="results"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for ammeter_name, data in results.items():
        measurements = data["measurements"]
        sample_numbers = range(1, len(measurements) + 1)

        fig, ax = plt.subplots()
        ax.plot(sample_numbers, measurements, marker="o")
        ax.axhline(
            data["summary"]["mean"],
            color="red",
            linestyle="--",
            label="Mean"
        )

        ax.set_title(f"{ammeter_name.upper()} — Current Measurements")
        ax.set_xlabel("Measurement Number")
        ax.set_ylabel("Current (A)")
        ax.grid(True, alpha=0.3)
        ax.legend()

        fig.tight_layout()
        fig.savefig(
            Path(output_dir) / f"plot_{run_id}_{ammeter_name}.png"
        )
        plt.close(fig)
import threading
import time
import uuid
from Ammeters.Circutor_Ammeter import CircutorAmmeter
from Ammeters.Entes_Ammeter import EntesAmmeter
from Ammeters.Greenlee_Ammeter import GreenleeAmmeter
from src.result_comparsion import compare_results_across_ammeters
from src.result_writer import write_results_to_csv
from src.analyze_measurements import analyze_measurements
from src.measurement_sampler import gather_measurements
from src.utils.config import load_config
from src.utils.arg_parse import parse_args
from src.data_visualization import plot_measurements


def run_greenlee_emulator(port):
    greenlee = GreenleeAmmeter(port)
    greenlee.start_server()

def run_entes_emulator(port):
    entes = EntesAmmeter(port)
    entes.start_server()

def run_circutor_emulator(port):
    circutor = CircutorAmmeter(port)
    circutor.start_server()

def main():
    args = parse_args()
    config_file = load_config('config/config.yaml') # load config
    run_id = str(uuid.uuid4()) # unique identification for each run

    # Start each ammeter in a separate thread
    threading.Thread(
        target=run_greenlee_emulator,
        args=(config_file["ammeters"]["greenlee"]['port'],), 
        daemon=True).start()
    threading.Thread(
        target=run_entes_emulator,
        args=(config_file["ammeters"]["entes"]['port'],),
        daemon=True).start()
    threading.Thread(
        target=run_circutor_emulator,
        args=(config_file["ammeters"]["circutor"]['port'],),
        daemon=True).start()

    # Wait for the servers to start, if you have problem restarting the servers between runs try increasing sleep time.
    time.sleep(5)

    start_time = time.time()
    results = {}

    for ammeter_name, ammeter_config in config_file["ammeters"].items():
        measurements = gather_measurements(
            measurements_count=ammeter_config["measurements_count"],
            sampling_frequency_hz=ammeter_config["sampling_frequency_hz"],
            total_duration_seconds=ammeter_config["total_duration_seconds"],
            port=ammeter_config["port"],
            command=ammeter_config["command"],
        )

        results[ammeter_name] = {
            "config": ammeter_config, 
            "measurements": measurements,
            "summary": analyze_measurements(measurements),
        }

    total_runtime = time.time() - start_time
    print(f"Total runtime: {total_runtime:.2f} seconds")
    write_results_to_csv(
        file_path=f"results/measurements_{run_id}.csv",
        run_id=run_id,
        start_time=start_time,
        results=results,
    )

    if args.plot:
        plot_measurements(results, run_id)

    if args.compare:
        compare_results_across_ammeters()



if __name__ == "__main__":
    main()
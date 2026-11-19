

import time
from Ammeters.client import request_current_from_ammeter


def gather_measurements(measurements_count: int,
                        sampling_frequency_hz: float,
                        total_duration_seconds: float,
                        port: int,
                        command: bytes):
    command = command.encode('utf-8') if isinstance(command, str) else command

    if type(measurements_count) is not int or measurements_count <= 0:
        raise ValueError("measurements_count must be greater than zero")
    if type(sampling_frequency_hz) not in (int, float) or sampling_frequency_hz <= 0:
        raise ValueError("sampling_frequency_hz must be a positive number")
    if type(total_duration_seconds) not in (int, float) or total_duration_seconds <= 0:
        raise ValueError("total_duration_seconds must be a positive number")
    if type(port) is not int or port <= 0 or port > 65535:
        raise ValueError("port must be an integer between 1 and 65535")
    
    measurements = []
    interval_period = 1 / sampling_frequency_hz
    start_time = time.time()
    while len(measurements) < measurements_count and time.time() - start_time < total_duration_seconds:
        current = request_current_from_ammeter(port, command) 
        measurements.append(current)
        time.sleep(interval_period) 

    return measurements
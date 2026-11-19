import math


def calculate_mean(measurements):
    """
    Calculate the mean of the measurements.

    Args:
        measurements (list): A list of measurement values.

    Returns:
        float: The mean of the measurements.
    """
    return math.fsum(measurements) / len(measurements) if measurements else 0

def calculate_median(measurements):
    """
    Calculate the median of the measurements.

    Args:
        measurements (list): A list of measurement values.

    Returns:
        float: The median of the measurements.
    """
    sorted_measurements = sorted(measurements)
    n = len(sorted_measurements)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_measurements[mid - 1] + sorted_measurements[mid]) / 2
    else:
        return sorted_measurements[mid]

def calculate_standard_deviation(measurements):
    """
    Calculate the standard deviation of the measurements.

    Args:
        measurements (list): A list of measurement values.

    Returns:
        float: The standard deviation of the measurements.
    """
    mean = calculate_mean(measurements)
    variance = sum((x - mean) ** 2 for x in measurements) / len(measurements) if measurements else 0
    return math.sqrt(variance)

def min_max_measurements(measurements):
    """
    Calculate the minimum and maximum of the measurements.

    Args:
        measurements (list): A list of measurement values.  
    """
    if not measurements:
        return None, None
    return min(measurements), max(measurements)


def analyze_measurements(measurements):
    """
    Analyze the measurements and return a summary.

    Args:
        measurements (list): A list of measurement values.   
    """
    if not measurements: raise ValueError("The measurements list is empty. Cannot analyze empty data.")
    min_max = min_max_measurements(measurements)
    measurement_summary = {
        "mean": calculate_mean(measurements),
        "median": calculate_median(measurements),
        "std_dev": calculate_standard_deviation(measurements),
        "min": min_max[0],
        "max": min_max[1]
    }
    return measurement_summary
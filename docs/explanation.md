
# Addressed Bugs 
1. runs occasionally failed with "OSError: Address already in use"
To support reusing the server address after orevious run, I added to base_ammeter.py (before bind) the following line: 
```s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)```
this allows the address re-use in situation where there is a lingering TCP connection .

2. Communication timeout -  a socket timeout was added to the function: request_current_from_ammeter - in order to avoid waiting for forever for responeses, so when timeout exeed, it will raise a timeout exception.


# How to run?
First, Install dependencies with : ```python -m pip install -r requirements.txt```

Run measurements using the default configuration:

```python main.py```

Run measurements and generate plots:

```python main.py --plot```

Run measurements and generate a comparison of saved runs:

```python main.py --compare```

Generate both plots and a comparison:

```python main.py --plot --compare```

Use a specific configuration file:

```python main.py --config config/config.yaml```

Run the automated tests:

```python -m pytest src/tests```


# Output Files

Results are saved in the results/ directory:

### measurements_<run_id>.csv: measurements, statistical summaries, and sampling settings for each ammeter.

### comparison.csv: a summary of saved runs, grouped by ammeter and ordered by start time.

### plot_<run_id>_<ammeter_name>.png: measurement plots, generated when --plot is enabled.
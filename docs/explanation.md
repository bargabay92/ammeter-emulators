
# Bugs
One bug that i've encourted with, was an exception of 'Address already in use',
so I added in base_ammeter.py, right before the bind:
```s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)```
Which enables to re-use the port although it remained open from the last run.

request_current_from_ammeter - added timeout to avoid waiting for forever for responeses



# How to run?
python main.py --plot
python main.py --compare
python main.py --config config/config.yaml
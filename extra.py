import os

# Create a dictionary to store state across function calls
_sequence_state = {}

def get_random_file(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        return None

    # Initialize state if not already done
    if directory not in _sequence_state:
        _sequence_state[directory] = {'index': 0, 'files': files}
    else:
        # Refresh file list if it has changed
        if _sequence_state[directory]['files'] != files:
            _sequence_state[directory] = {'index': 0, 'files': files}

    index = _sequence_state[directory]['index']
    file = files[index]
    _sequence_state[directory]['index'] = (index + 1) % len(files)

    return file

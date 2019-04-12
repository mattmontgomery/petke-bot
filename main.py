from textgenrnn import textgenrnn
from pathlib import Path

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "petke.txt"

# Path(filename + ".hdf5").touch()
textgen = textgenrnn(name=filename)
textgen.train_from_file(filename, num_epochs=10)
textgen.generate_samples(1, interactive=False)

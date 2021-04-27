#!/bin/bash
# This script collect training data from a given directory by looking
# for all the files in that directory that end wih ".mid" and converting
# them to a five-track pianoroll dataset.
# Usage: ./generate_data.sh [INPUT_DIR] [OUTPUT_FILENAME]
python "PLD_SMART/src/algo/MuseGAN/v1/src/collect_data.py" -i "/content/drive/My Drive/SMART/MuseGAN/data" -o "/content/drive/My Drive/SMART/MuseGAN/data/output.npz"

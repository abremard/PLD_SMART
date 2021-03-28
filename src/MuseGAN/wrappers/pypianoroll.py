""" Read pianorolls, visualize, export
"""

import pypianoroll
import matplotlib.pyplot as plt

file = "./data/b97c529ab9ef783a849b896816001748.npz"

def load(file):
    return pypianoroll.load(file) 

def visualize(file):
    m = pypianoroll.load(file)
    m.plot()
    plt.show()

def convertToMidi(path, file):
    pypianoroll.write("./test.mid", pypianoroll.load(file))

if __name__ == "__main__":
    convertToMidi("./test.mid")
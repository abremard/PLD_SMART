""" LSTM module

Monophonic midi generation using LSTM with Attention mechanism
source: https://github.com/davidADSP/GDL_code

"""

from pathlib import Path
parent = Path(__file__).resolve().parent
srcPath = str(parent).replace("\\", "\\\\")
import sys
sys.path.insert(0, srcPath)
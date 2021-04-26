import pypianoroll


path = 'output.npz'
multitrack = pypianoroll.read(path="BackInBlack.mid")

pypianoroll.save(path=path, multitrack=multitrack)
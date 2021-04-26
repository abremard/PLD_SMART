# import pypianoroll


# path = 'data/output.npz'
# multitrack = pypianoroll.read(path="BackInBlack.mid")

# pypianoroll.save(path=path, multitrack=multitrack)

from numpy import load

data = load('data/output.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
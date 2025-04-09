# MBW (matplotlib backend workaround)

A minimalistic python package to get interactive plots while working with pycharm without imposing a backend for other users.

## Setup

```commandline
pip install mbw@git+https://github.com/eurobios-mews-labs/mbw.git
```

## Usage

```python
import matplotlib.pyplot as plt
import mbw
import numpy as np

plt.figure()
x = np.linspace(0.0, np.pi, 21)
y = np.sin(x)
plt.plot(x, y)
plt.show()
```

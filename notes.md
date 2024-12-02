from numpy import dtype

# Python Class Notes

### Importing NumPy

```python
import numpy as np

# OR 

from numpy import *
```

- The array object in NumPy is called `ndarray`.
- We can create a NumPy `ndarray` object by using the `array()` function.

### Making Multidimensional Array
```python
import numpy
Myarr = numpy.array([[1, 2, 3], [4, 5, 6]])
```
- The first ist in the argument represents the columns, and the second list in the argument represents the rows.

### Checking dimensions of the array
```python
Myarr.ndim
```
### Creating ndarray with Zeros
```python
import numpy as np
x = np.zeros((512,512), dtype = float)
```

### Creating ndarray with Ones
```python
import numpy as np
x = np.ones((512,512), dtype = float)
```
# Tkinter Notes

A tkinter window application can be created by following these steps:
1. Import the tkinter module.
2. Create the main application window.
3. Add widgets like labels, buttons, frames, etc. to the main window.
4. Enter the main event loop to take action against each event triggered by the user.

### Importing tkinter module
```python
import tkinter as tk
# or
from tkinter import *
```

### Creating the main application window
```python
top = tk.Tk()
```

### Adding widgets to the main window
```python
label = tk.Label(top, text="Hello, World!")
label.pack()
```

### Entering the main event loop
```python
top.mainloop()
```

## Geometry Methods
1. **`pack()`**: It organizes the widgets in blocks before placing them in the parent widget.

    Syntax:
    ```python
    widget.pack(options)
    ```
   
2. **`grid()`**: It organizes the widgets in a table-like structure in the parent widget.
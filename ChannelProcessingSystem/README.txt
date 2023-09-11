## Code Documentation and Usage Guide

## Introduction

This .zip folder contains a Python script and testcases unit test script that performs various calculations based on user-defined parameters and input data. It includes functions for mathematical operations and is designed to be easily extensible for adding more functions or parameters. This README file provides an overview of the code and instructions on how to use it.

## Getting Started


### Prerequisites

Before using this code, make sure you have the following prerequisites installed on your system:

- Python (3.x recommended)
- Miniconda or Anaconda compiler recommended
- NumPy library

You can install NumPy using pip:

```bash

pip install numpy

```

## Usage

1. **Input Data:**

   - Create a `parameters.txt` file with key-value pairs for the parameters required for calculations. Each line should have the format: `parameter_name, parameter_value`.

   Example `parameters.txt`:
   ```
   m, 2.5
   c, 3.0
   g, 9.8
   h, 10.0
   ```

   - Create a `channels.txt` file with data for the `X` variable. Each line should contain comma-separated values, and non-numeric values (e.g., 'X') will be ignored.

   Example `channels.txt`:
   ```
   X, 1, 2, 3, 4, 5

   ```

2. **Run the Script:**

   Execute the Python script `main.py`:

   ```bash

   python main.py

   ```
3. **Output:**

   The script will calculate various metrics and print the results to the console. You can customize which metrics to print by uncommenting the respective lines in the code.

   Example Output:
   ```
   The value of metric b is : 15.0
   the value of metric G is : 245.0
   ```

## Extensibility

The code is designed to be easily extensible. You can add more functions or parameters as needed. Here's how:

- Define your new function following the existing function structure.
- Add the function call in the appropriate section of the script.
- Update the `parameters.txt` file with any new parameters required for your function.
- Run the script, and your new function will be included in the calculations.

## Acknowledgments

- This code uses the NumPy library for numerical operations.
- Inspiration for extensibility was drawn from the need for easily adding new functions and parameters.

This README provides a clear guide for users to understand how to use the code, customize it, and acknowledge any dependencies or packages.
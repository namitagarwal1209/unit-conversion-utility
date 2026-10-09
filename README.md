# Unit Conversion Utility Tool

## Description

A command line utility that:

* Reads unit conversion relationships from a CSV file.
* Converts a user supplied quantity from one unit to another.

The utility supports:

* Direct conversions, such as meter to feet.
* Reverse conversions, even when only the opposite direction is provided in the CSV.
* Indirect conversions through multiple known relationships.
* Conversion from a unit to itself.
* Validation of unknown units and unavailable conversion paths.
* Validation of invalid CSV conversion factors.

## How to Run

The project inlcudes a "units.csv".

### Option 1: Use the provided CSV file

From the project root, run:

`python main.py`

This automatically loads the provided units.csv file.

### Option 2: Use your own CSV file

You can also use a CSV file stored anywhere on your computer by providing its path:

`python main.py <csv_file>`

For example, if your CSV file is located at:

C:\Users\Namit\Documents\conversions.csv

Run:

python main.py "C:\Users\Namit\Documents\conversions.csv"

The custom CSV must contain the columns SourceUnit, TargetUnit, and Factor, as shown below:

```text
SourceUnit,TargetUnit,Factor
meter,feet,3.28084
feet,inch,12
```

### User Input

The utility requests three inputs:

* Quantity: float
* Source unit: string
* Target unit: string

Example output:

`5.0 meter = 196.8504 inch`

Note: Unit inputs are case insensitive.

## Implementation

### 1. main.py

Handles command line input and output.

### 2. csv_loader.py

Loads conversion data from the CSV file and constructs the conversion graph.

The CSV loader builds an adjacency list representing the available unit conversions as a graph. Each unit is represented as a node, and each conversion relationship is represented as an edge containing its conversion factor.

For every conversion in the CSV, a reverse edge is also created using the reciprocal of the supplied factor.

For example, given the following CSV data:

```text
SourceUnit,TargetUnit,Factor
meter,feet,3.28084
```

The following relationships are stored in the graph:

```python
{
    "meter": {
        "feet": 3.28084
    },
    "feet": {
        "meter": 1 / 3.28084
    }
}
```

### 3. conversion.py

Contains the conversion logic and Breadth First Search (BFS) path finding algorithm.

BFS is used to find a path between the requested source and target units. Conversion factors are accumulated while traversing the path.

For example:

```text
meter -> feet : 3.28084
feet -> inch  : 12
```

Using BFS, the conversion factor for meter to inch becomes:

`3.28084 × 12 = 39.37008`

The input quantity is then multiplied by the resulting conversion factor to produce the final converted value.

### 4. units.csv

Contains the available conversion relationships.

### 5. tests/

Contains automated tests for `conversion.py` and `csv_loader.py`.

## Tests

The project uses Python's built in `unittest` framework.

Run all tests from the project root using:

`python -m unittest discover -s tests`

Tests cover:

* Direct conversion
* Reverse conversion
* Indirect conversion
* Same unit conversion
* Quantity conversion
* Unknown units
* Unavailable conversion paths
* Forward and reverse graph creation
* Invalid conversion factors
* Zero conversion factors

## Dependencies

The utility uses only the Python standard library and has no external package dependencies.

## LLM Usage

ChatGPT was used as a learning and review aid during development. It was used to discuss the graph based approach to the conversion problem, review implementation decisions, explain `unittest` concepts, and suggest edge cases and test scenarios.

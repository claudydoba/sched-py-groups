# Scheduling Groups Optimizer

A Python-based utility to discover optimal meeting groups based on individual weekly availability. It processes participant records and identifies time slots that maximize attendance for a fixed number of groups.

## Features
* **CSV Ingestion**: Automatically detects delimiters and cleans input data.
* **Density Analysis**: Identifies restrictive participants with low availability.
* **Greedy Optimization**: Iteratively selects slots with the highest coverage.
* **Professional Logging**: Structured output for better traceability.

## Prerequisites
* Python 3.14+
* Pandas 3.0.2+

## Usage
1. Prepare your `disponibilidad.csv` with the following headers: `Id, Monday, Tuesday, Wednesday, Thursday, Friday`.
2. Run the script:
   ```bash
   python3 main.py disponibilidad.csv
   ```
3. Check the console output for group assignments and debugging stats.

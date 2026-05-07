# Developer Documentation

## Architecture Overview
The project follows a **Functional Programming** paradigm to ensure idempotency and testability. Data flows through a linear pipeline of pure transformations.

### Data Pipeline
1. **Ingestion**: `utils.load_csv` reads raw data.
2. **Standardization**: `core.preprocess_dataframe` ensures `Id` is the index and headers are trimmed.
3. **Binarization**: `core.get_binary_matrix` explodes the multi-choice availability into a sparse 1/0 matrix where each column is a `Day_Slot` pair.
4. **Analysis**: `core.get_stats` computes frequency distributions and participant density.
5. **Optimization**: `core.find_groups_greedy` implements a recursive-style iteration to pick the best-performing columns from the matrix and remove assigned participants.

## Module Breakdown
* `consts.py`: Domain-specific constants (headers, slot names, thresholds).
* `utils.py`: Infrastructure logic (logging configuration, file I/O).
* `core.py`: Pure logic and data transformations.
* `main.py`: Orchestration and error handling.

## Maintenance Notes
* **Pandas 3.0 Compliance**: Avoid using the `axis` parameter in `groupby` and `sum` where deprecated. Use `.T` (transpose) for column-wise operations.

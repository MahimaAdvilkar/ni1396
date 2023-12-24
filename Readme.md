# Employee Data Analysis

## Introduction

This Python script is designed to analyze employee data stored in a CSV file. The script performs various tasks, including reading employee data, calculating hourly salaries, grouping data by employee type code, and generating statistics such as mean and standard deviation for each employee type. The results are then written to an output file.

## Requirements

- Python 3.x
- NumPy library

## Usage

1. Ensure that you have Python 3.x installed on your system.
2. Install the NumPy library using the following command:

   ```
   pip install numpy
   ```

3. Download the script and replace the `file_path` variable in the `main` function with the path to your CSV file.

4. Run the script using the following command:

   ```
   python script_name.py
   ```

## Functions

### `read_employee_data(file_path)`

- **Input**: `file_path` (string) - Path to the CSV file containing employee data.
- **Output**: Numpy array containing employee data.

### `calculate_hourly_salary(base_pay, hours_per_year=1778)`

- **Input**: 
  - `base_pay` (float) - Base salary of the employee.
  - `hours_per_year` (int, optional) - Number of working hours per year. Default is set to 1778.
- **Output**: Calculated hourly salary.

### `calculate_statistics_by_employee_type(employee_data)`

- **Input**: Numpy array containing employee data.
- **Output**: Dictionary containing mean and standard deviation of hourly salaries for each employee type.

### `write_output_to_file(output_file, employee_data, statistics)`

- **Input**:
  - `output_file` (string) - Path to the output file.
  - `employee_data` (Numpy array) - Employee data.
  - `statistics` (dict) - Dictionary containing mean and standard deviation of hourly salaries for each employee type.
- **Output**: Output file containing employee IDs, hourly pay, mean values, and standard deviation values.

### `main()`

- **Description**: Main function to execute the entire script.
- **Input**: None.
- **Output**: Results written to the specified output file.

## Example

```python
python employee_analysis_script.py
```

## Notes

- Ensure that the CSV file follows the expected format with relevant columns such as 'Id,' 'BasePay,' and 'EmployeeTypeCode.'
- Review the output file for analyzed results.

Feel free to customize the script as needed for your specific use case.
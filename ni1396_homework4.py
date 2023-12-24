import numpy as np

#Reading employee data from CSV Filee into Numpy array File  

def read_employee_data(file_path):
    try:
     
        employee_data = np.genfromtxt(file_path, delimiter=',', dtype=None, names=True, encoding='utf-8-sig')
        return employee_data
    except Exception as e:
        print(f"Error reading employee data: {e}")
        return None
    
#Calculating Hourly Salary of the employees

def calculate_hourly_salary(base_pay, hours_per_year=1778):

    hourly_salary = base_pay / hours_per_year
    return hourly_salary

#Grouping Data by Employee Typecode
def calculate_statistics_by_employee_type(employee_data):
    # Group data by EmployeeTypeCode
    grouped_data = {}
    for row in employee_data:
        emp_type = row['EmployeeTypeCode']
        if emp_type not in grouped_data:
            grouped_data[emp_type] = []
        grouped_data[emp_type].append(row)

# Calculating mean and standard deviation for each EmployeeTypeCode
    statistics = {}
    for emp_type, data in grouped_data.items():
        # Convert data to numpy array
        data = np.array(data)
        
        base_hourly_salary = calculate_hourly_salary(data['BasePay'])
        mean_salary = np.mean(base_hourly_salary)
        std_dev_salary = np.std(base_hourly_salary)
        statistics[emp_type] = {'mean': mean_salary, 'std_dev': std_dev_salary}

    return statistics

#Defining and writing the output file 

def write_output_to_file(output_file, employee_data, statistics):
    try:
        with open(output_file, 'w') as file:
            # Write employee ID and hourly pay of BasePay
            file.write("Id, hr_base_pay\n")
            for row in employee_data:
                hourly_pay = calculate_hourly_salary(row['BasePay'])
                file.write(f"{row['Id']}, {int(hourly_pay)}\n")

# Write summary lines
            file.write("\n")
            
            # Sort employee types for consistent order in output
            sorted_employee_types = sorted(statistics.keys())
            
            # Write mean values
            for emp_type in sorted_employee_types:
                file.write(f"{emp_type}:{statistics[emp_type]['mean']:.4f}, ")
            file.write("\n")
            
            # Write standard deviation values
            for emp_type in sorted_employee_types:
                file.write(f"{emp_type}:{statistics[emp_type]['std_dev']:.4f}, ")
            file.write("\n")

    except Exception as e:
        print(f"Error writing output to file: {e}")

def main():
    file_path = '/Users/mahimaadvilkar/emp_base_salaries_homework4.csv'
    output_file = 'ni1396_stats.txt'

    employee_data = read_employee_data(file_path)
    if employee_data is not None:
        statistics = calculate_statistics_by_employee_type(employee_data)
        write_output_to_file(output_file, employee_data, statistics)

if __name__ == "__main__":
    main()

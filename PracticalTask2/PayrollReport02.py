### PayrollReport02.py ファイル
import csv

def read_employees_from_csv(filename):
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # This skips the header row
        employees = [row for row in reader]
    return employees

def calculate_payroll(employees):
    payroll_data = {'Manager': 0, 'Sales': 0, 'Administration': 0, 'total_salary': 0, 'num_employees': 0}
    for employee in employees:
        # Ensure the 'position' from the CSV file is exactly 'Manager', 'Sales', or 'Administration'.
        position = employee[2]
        if position not in payroll_data:
            continue  # Skip this employee or handle unexpected position appropriately.
        salary = float(employee[3])
        payroll_data[position] += salary
        payroll_data['total_salary'] += salary
        payroll_data['num_employees'] += 1
    # Calculate the average salary if num_employees is not zero
    payroll_data['average_salary'] = payroll_data['total_salary'] / payroll_data['num_employees'] if payroll_data['num_employees'] > 0 else 0
    return payroll_data

def write_payroll_report_to_csv(report_data, filename):
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Total payroll", f"${report_data['total_salary']:.2f}"])
        writer.writerow(["Number of payroll", report_data['num_employees']])
        writer.writerow(["Average payroll", f"${report_data['average_salary']:.2f}"])
        writer.writerow([])
        writer.writerow(["Total pay for"])
        for position, total in (("Manager", report_data['Manager']), ("Sales", report_data['Sales']), ("Administration", report_data['Administration'])):
            writer.writerow([f"Total salaries for {position}", f"${total:.2f}"])

def main():
    employees_file_path = './Practicaltask2/employees.csv'
    employees = read_employees_from_csv(employees_file_path)
    payroll_data = calculate_payroll(employees)
    write_payroll_report_to_csv(payroll_data, './Practicaltask2/PayrollReport.csv')

if __name__ == '__main__':
    main()
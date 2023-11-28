# Payrollreport02.py
import csv

def read_employees_from_csv(filename):
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # This skips the header row
        employees = [row for row in reader]
    return employees


def calculate_payroll(employees):
    payroll_data = {
        'totals_by_position': {'Manager': 0, 'Sales': 0, 'Administration': 0},
        'total_salary': 0,
        'num_employees': 0
    }
    for employee in employees:
        if len(employee) < 4:
            continue  

        position = employee[2]
        if position not in payroll_data['totals_by_position']:
            continue

        try:
            salary = float(employee[3])
        except ValueError:
            continue 

        payroll_data['totals_by_position'][position] += salary
        payroll_data['total_salary'] += salary
        payroll_data['num_employees'] += 1

    payroll_data['average_salary'] = (payroll_data['total_salary'] / payroll_data['num_employees']) if payroll_data['num_employees'] > 0 else 0
    return payroll_data

def print_and_write_payroll_report(report_data, filename):
    report_lines = []
    report_lines.append(f"Total payroll: ${report_data['total_salary']:.2f}")
    report_lines.append(f"Number of payroll: {report_data['num_employees']}")
    report_lines.append(f"Average payroll: ${report_data['average_salary']:.2f}")
    report_lines.append("\nTotal pay for:")
    for position, total in report_data['totals_by_position'].items():
        report_lines.append(f"Total salaries for {position}: ${total:.2f}")

    with open(filename, 'w') as file:
        for line in report_lines:
            print(line)
            file.write(line + "\n")

def main():
    employees_file_path = './Practicaltask2/employees.csv'
    employees = read_employees_from_csv(employees_file_path)
    payroll_data = calculate_payroll(employees)
    payroll_report_path = './Practicaltask2/PayrollReport.txt'
    print_and_write_payroll_report(payroll_data, payroll_report_path)

if __name__ == '__main__':
    main()
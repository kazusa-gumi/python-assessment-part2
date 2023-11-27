def read_employee_data(filename):
    employees = []
    with open(filename, 'r') as file:
        while True:
            try:
                id_line = next(file).strip()
                name_line = next(file).strip()
                position_line = next(file).strip()
                salary_line = next(file).strip()
            except StopIteration:
                # ファイルの終わりに達した
                break
            
            employee = {
                'id': id_line,
                'name': name_line,
                'position': position_line,
                'salary': float(salary_line)
            }
            employees.append(employee)
    return employees

def print_employees(employees):
    for employee in employees:
        print(f"{employee['id']} {employee['name']} {employee['position']} ${employee['salary']:.2f}")


def calculate_salaries(employees):
    total_salaries = {
        'Manager': 0,
        'Sales': 0,
        'Administration': 0
    }
    total_salary = 0

    for employee in employees:
        position = employee['position']
        salary = employee['salary']
        total_salaries[position] += salary
        total_salary += salary

    num_employees = len(employees)
    average_salary = total_salary / num_employees if num_employees > 0 else 0

    return {
        'totals_by_position': total_salaries,
        'total_salary': total_salary,
        'num_employees': num_employees,
        'average_salary': average_salary
    }

def write_payroll_report(report_data, filename):
    with open(filename, 'w') as file:
        file.write(f"Total payroll: ${report_data['total_salary']:.2f}\n")
        file.write(f"Number of payroll: {report_data['num_employees']}\n")
        file.write(f"Average payroll: ${report_data['average_salary']:.2f}\n")
        file.write("\nTotal pay for:\n")
        for position, total in report_data['totals_by_position'].items():
            file.write(f"Total salaries for {position}: ${total:.2f}\n")

def write_employees_report(employees, filename):
    with open(filename, 'w') as file:
        for employee in employees:
            file.write(f"{employee['id']} {employee['name']} {employee['position']} ${employee['salary']:.2f}\n")

# 主な実行関数
def main():
    # 'employees.txt' ファイルのフルパスを指定
    employees_file_path = './Practicaltask2/Employees.txt'
    # 従業員情報をファイルから読み込む
    employees = read_employee_data(employees_file_path)
    # 給与情報を計算
    payroll_data = calculate_salaries(employees)
    # 給与報告書をファイルに書き込む
    payroll_report_path = './Practicaltask2/PayrollReport.txt'
    write_payroll_report(payroll_data, payroll_report_path)
    # 整形された従業員情報をファイルに書き込む
    employees_report_path = './Practicaltask2/EmployeesReport.txt'
    write_employees_report(employees, employees_report_path)

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()

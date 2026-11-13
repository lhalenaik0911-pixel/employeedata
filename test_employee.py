from employee import employee_details

def test_employee_details_laxmi():
    result = employee_details("rahul", 101, "IT", 45000 )

    expected_emp = (
        "Employee name: rahul\n"
        "Employee id: 101\n"
        "department: IT\n"
        "salary: 45000"
    )

    assert result == expected_emp
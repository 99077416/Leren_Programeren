from test_lib import test, report

def calculate_cilinder_content(diameter,hoogte):
    return round((diameter/ 2) * (diameter/ 2) * 3.1415 * hoogte,1)
    


diameter = 8.0
height = 5.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

report()
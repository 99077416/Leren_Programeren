from test_lib import test, report
import math
def calculate_cilinder_content(diameter,hoogte):
    return round((diameter/ 2) * (diameter/ 2) * math.pi * hoogte,1)
    


diameter = 8.0
height = 5.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

diameter = 11.0
height = 7.0
expect_content = 665.2
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

diameter = 18.0
height = 7.0
expect_content = 1781.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

diameter = 15.0
height = 2.0
expect_content = 353.4
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

diameter = 0.0
height = 6.0
expect_content = 0.0
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

report()
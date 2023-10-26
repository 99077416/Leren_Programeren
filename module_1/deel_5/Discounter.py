from test_lib import test, report

month_discount_brands = ('Vespa', 'Kymco','Yamama')
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        return round(price * MONTH_DISCOUNT_PERC / 100, 2)
    else:
        return 0


print(calc_discount(1456.54,'Vespa',month_discount_brands))


expected = round(1456.54 * MONTH_DISCOUNT_PERC / 100,2)
calculated = calc_discount(1456.54,'Vespa',month_discount_brands)
test('Discount', expected, calculated)

expected = round(50 * MONTH_DISCOUNT_PERC / 100,2)
calculated = calc_discount(50,'Yamama',month_discount_brands)
test('Discount', expected, calculated)

expected = 0
calculated = calc_discount(5000,'Volkswagen',month_discount_brands)
test('Discount', expected, calculated)

expected = round(732.96 * MONTH_DISCOUNT_PERC / 100,2)
calculated = calc_discount(732.96,'Vespa',month_discount_brands)
test('Discount', expected, calculated)

expected = round(596 * MONTH_DISCOUNT_PERC / 100,2)
calculated = calc_discount(596,'Kymco',month_discount_brands)
test('Discount', expected, calculated)


report()
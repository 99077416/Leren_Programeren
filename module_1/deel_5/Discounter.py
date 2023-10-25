from test_lib import test, report

month_discount_brands = ('Vespa', 'Kymco','Yamama')
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        return round(price * MONTH_DISCOUNT_PERC / 100, 2)
    else:
        return 0


print(calc_discount(1456.54,'Vespa',month_discount_brands))

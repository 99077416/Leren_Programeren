from test_lib import test, report

def centen_afronden(bedrag):
    AFRONDEN = 5
    return round(bedrag * 100 / AFRONDEN) * AFRONDEN / 100


expected = round(62.60 * 100 / 5) * 5 / 100
calculated = centen_afronden(62.60)
test('afronden', expected, calculated)

expected = round(76.61 * 100 / 5) * 5 / 100
calculated = centen_afronden(76.61)
test('afronden', expected, calculated)

expected = round(28.82 * 100 / 5) * 5 / 100
calculated = centen_afronden(28.82)
test('afronden', expected, calculated)

expected = round(2.23 * 100 / 5) * 5 / 100
calculated = centen_afronden(2.23)
test('afronden', expected, calculated)

expected = round(28.34 * 100 / 5) * 5 / 100
calculated = centen_afronden(28.34)
test('afronden', expected, calculated)

expected = round(-42.85 * 100 / 5) * 5 / 100
calculated = centen_afronden(-42.85)
test('afronden', expected, calculated)

expected = round(31.06 * 100 / 5) * 5 / 100
calculated = centen_afronden(31.06)
test('afronden', expected, calculated)

expected = round(-138.47 * 100 / 5) * 5 / 100
calculated = centen_afronden(-138.47)
test('afronden', expected, calculated)

expected = round(14.88 * 100 / 5) * 5 / 100
calculated = centen_afronden(14.88)
test('afronden', expected, calculated)

expected = round(149.69 * 100 / 5) * 5 / 100
calculated = centen_afronden(149.69)
test('afronden', expected, calculated)





report()
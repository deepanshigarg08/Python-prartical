import decimal
#Source: https://bit.ly/2SfZEtL
def format_e(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

print("Original decimal value: "+ "40800000000.00000000000000")
print("Scientific notation of the said decimal value:")
print(format_e(decimal.Decimal('40800000000.00000000000000')))
print("\nOriginal decimal value: "+ "40000000000.00000000000000")
print("Scientific notation of the said decimal value:")
print(format_e(decimal.Decimal('40000000000.00000000000000')))
print("\nOriginal decimal value: "+ "40812300000.00000000000000")
print("Scientific notation of the said decimal value:")
print(format_e(decimal.Decimal('40812300000.00000000000000')))

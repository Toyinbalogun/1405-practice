# to test abs(x)
x = abs(5-10)
print(x)

m1 = float(input("Enter a distance in miles: "))
m2 = float(input("Enter a distance in miles: "))
m3 = float(input("Enter a distance in miles: "))

km1 = m1 * 1.6
km2 = m2 * 1.6
km3 = m3 * 1.6

closestkm1 = abs(15 - km1)
closestkm2 = abs(15 - km2)
closestkm3 = abs(15 - km3)

if closestkm1 < closestkm2 and closestkm1 < closestkm3:
    print(str(km1) + " is the closest to 15.")

elif closestkm2 < closestkm1 and closestkm2 < closestkm3:
    print(str(km2) + " is the closest to 15.")

else:
    print(str(km3) + " is the closest to 15.")

electric_numbs = [48, 100, 150, 199, 250, 1000]

for electric_numb in electric_numbs:
    if electric_numb < 50:
        print("Price of {:4d} electrical numbers is : {}".format(electric_numb, electric_numb * 15000))
    elif electric_numb > 50 and electric_numb <= 200:
        print("Price of {:4d} electrical numbers is : {}".format(electric_numb, electric_numb * 16500))
    else:
        print("Price of {:4d} electrical numbers is : {}".format(electric_numb, electric_numb * 20000))
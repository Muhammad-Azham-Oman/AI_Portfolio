def celsius_to_fahrenheit(celsius):
    f = (celsius * 9/5)+32
    return f

c = float(input("Enter the temperature in celsius: "))
f = celsius_to_fahrenheit(c)
f_round = round(f,2)
print(f"{c}C° is equal to {f_round}F°")
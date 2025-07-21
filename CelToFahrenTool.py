def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32  
    print(f"{celsius}°C is {fahrenheit:.2f}°F")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F is {celsius:.2f}°C")

while True:
    try:
        user_input = int(input("What do you want? (C to F: 1, F to C: 2, Exit: 3): "))
        if user_input == 1:
            c_to_f = float(input("Please enter the temperature in Celsius that you would like to convert to Fahrenheit: "))
            celsius_to_fahrenheit(c_to_f)
        elif user_input == 2:
            f_to_c = float(input("Please enter the temperature in Fahrenheit that you would like to convert to Celsius: "))
            fahrenheit_to_celsius(f_to_c)
        elif user_input == 3:
            print("Exiting the program.")
            break
        else:
            print("Please enter a valid option (1, 2, or 3).")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

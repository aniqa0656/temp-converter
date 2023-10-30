# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Main function to take user input and perform temperature conversion
def temperature_converter():
    print("Select operation:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        temperature = float(input("Enter temperature: "))
        if choice == '1':
            print("Result: ", celsius_to_fahrenheit(temperature), "Fahrenheit")
        elif choice == '2':
            print("Result: ", fahrenheit_to_celsius(temperature), "Celsius")
        elif choice == '3':
            print("Result: ", celsius_to_kelvin(temperature), "Kelvin")
        elif choice == '4':
            print("Result: ", kelvin_to_celsius(temperature), "Celsius")
        elif choice == '5':
            print("Result: ", fahrenheit_to_kelvin(temperature), "Kelvin")
        elif choice == '6':
            print("Result: ", kelvin_to_fahrenheit(temperature), "Fahrenheit")
    else:
        print("Invalid Input!")

# Call the temperature_converter function
temperature_converter()

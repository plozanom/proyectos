def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_a_kelvin(fahrenheit):
    return ((5/9) * (fahrenheit - 32)) + 273.15

def kelvin_a_fahrenheit(kelvin):
    return ((kelvin - 273.15) * 1.8) + 32
class TemperatureConverter:
    def to_fahrenheit(self, celsius: float) -> float:
        if celsius < 0:
            raise ValueError("Temperature cannot be negative.")
        return celsius * 9 / 5 + 32

    def to_celsius(self, fahrenheit: float) -> float:
        celsius: float = (fahrenheit - 32) * 5 / 9
        if celsius < 0:
            raise ValueError("Temperature cannot be negative.")
        return celsius

try:
    converter = TemperatureConverter()
    print("Fahrenheit:", converter.to_fahrenheit(20))  
    print("Celsius:", converter.to_celsius(77)) 
    print("Fahrenheit:", converter.to_fahrenheit(-20)) 
except ValueError as e:
    print(e)
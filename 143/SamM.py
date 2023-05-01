input_temperature = float(input("Enter a temperature: "))
fah_or_cel = input("Is the temp F for Fahrenheit or C for Celcius? ")
if fah_or_cel == "F":
    temp_in_cel = (input_temperature - 32) * (5/9)
    print("The Celcius equivalent is:", temp_in_cel)
elif fah_or_cel == "C":
    temp_in_fah = (input_temperature * 9/5) + 32
    print("The Fahrenheit equivalent is:", temp_in_fah)
    
    
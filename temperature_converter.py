def temp_converter(value, unit):
    if unit.upper() == "C":
        return (value * (9/5)) + 32
    elif unit.upper() == "F":
        return (value - 32) * 5/9
    else:
        return None
    
body_temp_f = temp_converter(37, "C")
print(f"The body temperature is {body_temp_f:.1f}°F.")

wind_tunnel_c = temp_converter(68, "f")
print(f"Wind tunnel ambient temperature is {wind_tunnel_c:.1f}°C")
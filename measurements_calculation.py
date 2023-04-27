def temperature_calculation(temperature: tuple, value) -> float:
    if (
        temperature == ("C", "C")
        or temperature == ("K", "K")
        or temperature == ("F", "F")
    ):
        return 1 * value
    if temperature == ("C", "K"):
        return value + 273.15
    if temperature == ("C", "F"):
        return value * 9 / 5 + 32
    if temperature == ("K", "C"):
        return value - 273.15
    if temperature == ("K", "F"):
        return (value - 273.15) * 9 / 5 + 32
    if temperature == ("F", "C"):
        return (value - 32) * 5 / 9
    if temperature == ("F", "K"):
        return (value - 32) * 5 / 9 + 273.15


MEASUREMENT_UNITS = {
    "length": {
        ("ml", "ft"): 5280,
        ("ml", "km"): 1.609,
        ("ml", "m"): 1609,
        ("ft", "ml"): 1 / 5280,
        ("ft", "km"): 1 / 3281,
        ("ft", "m"): 1 / 3.281,
        ("km", "ml"): 1 / 1.609,
        ("km", "ft"): 3281,
        ("km", "m"): 1000,
        ("m", "ml"): 1 / 1609,
        ("m", "ft"): 3.281,
        ("m", "km"): 1 / 1000,
    },
    "mass": {
        ("lb", "kg"): 1 / 2.205,
        ("lb", "g"): 453.6,
        ("kg", "lb"): 2.205,
        ("kg", "g"): 1000,
        ("g", "lb"): 1 / 453.6,
        ("g", "kg"): 1 / 1000,
    },
    "temperature": temperature_calculation,
}
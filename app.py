import flet as ft


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


class MeasurementDropdown(ft.UserControl):
    def __init__(self, measurement):
        super().__init__()
        self.measurement = measurement

    def build(self):
        def options_build():
            if self.measurement == "length":
                return ["ml", "ft", "km", "m"]
            elif self.measurement == "mass":
                return ["lb", "kg", "g"]
            elif self.measurement == "temperature":
                return ["C", "K", "F"]

        left_dropdown = ft.Dropdown(text_size=12, width=200, label=self.measurement)
        right_dropdown = ft.Dropdown(text_size=12, width=200, label=self.measurement)
        left_dropdown.options = [ft.dropdown.Option(unit) for unit in options_build()]
        right_dropdown.options = left_dropdown.options
        return ft.Row(
            [left_dropdown, right_dropdown],
            alignment=ft.MainAxisAlignment.CENTER,
        )


def main(page: ft.Page):
    def get_units(e):
        if len(page.controls) > 4:
            page.controls.pop(-3)
        page.controls.insert(2, MeasurementDropdown(e.control.value))
        page.update()

    def calculation(e):
        answer_text.color = ft.colors.BLACK
        answer_text.weight = ft.FontWeight.NORMAL

        if len(page.controls) > 4:
            left_dd = page.controls[2].controls[0].controls[0].value
            right_dd = page.controls[2].controls[0].controls[1].value
            unit_type = page.controls[1].value

            if left_dd == None or right_dd == None:
                index = 0
            elif left_dd == right_dd and unit_type != "temperature":
                index = 1
            elif unit_type == "temperature":
                index = MEASUREMENT_UNITS[unit_type]
            else:
                index = MEASUREMENT_UNITS[unit_type][(left_dd, right_dd)]

            try:
                if index == 0:
                    answer_text.value = "Please, choose unit type!"
                elif unit_type == "temperature":
                    answer_text.value = f"There is {index((left_dd, right_dd), float(user_input.value)) : .3f} {right_dd} in {float(user_input.value) : .3f} {left_dd}"
                else:
                    answer_text.value = f"There is {float(user_input.value) * index : .4f} {right_dd} in {float(user_input.value) : .4f} {left_dd}"
            except:
                answer_text.color = ft.colors.RED
                answer_text.weight = ft.FontWeight.BOLD
                answer_text.value = "Please, enter ONLY numders!!!"
        else:
            answer_text.value = "There is nothing to calculate!"

        page.update()

    # Page settings
    page.title = "Units Converter"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 600
    page.window_width = 600
    page.window_maximizable = False
    page.window_resizable = False

    app_name = ft.Text(value="Units Converter", style=ft.TextThemeStyle.TITLE_LARGE)
    measurement_radio = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(value="length", label="Length"),
                ft.Radio(value="mass", label="Mass"),
                ft.Radio(value="temperature", label="Temperature"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_change=get_units,
    )
    user_input = ft.TextField(data="hello")
    answer_text = ft.Text()
    convert_button = ft.ElevatedButton("Convert", on_click=calculation)

    page.add(
        app_name,
        measurement_radio,
        ft.Row(
            controls=[user_input, convert_button], alignment=ft.MainAxisAlignment.CENTER
        ),
        answer_text,
    )


ft.app(target=main)

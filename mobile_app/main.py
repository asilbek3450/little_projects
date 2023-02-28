import flet
from flet import ElevatedButton, Page, Text, TextField, icons


def main(page: Page):
    def button_clicked(e):
        t.value = (
            f"Textboxes values are:  "
            f"'{tb1.value}', "
            f"'{tb2.value}', "
            f"'{tb3.value}', "
            f"'{tb4.value}', "
            f"'{tb5.value}'."
        )
        page.update()

    t = Text()
    tb1 = TextField(label="Standard")
    tb2 = TextField(label="first name", hint_text="Please enter the first name")
    tb3 = TextField(label="last name", hint_text="Please enter the last name")
    tb4 = TextField(label="With placeholder", hint_text="Please enter text here")
    tb5 = TextField(label="With an icon", icon=icons.EMOJI_EMOTIONS)
    b = ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)


flet.app(target=main)
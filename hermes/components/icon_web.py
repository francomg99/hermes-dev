import reflex as rx
from hermes.styles.styles import Size

def skills(text1:str) -> rx.Component:
    return rx.hstack(
                rx.html(
                    text1
                ),
                align="center",
                align_items="center"
            )
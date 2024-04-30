import reflex as rx
import hermes.styles.styles as styles
from hermes.styles.styles import Size

def title(text: str) -> rx.Component:
    return rx.heading(
        rx.hstack(
            rx.text(text),        
            ),
            align="left",
            padding_top=["0.3em",Size.SMALL.value],
            padding_bottom=["0.3em","0.3em"],
            style=styles.title_style,
            width="100%"
            )
def others_titles(text: str) -> rx.Component:
    return rx.heading(
        rx.hstack(
            rx.text(text),        
            ),
            align="left",
            padding_top=["0.3em",Size.SMALL.value],
            padding_bottom=["0.3em","0.3em"],
            style=styles.other_titles,
            width="100%"
            )    
    
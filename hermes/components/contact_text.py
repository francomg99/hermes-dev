import reflex as rx
from hermes.styles.styles import Color, TextColor, Size

def contact_text(text:str, text2:str, url:str) -> rx.Component:
    return rx.text(
                text, 
                rx.link(
                    rx.text.strong(text2), 
                        href=url,
                        is_external=True,
                        color=TextColor.SECONDARY.value,
                ),
                    style={
                        'font_size':Size.LETTER.value
                        }
            ),
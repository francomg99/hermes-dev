import reflex as rx
from hermes.styles.styles import Color, TextColor, Size

def button (text: str, tag:str, url:str) -> rx.Component:
    return rx.chakra.button(
        text,
        rx.icon(tag=tag, padding_left=Size.SMALL.value, size=30),   
        rx.link(url, external=True),
            style={
                "background":Color.PRIMARY.value,
                "color":TextColor.TERTIARY.value,
                },
            _hover={
                "background": Color.TERTIARY.value,
                "color": TextColor.SECONDARY.value
            },  
            size="md",
    )
import reflex as rx
from hermes.styles.styles import Color, TextColor, Size

def copy_button(tag:str) -> rx.Component:
    return rx.button(
                rx.icon(tag=tag),
                on_click=rx.set_clipboard("francomartinezg@gmail.com"),
                margin_top=Size.SMALL.value,
                margin_bottom=Size.SMALL.value,
                style={
                    "background":Color.PRIMARY.value,
                    "color":TextColor.TERTIARY.value,
                    "width":"80px"
                    },
                _hover={
                    "background": Color.TERTIARY.value,
                    "color": TextColor.SECONDARY.value
                },                    
        )

def send_button(tag:str) -> rx.Component:
    return rx.button(
                rx.icon(tag=tag),
                on_click=rx.redirect(
                    "https://mail.google.com/mail/u/0/#inbox?compose=CllgCKHRtgQwSnjwwPCwbnZvQnfzXGFplcwVmqFpfmjhBlPdtMTTgfsMhkBNrWltKhHbtqPhzsq",
                    external=True                
                ),
                margin_top=Size.SMALL.value,
                margin_bottom=Size.SMALL.value,
                style={
                    "background":Color.PRIMARY.value,
                    "color":TextColor.TERTIARY.value,
                    "width":"80px"
                    },
                _hover={
                    "background": Color.TERTIARY.value,
                    "color": TextColor.SECONDARY.value
                },                    
        )

def icon_link (text:str, url:str) -> rx.Component:
    return rx.link(
                rx.icon(
                    text,
                    _hover={
                        "color": Color.PRIMARY.value
                    }                                
                ),
                href=url,
                is_external=True,
                margin_top=Size.SMALL.value,
                color=Color.SECONDARY.value
            )
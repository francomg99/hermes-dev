import reflex as rx
from hermes.styles.styles import Color, Size, TextColor
from hermes.components.button import button
from hermes.styles.styles import Font

def portafolio_pages_desktop(src:str, strong:str, text: str, name: str, icon: str, url: str)->rx.Component:
      return rx.center(
                    rx.vstack(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src=src,
                                width="100%",
                                height="auto",
                                _hover={
                                    "opacity": 0.8,
                                },
                            ),
                            side="top",
                            pb="current",
                        ),
                            rx.text(
                                rx.text.strong(rx.text.em(strong), color=TextColor.SECONDARY.value), text,
                                style={
                                    'background':Color.ACCENT.value,
                                    'color':TextColor.PRIMARY.value,
                                    'font_size':Size.LETTER.value,
                                }
                        ),
                        width="45vw",
                        bg=Color.ACCENT.value,
                        border_color=Color.TERTIARY.value
                    ),
                    button(name, icon, url)),
                    padding_left=Size.BIG.value,
                    padding_bottom=Size.BIG.value
                ),
def portafolio_pages_mobile(src:str, strong:str, text: str, name: str, icon: str, url: str)->rx.Component:
      return rx.center(
                    rx.vstack(
                    rx.card(
                        rx.inset(
                            rx.image(
                                src=src,
                                width="100%",
                                height="auto",
                                _hover={
                                    "opacity": 0.8,
                                },
                            ),
                            side="top",
                            pb="current",
                        ),
                            rx.text(
                                rx.text.strong(rx.text.em(strong), color=TextColor.SECONDARY.value), text,
                                style={
                                    'background':Color.ACCENT.value,
                                    'color':TextColor.PRIMARY.value,
                                    'font_size':Size.LETTER.value,
                                }
                        ),
                        width="full",
                        bg=Color.ACCENT.value,
                        border_color=Color.TERTIARY.value
                    ),
                    button(name, icon, url)),
                    #padding_left=Size.BIG.value,
                    padding_bottom=Size.BIG.value
                ),
import reflex as rx
from hermes.styles.styles import Size, Color

def navbar() -> rx.Component:
    return rx.hstack(
                rx.link(
                    rx.image(
                        src="hermes_logo.png",
                        alt="Logo de Hermes Web - Fondo azul marino con letras color crema",
                        width="8em",
                        margin_left=[Size.BIG.value,"10em"],
                    )
                ),                
        position="sticky",
        bg=Color.TERTIARY.value,
        z_index="9999",
        top="0",
        width="100%",
        align="center"
    )
    
                
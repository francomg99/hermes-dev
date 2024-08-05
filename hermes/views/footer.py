import reflex as rx

def footer()->rx.Component:
    return rx.center(
        rx.image(
            src="hermes_pilar.png",
            alt="Pilar griego, logo de Hermes Web.",
            width=["7em","10em"]
        ),
        rx.text(
            "©Pagina creada por Franco Martínez",
            color="#828282"
        )
    )
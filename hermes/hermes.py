import reflex as rx
import hermes.styles.styles as styles
from hermes.views.navbar import navbar
from hermes.views.header import header_desktop, header_mobile
from hermes.views.body import body_desktop, body_mobile
from hermes.views.footer import footer

def index() ->rx.Component:
    return rx.box(
        navbar(),
        header_desktop(),
        header_mobile(),
        body_desktop(),
        body_mobile(),
        footer()
        )        

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
    
app.add_page(
    index,
    title="HΞRMΞS DEV | Desarrollo Web y Programación",
    description="Página web de \"HΞRMΞS WEB\""
)
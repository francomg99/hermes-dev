import reflex as rx
from hermes.styles.styles import Size
from hermes.components.title import title
from hermes.components.portafolio_pages import portafolio_pages_desktop, portafolio_pages_mobile
from hermes.components.button import button

def body_desktop() -> rx.Component:
    return rx.desktop_only(
            rx.vstack(
                rx.box(
                    title("PORTAFOLIO"),
                    padding=Size.BIG.value
                ),
                rx.hstack(
                portafolio_pages_desktop(
                    "cache.png",
                    "Caché Bistro ",
                    """es un restaurante ubicado en una de las capitales internacionales del vino,
                    en la provincia de Mendoza, Argentina. Se destaca por su amplia variedad en el sector, 
                    contando con mas de 700 etiquetas y por sus espacios acogedores. 
                    Conocé su página para saber más sobre ellos.""",
                    "Visitar página de Caché Bistro", 
                    "wine", 
                    "https://cachebistro.com.ar",                 
                    ),
                rx.spacer(),
                portafolio_pages_desktop(
                    "jacaranda.png",
                    "Jacaranda Coffee ",
                    """es un proyecto ficticio diseñado con fines demostrativos y educativos. 
                    Cualquier similitud con nombres, marcas o entidades reales es pura coincidencia. 
                    Este proyecto se ha desarrollado únicamente con propósitos de práctica 
                    y no representa una empresa existente.""",
                    "Visitar página de Jacaranda Coffee", 
                    "coffee",
                    "https://jacarandacoffee.es/",                     
                    ),
                ),
                portafolio_pages_desktop(
                    "hermes_page.png",
                    "Hermes Web ",
                    """es el portafolio de Franco Martínez. Aquí encontraras sus trabajos más recientes como también los
                    enlaces de interes para poder contactarte con él y consultar todas tus dudas.""",
                    "Enviar mensaje a Hermes Web", 
                    "send", 
                    "https://hermesdev.es",                     
                    ),
                width="100%",
            )    
    )            
def body_mobile() -> rx.Component:
    return rx.mobile_and_tablet(
            rx.vstack(
                rx.box(
                    title("PORTAFOLIO"),
                ),
                portafolio_pages_mobile(
                    "cache.png",
                    "Caché Bistro ",
                    """es un restaurante ubicado en una de las capitales internacionales del vino,
                    en la provincia de Mendoza, Argentina. Se destaca por su amplia variedad en el sector, 
                    contando con mas de 700 etiquetas y por sus espacios acogedores. 
                    Conocé su página para saber más sobre ellos.""",
                    "Visitar página de Caché Bistro", 
                    "wine", 
                    "https://cachebistro.com.ar",                   
                ),
                
                portafolio_pages_mobile(
                    "jacaranda.png",
                    "Jacaranda Coffee ",
                    """es un proyecto ficticio diseñado con fines demostrativos y educativos. 
                    Cualquier similitud con nombres, marcas o entidades reales es pura coincidencia. 
                    Este proyecto se ha desarrollado únicamente con propósitos de práctica 
                    y no representa una empresa existente.""",
                    "Visitar página de Jacaranda Coffee", 
                    "coffee",
                    "https://jacarandacoffee.es/",            
                ),
                portafolio_pages_mobile(
                    "hermes_page.png",
                    "Hermes Web ",
                    """es el portafolio de Franco Martínez. Aquí encontraras sus trabajos más recientes como también los
                    enlaces de interes para poder contactarte con él y consultar todas tus dudas.""",
                    "Enviar mensaje a Hermes Web", 
                    "send", 
                    "https://hermesdev.es",                     
                ),
                width="100%",
                padding=Size.SMALL.value,
                margin_top=Size.MEDIUM.value,
                spacing="4"
            )    
    )

    
            
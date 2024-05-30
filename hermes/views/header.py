import reflex as rx
from hermes.styles.styles import Size, Color, TextColor
from hermes.components.icon_web import skills
from hermes.components.title import title, others_titles
from hermes.components.contact_button import copy_button, send_button, icon_link
from hermes.components.contact_text import contact_text

def header_desktop() -> rx.Component:
    return rx.desktop_only(
            rx.hstack(
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.avatar(
                            name="Franco Martínez",
                            size="9",
                            src="/foto_franco.jpeg",
                            radius="full",
                            color=TextColor.PRIMARY.value,
                            bg=Color.ACCENT.value,
                            border=f"4px solid {Color.TERTIARY.value}"
                        ),
                    padding=Size.DEFAULT.value,
                    position="relative"
                    ),
                    rx.vstack(
                        rx.heading(
                            "Franco Martínez",
                            size="7"
                        ),
                        rx.text.strong(
                            "@francomg99",
                            margin_top=Size.ZERO.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':Size.LETTER.value}
                        ),
                        rx.hstack(
                            icon_link(
                                "github",
                                "https://github.com/francomg99"
                            ),
                            icon_link(
                                "instagram",
                                "https://www.instagram.com/hermeswebs/"
                            ),
                            icon_link(
                                "linkedin",
                                "https://www.linkedin.com/in/francomg99/"
                            ),
                            icon_link(
                                "mail",
                                "https://mail.google.com/mail/u/7/#inbox?compose=CllgCJTLpLqMGczKsnjBJcXLPPbBGSVXjdRnGJvjSLRXNpzxKsHnVwfXrvPmdphBQTJVPfNTMpg"
                            ),
                            icon_link(
                                "sticky_note",
                                "https://drive.google.com/file/d/1z7WwL7m_GnrV2cWFhmmef--13r5i6lpu/view?usp=sharing"
                            )                        ),
                    spacing="0",
                    align_items="start"                        
                    ),
                align="center",
                spacing="0"
                ),
                rx.box(
                rx.text(
                    """¡Bienvenidx a mi portafolio!. Soy un iniciado desarrollador Front-End en Python, apasionado por 
                    el diseño web y la programación. 
                    ¡Explora mis proyectos y acompáñame en este viaje de desarrollo!"""
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.chakra.button(
                                "Ver más", 
                                margin_top=Size.SMALL.value,
                                style={
                                    "background":Color.PRIMARY.value,
                                    "color":TextColor.TERTIARY.value,
                                    "width":"80px"
                                },
                                _hover={
                                    "background": Color.TERTIARY.value,
                                    "color": TextColor.SECONDARY.value
                                }, 
                            ),),
                    rx.dialog.content(
                        rx.dialog.title(others_titles("Sobre mí!")),
                        rx.dialog.description(
                            """Soy Franco, un apasionado por la programación y el desarrollo web Front-End que esta entrando
                            en este mundo, cada día queriendo aprender algo nuevo.""",
                        ),
                        rx.dialog.description(
                            """Me gusta el café por lo que sería un sueño poder abrir mi propia cafetería y 
                            programar desde allí.""",
                        ),
                        rx.dialog.description(
                            """Estoy en búsqueda de mi primer experiencia, mientras tanto voy siendo alguien
                            autodidacta que va realizando proyectos para sí mismo, algunos reales y otros ficticios.""",
                        ),                        
                        rx.dialog.close(
                            rx.chakra.button(
                                "Cerrar", 
                                padding=Size.SMALL.value,
                                margin_top=Size.MEDIUM.value,
                                style={
                                    "background":Color.PRIMARY.value,
                                    "color":TextColor.PRIMARY.value,
                                    "width":"80px"
                                },
                                _hover={
                                    "background": Color.ACCENT.value,
                                    "color": TextColor.SECONDARY.value
                                },  
                            ),
                        ),
                        bg=Color.TERTIARY.value,
                        color=TextColor.PRIMARY.value,
                        border=f"2px solid {Color.PRIMARY.value}",
                        style={
                            'text_indent':"1em"
                        }
                    ),
                ),
                padding_left=Size.DEFAULT.value,
                font_size=Size.LETTER.value
                ),
                width="33%",
            ),
                rx.box(
                rx.vstack(
                        title(
                            "SKILLS",
                        ),
                    rx.vstack(
                        rx.text.strong(
                            "Lenguajes de programación",
                            margin_top=Size.ZERO.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':"1.25em"}
                        ),
                        rx.hstack(
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/PYTHON-%230A151C?style=for-the-badge&logo=python&logoColor=white&labelColor=%233776AB">"""

                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/CSS3-%230A151C?style=for-the-badge&logo=css3&logoColor=white&labelColor=%231572B6">"""
                        )                      
                        ),
                        rx.text.strong(
                            "Frameworks y herramientas",
                            margin_top=Size.SMALL.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':"1.25em"}
                        ),
                        rx.hstack(
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/REFLEX-%230A151C?style=for-the-badge&logo=resend&logoColor=white&labelColor=%23181717">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/VISUAL%20STUDIO%20CODE-%230A151C?style=for-the-badge&logo=visualstudiocode&labelColor=%23007ACC">"""
                        ),
                        ),
                      rx.text.strong(
                            "Portfolio",
                            margin_top=Size.SMALL.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':"1.25em"}
                        ),
                        rx.hstack(
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/GIT--HUB-%230A151C?style=for-the-badge&logo=github&labelColor=%23181717">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/HERMES-%230A151C?style=for-the-badge&logo=hetzner&labelColor=%23D1181E">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/LINKEDIN-%230A151C?style=for-the-badge&logo=linkedin&labelColor=%230A66C2">"""
                        ),    
                        ),                    
                        align_items="start",
                        spacing="1"                        
                    ),                      
                spacing="2"
                ),
                #width="33%",
                padding_top="2em",
            ),
            rx.box(
                rx.vstack(
                        title(
                            "CONTACTO",
                        ),
                    rx.vstack(
                        rx.input(
                            default_value="hermesdev.info@gmail.com",
                            style={
                                "width": "300px",        # Controla el ancho
                                "height": "40px",        # Controla el alto
                                "background_color": "rgba(163, 33, 38, 0.7)",  # Color de fondo
                                "color": TextColor.TERTIARY.value,     # Color del texto
                                "font_size": Size.LETTER.value      # Tamaño del texto
                            }
                        ),
                    rx.hstack(
                        copy_button(
                            "copy",
                        ),
                        send_button(
                            "send"
                        ) 
                    ),
                    rx.vstack(
                        contact_text(
                            "✦ Mandanos un correo también haciendo ",
                            "Click Aquí.",
                            "https://mail.google.com/mail/u/0/#inbox?compose=CllgCKHRtgQwSnjwwPCwbnZvQnfzXGFplcwVmqFpfmjhBlPdtMTTgfsMhkBNrWltKhHbtqPhzsq"   
                        ),
                        contact_text(
                            "✦ O si prefieres la comodidad de ",
                            "What's App.",
                            "https://wa.me/+34625779836"
                        ),
                        contact_text(
                            "✦ Antes que nada revisa nuestro ",
                            "Instagram.",
                            "https://www.instagram.com/hermeswebs"
                        )                  
                    )                     
                    ),                      
                spacing="2"
                ),
                padding_top=Size.BIG.value,
            ), 
            spacing="9" #Mueve las skills más a la derecha        
    )
    ) 
def header_mobile() -> rx.Component:
    return rx.mobile_and_tablet(
            rx.vstack(
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.avatar(
                            name="Franco Martínez",
                            size="9",
                            src="/foto_franco.jpeg",
                            radius="full",
                            color=TextColor.PRIMARY.value,
                            bg=Color.ACCENT.value,
                            border=f"4px solid {Color.TERTIARY.value}"
                        ),
                    padding=Size.MEDIUM.value,
                    position="relative"
                    ),
                    rx.vstack(
                        rx.heading(
                            "Franco Martínez",
                            size="7"
                        ),
                        rx.text.strong(
                            "@francomg99",
                            margin_top=Size.ZERO.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':Size.LETTER.value}
                        ),
                        rx.hstack(
                            icon_link(
                                "github",
                                "https://github.com/francomg99"
                            ),
                            icon_link(
                                "instagram",
                                "https://www.instagram.com/francomartinezg_/"
                            ),
                            icon_link(
                                "linkedin",
                                "https://www.linkedin.com/in/francomg99/"
                            ),
                            icon_link(
                                "mail",
                                "https://mail.google.com/mail/u/0/#inbox?compose=CllgCKHRtgQwSnjwwPCwbnZvQnfzXGFplcwVmqFpfmjhBlPdtMTTgfsMhkBNrWltKhHbtqPhzsq"
                            ),
                            icon_link(
                                "sticky_note",
                                "https://drive.google.com/file/d/1z7WwL7m_GnrV2cWFhmmef--13r5i6lpu/view?usp=sharing"
                            )
                        ),
                    spacing="0",
                    align_items="start"                        
                    ),
                align="center",
                spacing="0"
                ),
                rx.box(
                rx.text(
                    """¡Bienvenidx a mi portafolio!. Soy un iniciado desarrollador Front-End en Python, apasionado por 
                    el diseño web y la programación. 
                    ¡Explora mis proyectos y acompáñame en este viaje de desarrollo!"""
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                                "Ver más", 
                                margin_top=Size.SMALL.value,
                                style={
                                    "background":Color.PRIMARY.value,
                                    "color":TextColor.TERTIARY.value,
                                    "width":"80px"
                                },
                                _hover={
                                    "background": Color.TERTIARY.value,
                                    "color": TextColor.SECONDARY.value
                                }, 
                            ),),
                    rx.dialog.content(
                        rx.dialog.title(others_titles("Sobre mí!")),
                        rx.dialog.description(
                            """Soy Franco, un apasionado por la programación y el desarrollo web Front-End que esta entrando
                            en este mundo, cada día queriendo aprender algo nuevo.""",
                        ),
                        rx.dialog.description(
                            """Me gusta el café por lo que sería un sueño poder abrir mi propia cafetería y 
                            programar desde allí.""",
                        ),
                        rx.dialog.description(
                            """Estoy en búsqueda de mi primer experiencia, mientras tanto voy siendo alguien
                            autodidacta que va realizando proyectos para sí mismo, algunos reales y otros ficticios.""",
                        ),                        
                        rx.dialog.close(
                            rx.button(
                                "Cerrar", 
                                margin_top=Size.BIG.value,
                                style={
                                    "background":Color.PRIMARY.value,
                                    "color":TextColor.PRIMARY.value,
                                    "width":"80px"
                                },
                                _hover={
                                    "background": Color.ACCENT.value,
                                    "color": TextColor.SECONDARY.value
                                },  
                            ),
                        ),
                        bg=Color.TERTIARY.value,
                        color=TextColor.PRIMARY.value,
                        border=f"2px solid {Color.PRIMARY.value}",
                        style={
                            'text_indent':"1em"
                        }
                    ),
                ),                
                padding=Size.SMALL.value,
                font_size=Size.LETTER.value
                ),
            ),
                rx.box(
                rx.vstack(
                        title(
                            "SKILLS",
                        ),
                    rx.vstack(
                        rx.text.strong(
                            "Lenguajes de programación",
                            margin_top=Size.ZERO.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':Size.LETTER.value}
                        ),
                        rx.hstack(
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/PYTHON-%230A151C?style=for-the-badge&logo=python&logoColor=white&labelColor=%233776AB">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/CSS3-%230A151C?style=for-the-badge&logo=css3&logoColor=white&labelColor=%231572B6">"""
                        )                       
                        ),
                        rx.text.strong(
                            "Frameworks y herramientas",
                            margin_top=Size.SMALL.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':Size.LETTER.value}
                        ),
                        rx.hstack(
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/REFLEX-%230A151C?style=for-the-badge&logo=resend&logoColor=white&labelColor=%23181717">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/VISUAL%20STUDIO%20CODE-%230A151C?style=for-the-badge&logo=visualstudiocode&labelColor=%23007ACC">"""
                        ),
                        ),
                      rx.text.strong(
                            "Portfolio",
                            margin_top=Size.SMALL.value,
                            color=Color.PRIMARY.value,
                            style={'font_size':Size.LETTER.value}
                        ),
                        rx.hstack(
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/GIT--HUB-%230A151C?style=for-the-badge&logo=github&labelColor=%23181717">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/HERMES-%230A151C?style=for-the-badge&logo=hetzner&labelColor=%23D1181E">"""
                        ),
                        skills(
                            """<img alt="Static Badge" src="https://img.shields.io/badge/LINKEDIN-%230A151C?style=for-the-badge&logo=linkedin&labelColor=%230A66C2">"""
                        ),    
                        ),                    
                        align_items="start",
                        spacing="1"                        
                    ),                      
                spacing="2"
                ),
                padding=Size.SMALL.value,
            ),
            rx.box(
                rx.vstack(
                        title(
                            "CONTACTO",
                        ),
                    rx.vstack(
                        rx.input(
                            default_value="francomartinezg99@gmail.com",
                            style={
                                "width": "300px",        # Controla el ancho
                                "height": "40px",        # Controla el alto
                                "background_color": "rgba(163, 33, 38, 0.7)",  # Color de fondo
                                "color": TextColor.TERTIARY.value,     # Color del texto
                                "font_size": Size.LETTER.value      # Tamaño del texto
                            }
                        ),
                    rx.hstack(
                        copy_button(
                            "copy"
                        ),
                        send_button(
                            "send"
                        ) 
                    ),
                    rx.vstack(
                        contact_text(
                            "✦ Mandanos un correo también haciendo ",
                            "Click Aquí.",
                            "https://mail.google.com/mail/u/0/#inbox?compose=CllgCKHRtgQwSnjwwPCwbnZvQnfzXGFplcwVmqFpfmjhBlPdtMTTgfsMhkBNrWltKhHbtqPhzsq"   
                        ),
                        contact_text(
                            "✦ O si prefieres la comodidad de ",
                            "What's App.",
                            "https://wa.me/+342625779836"
                        ),
                        contact_text(
                            "✦ Antes que nada revisa nuestro ",
                            "Instagram.",
                            "https://www.instagram.com/francomartinezg_/"
                        )                  
                    )                     
                    ),                      
                spacing="2"
                ),
                padding=Size.SMALL.value,
            ), 
            spacing="4" #Mueve las skills más a la derecha        
    )
    )
    

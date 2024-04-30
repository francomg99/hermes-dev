from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "1em"
    LETTER = "1.15em"
    DEFAULT = "1.5em"
    BIG = "2em"
    METHOD_TITLE="2.5em"
    TITLE= "4em"
    BUTTON = "3em"
    VERY_BIG = "4em"
    
STYLESHEETS = [
        "https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Rubik+Doodle+Shadow&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.ACCENT.value,
}

title_style = dict(
    width="100%",
    font_size=[Size.METHOD_TITLE.value, Size.METHOD_TITLE.value],
    font_family=Font.TITLE.value,
    color=TextColor.SECONDARY.value,
    )

other_titles = dict(
    width="100%",
    font_size=[Size.BIG.value, Size.BIG.value],
    font_family=Font.TITLE.value,
    color=TextColor.SECONDARY.value,
    )
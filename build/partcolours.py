"""One colour for each part of the book, used on its cover in the PDF, the EPUB and the site."""
import re

COLOURS = {
    "I": "#8a5a1c",      # Origins: ochre
    "II": "#7a2e25",     # Conquest: red
    "III": "#1f4a52",    # Faith: blue-green
    "IV": "#27476e",     # Expansion: sea blue
    "V": "#3d5a2a",      # Wealth: green
    "VI": "#3a3a40",     # War: iron
    "VII": "#5a2f55",    # Dominion: purple
    "VIII": "#5c5148",   # Decline: ash
}
DEFAULT = "#b5523b"


def split(subtitle):
    """'Part III: Faith' gives ('III', 'Faith', colour). Anything else gives ('', subtitle, default colour)."""
    m = re.match(r"Part ([IVX]+):\s*(.+)", subtitle)
    if m:
        return m.group(1), m.group(2), COLOURS.get(m.group(1), DEFAULT)
    return "", subtitle, DEFAULT

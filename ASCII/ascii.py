# import pywhatkit as kit

# kit.image_to_ascii_art("./spire.png", "ascii")

import ascii_magic

art = ascii_magic.AsciiArt.from_image("spire.png")

art.to_terminal(columns=100, width_ratio=2, char="#")

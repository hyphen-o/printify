from typing import NamedTuple

THEMES = {
  "red": "\033[31m",
  "blue": "\033[34m",
  "green": "\033[32m",
  "yellow": "\033[33m",
  "white": "\033[37m",
}

END = "\033[0m"

def ColoredText(text: str, color="white"):
  return THEMES[color] + text + END
import sys
sys.path.append("../")
from constants.theme import ColoredText

def logging(text: str, dir='./log'):
  print(ColoredText("-------------------------------------", "green"))
  print(ColoredText("               logging               ", "green"))
  print(ColoredText("-------------------------------------", "green"))
  print(ColoredText(text, "green"))

  
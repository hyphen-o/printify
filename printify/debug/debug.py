from constants.theme import ColoredText

def info(text):
  print(ColoredText("-------------------------------------", "red"))
  print(ColoredText("                debug                ", "red"))
  print(ColoredText("-------------------------------------", "red"))
  print(ColoredText(text, "red"))
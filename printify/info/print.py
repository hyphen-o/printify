from constants.theme import ColoredText

def info(text):
  print(ColoredText("-------------------------------------", "yellow"))
  print(ColoredText("                 info                ", "yellow"))
  print(ColoredText("-------------------------------------", "yellow"))
  print(ColoredText(text, "yellow"))
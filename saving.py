import pyperclip
import sys

sys.path.append("/main.py")
from main import zufallszahl

pyperclip.copy(zufallszahl)
spam = pyperclip.paste()
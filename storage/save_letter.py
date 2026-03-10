import os
from datetime import datetime
from config import SAVE_FOLDER

def save_letter(letter):

    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    filename = f"{datetime.now().strftime('%Y_%m_%d')}.txt"
    path = os.path.join(SAVE_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(letter)

    return path
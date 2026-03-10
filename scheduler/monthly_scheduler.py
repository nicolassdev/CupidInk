from datetime import datetime
from generator.letter_generator import generate_letter
from storage.save_letter import save_letter
from config import LETTER_DAY

def check_and_generate():

    today = datetime.now()

    if today.day == LETTER_DAY:

        letter = generate_letter()

        save_letter(letter)

        print("💌 Love letter created!")
from flask import Flask, render_template, jsonify
import os
from datetime import datetime
from scheduler.monthly_scheduler import check_and_generate
from config import LETTER_DAY, SAVE_FOLDER
from generator.letter_generator import generate_letter
from storage.save_letter import save_letter

app = Flask(__name__)

@app.route("/")
def home():

    letters = []

    if os.path.exists(SAVE_FOLDER):
        for file in os.listdir(SAVE_FOLDER):
            with open(os.path.join(SAVE_FOLDER, file), encoding="utf-8") as f:
                letters.append({
                    "date": file.replace(".txt",""),
                    "content": f.read()
                })

    letters.reverse()

    return render_template("index.html", letters=letters)


@app.route("/generate")
def generate():

    today = datetime.now()

    if today.day != LETTER_DAY:
        return jsonify({
            "status": "not_allowed",
            "message": f"CupidLink only writes letters on the {LETTER_DAY}th of every month 💘"
        })

    letter = generate_letter()
    save_letter(letter)

    return jsonify({
        "status": "success",
        "message": "Your love letter has been created 💌"
    })


if __name__ == "__main__":
    app.run(debug=True)
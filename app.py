from flask import Flask, render_template, jsonify
import os
from datetime import datetime
from scheduler.monthly_scheduler import check_and_generate
from config import LETTER_DAY, SAVE_FOLDER
from generator.letter_generator import generate_letter
from storage.save_letter import save_letter
from send_email import send_email  # import email function

app = Flask(__name__)

@app.route("/")
def home():
    """Render the main page with all letters."""
    letters = []

    if os.path.exists(SAVE_FOLDER):
        for file in os.listdir(SAVE_FOLDER):
            with open(os.path.join(SAVE_FOLDER, file), encoding="utf-8") as f:
                letters.append({
                    "date": file.replace(".txt", ""),
                    "content": f.read()
                })

    letters.reverse()  # latest letters first
    return render_template("index.html", letters=letters)


@app.route("/generate")
def generate():
    """Generate a new letter (only allowed on the 11th)."""
    today = datetime.now()

    if today.day != LETTER_DAY:
        return jsonify({
            "status": "not_allowed",
            "message": f"❤️ CupidLink only writes letters on the {LETTER_DAY}th of each month. Come back then for a beautiful surprise!"
        })

    # Generate and save the letter
    letter = generate_letter()
    file_path = save_letter(letter)

    # Send email automatically (optional)
    # Replace with your partner's email or use multiple recipients
    partner_email = os.getenv("PARTNER_EMAIL")
    if partner_email:
        send_email(partner_email)

    return jsonify({
        "status": "success",
        "message": f"💌 Your love letter has been created and saved to {file_path}!"
    })


if __name__ == "__main__":
    # Get port from environment for hosting services like Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
cupidlink/
│
├── app.py # Main website + UI
├── config.py # App configuration (LETTER_DAY, SAVE_FOLDER, etc.)
├── requirements.txt # Python dependencies
├── send_email.py # Email sending logic
├── send_email_script.py # Script to trigger email generation (GitHub Actions)
│
├── data/
│ └── message_parts.py # Random love letter parts
│
├── generator/
│ └── letter_generator.py # Generates love letters
│
├── scheduler/
│ └── monthly_scheduler.py # Checks if it's the 11th and generates letter
│
├── storage/
│ └── save_letter.py # Save letters to local folder
│
├── templates/
│ └── index.html # Romantic website UI
│
├── letters/ # Saved letters folder
│
└── .github/
└── workflows/
└── cupidlink_email.yml # GitHub Actions workflow to run email every 11th

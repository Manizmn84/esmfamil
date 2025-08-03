# EsmFamil Game (Persian "Name Game")

This is a simple Python project that implements the logic of a Persian word game called "Esm o Famil" (meaning "Name and Family"). Players submit answers to different categories (such as name, color, country, food, etc.) starting with a specific letter. The game then stores and processes these answers.

## 📁 Project Structure

esmfamil/
├── esm_famil_data.csv # Allowed values in CSV format (e.g., mani,nima,alex,...)
├── game.py # Main game logic (add participant, read data, etc.)


## 🧠 Game Features

- Load valid words from a `.csv` file (e.g., names).
- Add participants and store their answers.
- Automatically strip unnecessary spaces from user inputs.

> 💡 *Note: This version does not include scoring logic or duplicate detection.*

## 🧪 How to Use

1. Clone the repo or copy the files.
2. Make sure your `esm_famil_data.csv` looks like:
mani,nima,alex,sara,elham

java
Copy
Edit
3. Use the `add_participant()` function like this:

```python
add_participant(
 participant='salib',
 answers={
     'esm': 'بردیا',
     'famil': 'بابایی',
     'keshvar': 'باربادوس',
     'rang': 'بنفش',
     'ashia': 'بمب',
     'ghaza': 'باقالیپلو'
 }
)

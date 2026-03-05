from openai import OpenAI
import os

# Create client (automatically reads OPENAI_API_KEY from environment)
from google import genai

client = genai.Client(api_key="AIzaSyCccNAVTzKDS3_g2oPf0xosEEBhtmd-NBo")



def get_decision_context():
    return input("Enter decision context: ")

def get_options():
    n = int(input("How many options? "))
    options = []
    for i in range(n):
        options.append(input(f"Enter option {i+1}: "))
    return options



def generate_questions(context):
    prompt = f"""
    Generate 5 evaluation questionsn for: {context}.
    Questions must allow rating from 1 to 5.
    Return as numbered list only.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    questions_text = response.text
    return parse_questions(questions_text)

def parse_questions(text):
    lines = text.split("\n")
    questions = []
    for line in lines:
        if line.strip():
            cleaned = line.lstrip("0123456789. ").strip()
            questions.append(cleaned)
    return questions

def collect_scores(options, questions):
    scores = {option: [] for option in options}
    
    for q in questions:
        print(f"\nQuestion: {q}")
        for option in options:
            rating = int(input(f"Rate {option} (1-5): "))
            scores[option].append(rating)

    return scores

def calculate_totals(scores):
    return {opt: sum(vals) for opt, vals in scores.items()}

def explain(best_option, totals):
    print(f"\nBest Option: {best_option}")
    print(f"Score: {totals[best_option]}")

def main():
    context = get_decision_context()
    options = get_options()
    questions = generate_questions(context)
    scores = collect_scores(options, questions)
    totals = calculate_totals(scores)
    
    best = max(totals, key=totals.get)
    explain(best, totals)

if __name__ == "__main__":
    main()
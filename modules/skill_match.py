import pandas as pd

def extract_skills(text):
    skills_df = pd.read_csv("data/skills.csv", header=None)
    skills = skills_df[0].tolist()

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
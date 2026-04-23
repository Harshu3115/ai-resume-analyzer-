import re

SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "mysql", "mongodb",
    "flask", "django", "spring", "spring boot",
    "html", "css", "javascript", "react", "node",
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit-learn",
    "git", "docker", "aws", "api"
]

def extract_entities(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if re.search(rf"\b{re.escape(skill)}\b", text_lower):
            found_skills.append(skill)

    return {"SKILL": list(set(found_skills))}
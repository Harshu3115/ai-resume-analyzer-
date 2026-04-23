import re

# Load NER model
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

ner_pipeline = pipeline(
    "ner",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple"
)

# 🔥 Custom Skill List (VERY IMPORTANT)
SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "mysql", "mongodb",
    "flask", "django", "spring", "spring boot",
    "html", "css", "javascript", "react", "node",
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit-learn",
    "git", "docker", "aws", "api"
]

def extract_entities(text):
    result = {}

    # 🔹 NER extraction
    entities = ner_pipeline(text)

    for ent in entities:
        label = ent['entity_group']
        word = ent['word']

        if label not in result:
            result[label] = []

        result[label].append(word)

    # 🔹 Clean duplicates
    for key in result:
        result[key] = list(set(result[key]))

    # 🔥 SKILL EXTRACTION (IMPORTANT UPGRADE)
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if re.search(rf"\b{re.escape(skill)}\b", text_lower):
            found_skills.append(skill)

    result['SKILL'] = list(set(found_skills))

    return result
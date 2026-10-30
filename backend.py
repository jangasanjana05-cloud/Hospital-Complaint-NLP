import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("complaints.csv")
df = df.dropna(subset=["complaint", "category", "priority"])

def build_model(target):
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("classifier", MultinomialNB())
    ])

    model.fit(
        df["complaint"].astype(str),
        df[target].astype(str)
    )
    return model

category_model = build_model("category")
priority_model = build_model("priority")

def predict_complaint(complaint):
    if not complaint.strip():
        return "Please enter a complaint.", "Not predicted"

    category = category_model.predict([complaint])[0]
    priority = priority_model.predict([complaint])[0]

    return category, priority

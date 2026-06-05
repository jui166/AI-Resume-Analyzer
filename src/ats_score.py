from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, job_description):

    documents = [resume_text, job_description]

    vectorizer = CountVectorizer().fit_transform(documents)

    similarity = cosine_similarity(vectorizer)

    score = similarity[0][1] * 100

    return round(score, 2)
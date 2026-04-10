from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text1 = "AI system for detecting fraud"
text2 = "Machine learning model for fraud detection"

embeddings = model.encode([text1, text2])

print("Setup working fine")
import pandas as pd
import torch
import transformers
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from fastai.text.all import *
import re
import fastai
from sentence_transformers import SentenceTransformer, util

# Load the tokenizer and model
tokenizer = GPT2TokenizerFast.from_pretrained("skt/kogpt2-base-v2")
model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")

# Read the CSV dataset
df = pd.read_excel('models/sejong1000QA.xlsx')

# Extract questions and answers from the DataFrame
questions = df['Q'].tolist()
answers = df['A'].tolist()
labels = df['label'].tolist()

# Define the tokenizer for FastAI
class TransformersTokenizer(Transform):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def encodes(self, x):
        toks = self.tokenizer.tokenize(x)
        return tensor(self.tokenizer.convert_tokens_to_ids(toks))

    def decodes(self, x):
        return TitledStr(self.tokenizer.decode(x.cpu().numpy()))


# Load the pre-trained sentence transformer model
sentence_transformer_model = SentenceTransformer('all-MiniLM-L6-v2')


class IntentModel:
    # Define the answer generator function
    def generate_answer(question):
        # Encode the input question
        question_embedding = sentence_transformer_model.encode([question])

        # Compute cosine similarities between the question and all stored questions
        similarities = util.pytorch_cos_sim(question_embedding, question_embeddings).flatten()

        # Find the index of the most similar question
        most_similar_idx = similarities.argmax().item()

        # Retrieve the corresponding answer
        answer = answers[most_similar_idx]
        lab = labels[most_similar_idx]

        return answer, lab


# Encode all stored questions
question_embeddings = sentence_transformer_model.encode(questions)

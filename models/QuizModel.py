import torch
import transformers
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from fastai.text.all import *
import re
import fastai
from sentence_transformers import SentenceTransformer, util

# Load the tokenizer and model
tokenizer = GPT2TokenizerFast.from_pretrained("skt/kogpt2-base-v2")
'''model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")'''

# Read the CSV dataset
df = pd.read_excel('models/Quiz_Dataset.xlsx')


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

class QuizModel:
    # Define the answer generator function
    def get_quiz(question):
        lab = int(question[-1])
        filtered_df = df[df['label'] == lab]

        # Extract questions and answers from the filtered DataFrame
        quizes = filtered_df['Q'].tolist()
        answers = filtered_df['A'].tolist()

        # Encode all stored questions
        quiz_embeddings = sentence_transformer_model.encode(quizes)

        # Encode the input question
        quiz_embedding = sentence_transformer_model.encode([question])

        # Compute cosine similarities between the question and the stored question
        similarity = util.pytorch_cos_sim(quiz_embedding, quiz_embeddings).flatten()

        # Find the index of the most similar question
        most_similar_idx = similarity.argmax().item()

        # Retrieve the corresponding quiz
        quiz = quizes[most_similar_idx]
        answer = answers[most_similar_idx]

        return quiz, answer


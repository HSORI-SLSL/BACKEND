from tensorflow import keras
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf
class IntentModel:

    def generate_answer(question):
        question = [question]

        # 모델 로드
        '''load_options = tf.saved_model.LoadOptions(experimental_io_device="/job:localhost")
        model = tf.saved_model.load("models/IntentModel.h5", options=load_options)'''
        '''model = tf.keras.models.load_model("models/IntentModel.h5",
                                           custom_objects={'KerasLayer': hub.KerasLayer})'''

        '''load_options = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost', )'''
        model = tf.keras.models.load_model("models/IntentModel.h5", custom_objects={'KerasLayer': hub.KerasLayer})
        return [np.argmax(pred) for pred in model.predict(question)][0]



'''# Define the tokenizer for FastAI
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
'''
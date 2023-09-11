from transformers import AutoTokenizer, pipeline, logging
import logging


class GenerateModel:

    def generate_text(self, prompt, label):
        model = "silok"
        model_name = "NousResearch/Llama-2-7b-hf"

        # Load LLaMA tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training

        # Ignore warnings
        logging.set_verbosity(logging.CRITICAL)

        # Run text generation pipeline with our next model
        pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
        result = pipe(f"<s>[Q] {prompt} [/Q] [label] {label} [/label]")
        generated_text = result[0]['generated_text']

        return generated_text



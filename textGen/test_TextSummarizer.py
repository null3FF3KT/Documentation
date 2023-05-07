from transformers import PegasusTokenizer, PegasusForConditionalGeneration, TFPegasusForConditionalGeneration

# Let's load the model and the tokenizer 
model_name = "human-centered-summarization/financial-summarization-pegasus"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name) # If you want to use the Tensorflow model 
                                                                    # just replace with TFPegasusForConditionalGeneration


def main():
    print("Welcome to a Text Summarizer")

    while True:
        try:

# Some text to summarize here
            text_to_summarize = input("Enter text to summarize (or type 'exit' to quit): ")
            if text_to_summarize.lower() == "exit":
                break
# Tokenize our text
# If you want to run the code in Tensorflow, please remember to return the particular tensors as simply as using return_tensors = 'tf'
            input_ids = tokenizer(text_to_summarize, return_tensors="pt").input_ids

# Generate the output (Here, we use beam search but you can also use any other strategy you like)
            output = model.generate(
                input_ids, 
                max_length=250, 
                num_beams=15, 
                early_stopping=False
            )
        # Finally, we can print the generated summary
            print(tokenizer.decode(output[0], skip_special_tokens=True))

        except ValueError:
            print("Invalid input.  Try something shorter.")
    
    print("Thank you for trying out this summarizer!")

if __name__ == "__main__":
    main()




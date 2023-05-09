
from transformers import pipeline; 
# Let's load the model and the tokenizer 
model_name = "google/flan-t5-xl"
task_name = "text2text-generation"
generator = pipeline(task=task_name, model=model_name)


def main():
    print("Welcome to a Text Generator")

    while True:
        try:

# Some text to prompt text generation
            promptText_to_generateText = input("Enter text prompt (or type 'exit' to quit): ")
            if promptText_to_generateText.lower() == "exit":
                break

# Generate the output
            
        # Finally, we can print the generated summary
            print(generator(promptText_to_generateText))

        except ValueError:
            print("Error:" + ValueError)
    
    print("Thank you for trying out this generator!")

if __name__ == "__main__":
    main()




# 📝 Import the necessary modules
import requests
import json
from chain import MinimalChainable  # Ensure that MinimalChainable is imported

# 🌟 Define a function to interact with the Ollama llama3.1:latest model
def ollama_prompt(model_name, prompt):
    # 🌐 Define the API endpoint for the local Ollama model
    url = f"http://localhost:11434/api/generate"  # Adjust the endpoint as necessary

    # 📝 Prepare the request payload, including the model name
    payload = {
        "model": model_name,
        "prompt": prompt,
        "temperature": 0.7,  # Adjust as needed
        "max_tokens": 100,  # Adjust as needed
    }

    # 🚀 Send the request to the Ollama model with streaming enabled
    response = requests.post(url, json=payload, stream=True)

    # 🧩 Initialize a variable to hold the generated text
    generated_text = ""

    # 📝 Process the response line by line (each line is a separate JSON object)
    for line in response.iter_lines():
        if line:
            try:
                # Parse the line as JSON
                data = json.loads(line.decode('utf-8'))

                # Append the generated part to the full text
                generated_text += data.get('response', '')

                # If the `done` flag is true, stop reading
                if data.get('done'):
                    break

            except json.JSONDecodeError as e:
                raise Exception(f"JSON decoding error: {str(e)}. Line: {line}")

    return generated_text

# 🚀 Main function to run the story generator using Sequential Prompt Chaining
def simple_story_chain():
    # 🚀 We start with a simple context, like a theme or topic for our story
    context = {"hero": "Tommy the Turtle", "friend": "Sally the Seagull"}

    # 🧩 Here are our prompts that will guide the storyteller
    prompts = [
        "Once upon a time, there was a hero named {{hero}} who lived in a peaceful pond. 🐢",
        "One day, {{hero}} met a new friend named {{friend}}. 🦅",
        "{{hero}} and {{friend}} decided to go on an adventure to find the legendary Golden Shell. 🌟",
        "After a long journey, they finally found the Golden Shell. The end! 🎉"
    ]

    # 🛠️ Run the MinimalChainable to create the story by chaining the prompts
    result, context_filled_prompts = MinimalChainable.run(
        context=context,
        model="llama3.1:latest",  # Specify the model to use
        callable=ollama_prompt,  # Use the Ollama function to generate text
        prompts=prompts,
    )

    # 🎈 Print out the story!
    print("\n📖 Here is the story we created:")
    for part in result:
        print(part)

# 🏁 Run the function to see the magic happen!
if __name__ == "__main__":
    simple_story_chain()

# 📝 Import the necessary modules
from chain import MinimalChainable

# 🌳 Define a fun function to make choices in the adventure
def adventure_chooser(model, prompt):
    # 🎲 Imagine this function as the decision-maker for our adventure
    # We'll just return the prompt as the "choice"
    return prompt

# 🌟 Main function to run the adventure using Sequential Prompt Chaining
def adventure_chain():
    # 🚀 Start with a simple context, like the name of the adventurer
    context = {"adventurer": "Luna"}

    # 🗺️ Here are our prompts that guide the adventure
    prompts = [
        "{{adventurer}} enters a dark forest. 🏞️ She can go left or right. Which way should she go? 🧭",
        "She chose to go {{output[-1]}}. Suddenly, she sees a glowing cave! Should she enter the cave? 🌟",
        "Inside the cave, {{adventurer}} finds a treasure chest. Should she open it? 💰",
        "The chest is filled with gold! Luna is now the richest adventurer in the land! The end. 🎉"
    ]

    # 🛠️ Run the MinimalChainable to create the adventure by chaining the prompts
    result, context_filled_prompts = MinimalChainable.run(
        context=context,
        model=None,  # 🚨 We're not using any fancy model, just a simple function
        callable=adventure_chooser,
        prompts=prompts,
    )

    # 🌟 Print out the adventure!
    print("\n🗺️ Here is the adventure we created:")
    for part in result:
        print(part)

# 🏁 Run the function to start the adventure!
if __name__ == "__main__":
    adventure_chain()

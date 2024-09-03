# 📝 Import the necessary modules
from chain import MinimalChainable

# ➕ Define a simple function that solves a math problem based on a prompt
def math_solver(model, prompt):
    # 🎯 We'll just return the prompt as if it was the answer
    return prompt

# 🌟 Main function to run the math challenge using Sequential Prompt Chaining
def math_challenge_chain():
    # 🚀 We start with a context that includes a number to kick things off
    context = {"number": 5}

    # 🧠 Here are our prompts that will create a chain of math problems
    prompts = [
        "Start with the number {{number}}. What is 5 + {{number}}? ➕",
        "Now take the result and multiply it by 2. What do you get? ✖️",
        "Divide the result by 3. What's the answer? ➗",
        "Finally, subtract 4 from the result. What is the final number? ➖",
    ]

    # 🛠️ Run the MinimalChainable to solve the math problems by chaining the prompts
    result, context_filled_prompts = MinimalChainable.run(
        context=context,
        model=None,  # 🚨 We're not using any fancy model, just a simple function
        callable=math_solver,
        prompts=prompts,
    )

    # 🎉 Print out each step of the math challenge
    print("\n📊 Here's how we solved the math challenge:")
    for i, step in enumerate(result, start=1):
        print(f"Step {i}: {step}")

# 🏁 Run the function to see the math challenge in action!
if __name__ == "__main__":
    math_challenge_chain()

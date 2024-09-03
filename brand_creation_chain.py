# 📝 Import the necessary modules
from chain import MinimalChainable

# 🌟 Define a simple function that will "execute" each part of the brand creation process
def brand_planner(model, prompt):
    # 🎉 We'll just return the prompt as the "result" for this example
    return prompt

# 🚀 Main function to help Tommy, Sally, and Luna create their brand
def brand_creation_chain():
    # 🐢🦅🎒 Our heroes: Tommy the Turtle, Sally the Seagull, and Luna the Adventurer
    context = {
        "hero1": "Tommy the Turtle",
        "hero2": "Sally the Seagull",
        "hero3": "Luna the Adventurer",
        "brand_name": "Adventure Pals"
    }

    # 🌟 Here are the prompts that guide the brand creation process
    prompts = [
        # Step 1: Choose a brand name
        "{{hero1}} and {{hero2}} decided to start a brand. They want {{hero3}} to help them. 🐢🦅🎒",
        "Together, they come up with the brand name '{{brand_name}}'. What should their slogan be? 📝",
        # Step 2: Plan the first product
        "The first product will be a special adventure kit. What should be included in the kit? 🎒",
        # Step 3: Pricing the product (math challenge)
        "They decide to sell the kit for $50. If they make 100 kits, how much will they earn? 💰",
        # Step 4: Advertising the brand (storytelling)
        "To advertise their brand, they create a fun story about their adventures. What’s the opening line of their story? 📖",
        # Step 5: Final decision-making (adventure)
        "They have two options for their first big adventure: exploring a mysterious island or climbing a snowy mountain. Which should they choose? 🌍❄️",
    ]

    # 🛠️ Run the MinimalChainable to create the brand by chaining the prompts
    result, context_filled_prompts = MinimalChainable.run(
        context=context,
        model=None,  # 🚨 We're not using any fancy model, just a simple function
        callable=brand_planner,
        prompts=prompts,
    )

    # 🌟 Print out the steps they took to create their brand
    print("\n🏆 Here’s how Tommy, Sally, and Luna created their brand:")
    for part in result:
        print(part)

# 🏁 Run the function to see the brand creation process in action!
if __name__ == "__main__":
    brand_creation_chain()

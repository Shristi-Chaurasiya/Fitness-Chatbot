import random

# Sample responses
responses = {
    "workout_routine": ["You can try a combination of cardio and strength training for a balanced workout routine.",
                        "A good workout routine includes exercises for both upper and lower body strength."],
    "dietary_advice": ["Make sure to include plenty of fruits and vegetables in your diet for essential nutrients.",
                       "Drink plenty of water throughout the day to stay hydrated and support your workouts."],
    "general_fitness_tips": ["Consistency is key when it comes to fitness. Make sure to stick to your routine.",
                             "Listen to your body and give it proper rest when needed to prevent injuries."],
    "fallback": ["I'm sorry, I didn't understand that. Could you please rephrase your question?",
                 "Apologies, I'm not equipped to answer that. Could you ask something else?"]
}

# Function to generate response
def get_response(query):
    query = query.lower()
    if "workout" in query or "routine" in query:
        return random.choice(responses["workout_routine"])
    elif "diet" in query or "nutrition" in query:
        return random.choice(responses["dietary_advice"])
    elif "fitness" in query or "tips" in query:
        return random.choice(responses["general_fitness_tips"])
    else:
        return random.choice(responses["fallback"])

# Main function to interact with the user
def main():
    print("Welcome to FitnessBot! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_response(user_input)
        print("FitnessBot:", response)

if __name__ == "__main__":
    main()

import random

# Sample responses
responses = {
    "workout_routine": {
        "lose weight": "For losing weight, focus on cardio exercises like running, cycling, or swimming. Incorporate high-intensity interval training (HIIT) to burn more calories in less time.",
        "build muscle": "To build muscle, prioritize strength training exercises like squats, deadlifts, and bench presses. Aim for 3-4 sets of 8-12 repetitions with progressively heavier weights.",
        "improve endurance": "For improving endurance, include activities like long-distance running, cycling, or swimming in your routine. Gradually increase the duration and intensity of your workouts over time.",
    },
    "dietary_advice": {
        "vegetarian": "As a vegetarian, focus on plant-based protein sources like beans, lentils, tofu, and tempeh. Incorporate a variety of fruits, vegetables, whole grains, and healthy fats into your diet.",
        "gluten_free": "If you're gluten-free, choose naturally gluten-free foods like fruits, vegetables, lean proteins, and gluten-free grains such as quinoa, rice, and buckwheat.",
        "allergies": "If you have allergies, avoid foods that trigger allergic reactions. Read food labels carefully and consider consulting a registered dietitian for personalized dietary advice.",
    },
    "general_fitness_tips": [
        "Stay hydrated by drinking plenty of water throughout the day, especially before, during, and after workouts.",
        "Incorporate rest days into your workout routine to allow your muscles to recover and repair.",
    ],
    "fallback": "I'm sorry, I didn't understand that. Could you please rephrase your question?",
}


# Function to generate personalized workout routine based on fitness goals
def generate_workout_routine(fitness_goal):
    return responses["workout_routine"].get(fitness_goal, responses["fallback"])


# Function to generate personalized dietary advice based on dietary restrictions
def generate_dietary_advice(dietary_restriction):
    return responses["dietary_advice"].get(dietary_restriction, responses["fallback"])


# Function to get a general fitness tip
def get_fitness_tip():
    return random.choice(responses["general_fitness_tips"])


# Main function to interact with the user
def main():
    print("Welcome to FitnessBot! Let's get started with your personalized recommendations.")

    # Gather user preferences
    fitness_goal = input("What is your fitness goal (lose weight, build muscle, improve endurance)? ").lower()
    dietary_restriction = input("Do you have any dietary restrictions (vegetarian, gluten-free, allergies)? ").lower()

    # Generate personalized recommendations
    workout_recommendation = generate_workout_routine(fitness_goal)
    dietary_recommendation = generate_dietary_advice(dietary_restriction)

    # Present recommendations to the user
    print("\nHere are your personalized recommendations:")
    print("Workout Routine:", workout_recommendation)
    print("Dietary Advice:", dietary_recommendation)
    print("Fitness Tip:", get_fitness_tip())


if __name__ == "__main__":
    main()

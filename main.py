import streamlit as st
import json

users = {}

def save_data():
    with open('data.json', 'w') as file:
        json.dump(users, file)

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def register_user():
    name = st.text_input("Enter your name:")
    return name

def log_workout():
    exercise = st.text_input("Enter exercise:")
    sets = st.number_input("Enter sets:", value=0, min_value=0)
    reps = st.number_input("Enter reps:", value=0, min_value=0)
    return {'exercise': exercise, 'sets': sets, 'reps': reps}

def log_diet():
    calories = st.number_input("Enter daily calories:", value=0, min_value=0)
    meals = st.text_input("Enter meals (comma-separated):")
    return {'calories': calories, 'meals': meals.split(',')}

def main():
    global users
    users = load_data()

    st.title("Fitness Tracker")
    
    st.write("Grow")

    option = st.sidebar.selectbox("Select an option:", ["Home", "Register User", "Log Workout", "Log Diet"])

    if option == "Register User":
        username = register_user()
        if st.button("Register"):
            if username:
                users[username] = {'workouts': [], 'diet': {'calories': 0, 'meals': []}}
                st.success(f"User {username} registered successfully!")
                save_data()
            else:
                st.warning("Please enter a valid username.")

    elif option == "Log Workout":
        username = st.text_input("Enter username:")
        if username in users:
            workout_data = log_workout()
            if st.button("Log Workout"):
                users[username]['workouts'].append(workout_data)
                st.success("Workout logged successfully!")
                save_data()
        else:
            st.warning("User not found.")

    elif option == "Log Diet":
        username = st.text_input("Enter username:")
        if username in users:
            diet_data = log_diet()
            if st.button("Log Diet"):
                users[username]['diet']['calories'] = diet_data['calories']
                users[username]['diet']['meals'] = diet_data['meals']
                st.success("Diet logged successfully!")
                save_data()
        else:
            st.warning("User not found.")

if __name__ == "__main__":
    main()

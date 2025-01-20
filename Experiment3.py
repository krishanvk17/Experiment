import streamlit as st

def number_guessing_game():
    """

    """
    st.title("Number Guessing Game")

    import random

    answer = random.randint(1, 100)
    max_tries = 7
    tries = 0

    st.write("I'm thinking of a number between 1 and 100.")

    while tries < max_tries:
        guess = st.number_input("Take a guess:", min_value=1, max_value=100)

        if guess < answer:
            st.write("Too low!")
        elif guess > answer:
            st.write("Too high!")
        else:
            st.success(f"Congratulations! You guessed it in {tries + 1} tries.")
            return

        tries += 1

    if tries == max_tries:
        st.error(f"Sorry, you ran out of tries. The answer was {answer}.")

if __name__ == "__main__":
    number_guessing_game()

import streamlit as st
import challenges

st.set_page_config(page_icon="random", layout="wide")

challenges = challenges.challenges

def sidebar():
    with st.sidebar:
        "# Challenges"
        challenge_names = []
        for challenge in challenges:
            challenge_names.append(challenge["name"])
            
        selected_challenge = st.radio("", challenge_names)

        return selected_challenge



def body(challenge_to_display):
    challenge_displayed = False

    for challenge in challenges:
        challenge_name = challenge["name"]

        if challenge_name == challenge_to_display:
            challenge_container = challenge["container"]
            challenge_container()
            challenge_displayed = True

    if not challenge_displayed:
        st.write("Challenge en construction, je serais content d'obtenir des propositions de ta part :)")



def app():
    selected_challenge = sidebar()
    body(selected_challenge)
app()

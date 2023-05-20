import streamlit as st
import datetime
from PIL import Image
import time

# Set the date we're counting down to
countdown_date = datetime.datetime(2024, 1, 25, 12, 0, 0)

# Set up how the webpage looks
st.set_page_config(
    page_title="baby countdown",
    page_icon=":baby:",
    layout="centered",
)
st.title("We're expecting a baby in...")
ph = st.empty()
image = Image.open("baby.jpg")
st.image(image)

# Update the countdown every second
while True:
    # Get the current date and time
    now = datetime.datetime.now()

    # Calculate the remaining time until the countdown date
    remaining_time = countdown_date - now

    # If the countdown is over, break out of the loop
    if remaining_time < datetime.timedelta(seconds=0):
        st.write("The baby is coming!!")
        st.balloons()
        break

    # Calculate the remaining days, hours, minutes, and seconds
    remaining_days = remaining_time.days
    remaining_hours, remainder = divmod(remaining_time.seconds, 3600)
    remaining_minutes, remaining_seconds = divmod(remainder, 60)

    # Display the countdown timer
    countdown = f"{remaining_days} days {remaining_hours} hours {remaining_minutes} minutes {remaining_seconds} seconds"

    ph.write(countdown)

    # Wait for one second
    time.sleep(1)

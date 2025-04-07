import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Set page title and icon
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

# Main title
st.title("🌱 Growth Mindset Challenge")
st.write("""
**Develop your abilities through dedication and hard work.**  
This app helps you build a growth mindset with daily challenges and reflections.
""")

# Sidebar for user info
with st.sidebar:
    st.header("Your Progress")
    user_name = st.text_input("Enter your name")
    start_date = st.date_input("Start date", datetime.today())

    if user_name:
        st.success(f"Welcome, {user_name}! Let's grow together.")

# What is Growth Mindset?
with st.expander("What is a Growth Mindset?"):
    st.write("""
    - **Challenges** are opportunities to grow.  
    - **Effort** leads to mastery.  
    - **Mistakes** are learning experiences.  
    - **Feedback** helps improvement.  
    """)
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*phSC6QHFUvC0QzS6q8H1Jg.png", width=400)

# Daily Challenge
st.subheader("📅 Today's Growth Challenge")

challenges = [
    {"day": 1, "task": "Reframe a negative thought into a learning opportunity."},
    {"day": 2, "task": "Learn something new outside your comfort zone."},
    {"day": 3, "task": "Reflect on a mistake and list 3 lessons."},
    {"day": 4, "task": "Ask for feedback on your work."},
    {"day": 5, "task": "Teach someone a concept you learned."},
]

if 'start_date' in locals():
    days_since_start = (datetime.today().date() - start_date).days
    current_day = (days_since_start % len(challenges)) + 1
    current_challenge = next(c for c in challenges if c["day"] == current_day)

    st.info(f"**Day {current_day}:** {current_challenge['task']}")

    # User reflection input
    with st.form("reflection_form"):
        reflection = st.text_area("How did you approach this challenge? What did you learn?")
        difficulty = st.slider("Difficulty (1-10)", 1, 10)
        submitted = st.form_submit_button("Submit Reflection")

        if submitted and reflection:
            st.success("✅ Reflection saved! Growth happens step by step.")

# Progress Tracking
st.subheader("📊 Your Progress")


if user_name:
    progress_data = {
        "Date": [start_date + timedelta(days=i) for i in range(7)],
        "Challenges Completed": [1, 3, 5, 7, 9, 11, 13],
        "Reflections": [1, 2, 3, 5, 6, 8, 10]
    }
    st.line_chart(pd.DataFrame(progress_data).set_index("Date"))

    st.write("### 🏆 Milestones")
    milestones = [
        {"goal": "First reflection", "completed": True},
        {"goal": "5 challenges", "completed": True if days_since_start >= 5 else False},
        {"goal": "10 reflections", "completed": False},
    ]
    for m in milestones:
        status = "✅" if m["completed"] else "◻️"
        st.write(f"{status} {m['goal']}")

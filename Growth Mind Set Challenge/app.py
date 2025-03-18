import streamlit as st
import random

# Web App Title
st.title("🌱 Growth Mindset Challenge")

# Welcome Message
st.write("Welcome to the Growth Mindset Challenge Web App! 🚀")
st.write(
    "A growth mindset is the belief that abilities and intelligence can be developed through hard work, perseverance, and learning from mistakes. 🌟"
)

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.write("Use this sidebar to explore different sections.")

# Section: What is Growth Mindset?
st.header("What is a Growth Mindset?")
st.write(
    "A **growth mindset** means believing that challenges are opportunities to learn and grow. "
    "Instead of avoiding failures, we embrace them as stepping stones to success! 💪"
)

# Section: Why Adopt a Growth Mindset?
st.header("Why Adopt a Growth Mindset?")
st.write(
    "- **Embrace Challenges:** See obstacles as learning opportunities 🎯\n"
    "- **Learn from Mistakes:** Every mistake helps you improve 📚\n"
    "- **Persist Through Difficulties:** Hard work leads to success 🚀\n"
    "- **Celebrate Effort:** Value the process, not just the result 🎉\n"
    "- **Keep an Open Mind:** Stay curious and keep learning 🧠"
)

# Motivational Quote
st.subheader("🌟 Remember: Growth is a Journey!")
st.write("Every expert was once a beginner. Keep learning, keep growing! 🚀")


# Your Growth Mindset Journal
st.header("🌟 Your Growth Mindset Journal")

# List of daily growth challenges
challenges = [
    "Try something new today, even if it feels a little scary! 🚀",
    "Set a small goal and achieve it today. 🎯",
    "Take a 10-minute walk outside and clear your mind. 🌳",
    "Learn something new online today! 📚",
    "Ask someone for feedback on something you're working on. 🔄",
    "Write down one thing you're grateful for today. 🙏",
    "Take a break and practice deep breathing for 5 minutes. 🌬️",
    "Read a book or article on a topic you're curious about. 📖",
    "Challenge yourself to solve a simple puzzle or brain teaser. 🧩",
    "Call or message a friend you haven't spoken to in a while. 📱",
    "Make a list of 3 things you accomplished today. 📝",
    "Set aside time to reflect on a mistake and what you learned from it. 💡",
    "Help someone with something, even if it's just small. 🤝",
    "Do something creative today, like drawing or writing. 🎨",
    "Take the time to organize your space or workspace. 🧹",
    "Try learning a new word in a foreign language. 🌍",
    "Step out of your comfort zone and do something different today. 🔥",
    "Practice mindfulness or meditation for 10 minutes. 🧘‍♀️",
    "Write down a goal for the week and make a plan to achieve it. 📅",
    "Spend time reflecting on your strengths and how to use them. 💪"
]


# Button to show a daily challenge
if st.button("Get Your Daily Growth Challenge"):
    challenge = random.choice(challenges)
    st.write(f"Your challenge for today is: {challenge}")



# User Progress Tracker using Streamlit session state
if "progress" not in st.session_state:
    st.session_state.progress = []

# User se input lena
user_input = st.text_area("What challenge did you face today? How did you overcome it?")

# Submit button
if st.button("Submit Your Progress"):
    if user_input:
        # Add user input to session state (track progress)
        st.session_state.progress.append(user_input)
        st.success("Great! Reflecting on challenges helps you grow. Keep it up! 🚀")
    else:
        st.warning("Please enter something before submitting.")

# Display saved progress (User's past progress in the same session)
if st.session_state.progress:
    st.write("Your Previous Progress:")
    for entry in st.session_state.progress:
        st.write(f"- {entry}")
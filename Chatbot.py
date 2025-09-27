import streamlit as st
import random

def beginner_resume_tips():
    tips_list = [
        """\n\n1. Keep your resume one page.\n\n2. Use bullet points for readability.\n\n3. Highlight your key projects.\n\n4. Mention technical and soft skills.\n\n5. Tailor your resume for each job.""",
        """\n\n1. Start with a strong objective.\n\n2. Include a professional summary.\n\n3. List education with dates.\n\n4. Add achievements and certifications.\n\n5. Avoid spelling mistakes.""",
        """\n\n1. Use clear section headings.\n\n2. Quantify your project results.\n\n3. Highlight leadership roles.\n\n4. Include volunteering activities.\n\n5. Keep formatting consistent.""",
        """\n\n1. Choose a clean resume template.\n\n2. Focus on relevant experience.\n\n3. Use action verbs for accomplishments.\n\n4. Include keywords from job description.\n\n5. Keep font readable (11-12pt).""",
        """\n\n1. Proofread multiple times.\n\n2. Avoid unnecessary personal details.\n\n3. List skills in a separate section.\n\n4. Showcase problem-solving projects.\n\n5. Include links to portfolios or GitHub."""
    ]
    return random.choice(tips_list)

knowledge_base = {
    "hello": "Hello! I am your Resume Assistant. How can I help you today?",
    "hey": "Hey hello! I am your Resume Assistant. Let me know how can I help you?",
    "hi": "Hi there! I can help you build or improve your resume.",
    "how are you": "I'm doing good..! Thank you",
    "what is a resume": "The resume is a short document that is an effective means of organizing and presenting yourself to an employer in written form.",
    "projects": "Projects act as real-world examples of your capabilities, allowing you to prove your competence, demonstrate soft skills like teamwork and communication.",
    "how to build a resume": beginner_resume_tips(),
    "tips for resume": beginner_resume_tips(),
    "resume tips": beginner_resume_tips(),
    "resume building tips": beginner_resume_tips(),
    "resume making tips": beginner_resume_tips(),
    "what sections in resume": "A good resume should include Objective, Profile, Education, Projects, Skills, Achievements, and Co-curricular Activities.",
    "what is an internship": "An internship is a short-term work experience that allows students or freshers to gain practical knowledge and skills in a professional environment.",
    "why are internships important": "Internships help you gain real-world experience, develop skills, build your resume, and increase your chances of getting a full-time job.",
    "how to apply for an internship": "You can apply for internships by preparing a strong resume, writing a cover letter, and applying through platforms like Internshala, LinkedIn, or directly on company websites.",
    "do i need a resume for internship": "Yes, a resume is usually required for internships. Even if you don’t have work experience, highlight your education, skills, projects, and achievements.",
    "do internships require experience": "No, most internships are designed for students and freshers. Recruiters look at your skills, projects, and willingness to learn.",
    "how to prepare for an interview": "Research the company, review your resume, practice common interview questions, and be ready to talk about your skills and projects.",
    "can internships be unpaid": "Yes, some internships are unpaid, especially in startups or NGOs, but they still provide valuable experience and learning.",
    "can i mention internships in resume": "Yes, internships are very important to add to your resume as they show practical experience and skills.",
    "what is the duration of internships": "Internships usually last from 1 month to 6 months, depending on the company and role.",
    "are virtual internships useful": "Yes, virtual internships help you gain experience and skills even without being physically present at the company.",
    "should i include school projects in resume": "Yes, projects show your practical knowledge and problem-solving ability.",
    "do certifications help in internship applications": "Yes, certifications make your resume stronger and prove your knowledge in a subject.",
    "where to find internships": "You can find internships on LinkedIn, Internshala, Naukri, InternLink, company career pages, and through networking.",
    "can internships turn into jobs": "Yes, if you perform well, many companies offer full-time jobs after internships.",
    "how to make best use of internship": "Be proactive, ask questions, take feedback positively, and build connections with your team.",
    "how to write a powerful resume summary": "Focus on your key achievements, include your professional title, and state how you can bring value to a potential employer.",
    "should i add internship in linkedin": "Yes, adding internships to LinkedIn improves your profile and visibility to recruiters.",
    "difference between internship and job": "An internship is a temporary learning experience, while a job is a long-term employment role.",
    "can first year students do internships": "Yes, first-year students can apply for internships, but focus on learning-based or virtual internships.",
    "is stipend compulsory in internship": "No, not all internships are paid. Many internships offer experience and certificates instead of stipends.",
    "what is industrial training": "Industrial training is a practical program where students learn industry skills, similar to an internship.",
    "thank you": "You're welcome! Happy to help.",
    "bye": "Goodbye! Wishing you success in your applications."
}

def chatbot_response_kb(message):
    message = message.lower().strip()

    # Exact match
    if message in knowledge_base:
        return knowledge_base[message]

    # Check if all words in a key exist in message (loose matching)
    message_words = message.split()
    for key in knowledge_base:
        key_words = key.split()
        if all(word in message_words for word in key_words):
            return knowledge_base[key]

    return "I'm sorry, I don't have an answer for that."

st.markdown("""
<style>
.stApp {
    background-color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #000000;
}
h1, h2, h3, label {
    color: #000000 !important;
}
.stButton>button {
    background: #000000;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background: #333333;
    transform: scale(1.03);
}
.chat-box {
    background-color: #f9f9f9;
    padding: 15px;
    border-left: 6px solid #000000;
    border-radius: 10px;
    margin-bottom: 10px;
    font-size: 16px;
    color: #000000;
}
/* Clear button as icon */
.clear-button {
    background: transparent;
    border: none;
    color: #000000;
    font-size: 24px;
    cursor: pointer;
    margin-left: 10px;
    vertical-align: middle;
    padding: 0;
}
.clear-button:hover {
    color: #ff0000;
}
</style>
""", unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 Chatbot")

# Layout: Input + clear button side-by-side
col1, col2 = st.columns([0.9, 0.1])

with col1:
    user_message = st.chat_input("Type your question and press Enter:")

with col2:
    if st.button("🗑️", help="Clear Chat", key="clear_chat"):
        st.session_state.chat_history = []

if user_message:
    response = chatbot_response_kb(user_message)
    st.session_state.chat_history.append((user_message, response))

# Show chat messages
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"<div class='chat-box'><b>You:</b> {user_msg}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-box' style='border-left:6px solid #000000'><b>Bot:</b> {bot_msg}</div>", unsafe_allow_html=True)

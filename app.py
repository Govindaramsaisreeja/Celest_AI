import streamlit as st
import ollama

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ClesetAI ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="side-title">✨ ClesetAI</div>
        <div class="side-subtitle">Your AI workspace</div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🧠 AI Model")

    model = st.selectbox(
        "Choose your model",
        ["llama3.2", "deepseek-r1"],
        label_visibility="collapsed"
    )

    st.divider()

    if st.button("🧹 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### ⚡ Quick Prompts")

    quick_prompt = None

    if st.button("📚 Explain AI"):
        quick_prompt = "Explain Artificial Intelligence in simple words."

    if st.button("💻 Python Help"):
        quick_prompt = "Teach me an interesting Python concept."

    if st.button("🎯 Interview Question"):
        quick_prompt = (
            "Ask me a beginner-friendly technical interview question."
        )

    if st.button("😂 Tell a Joke"):
        quick_prompt = "Tell me a short funny joke."

    if st.button("💡 Project Idea"):
        quick_prompt = "Give me a unique college project idea."


# =========================================================
# VIBRANT PROFESSIONAL CSS
# =========================================================

st.markdown(
    """
<style>

/* =====================================================
   VIBRANT MAIN BACKGROUND
   ===================================================== */

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {

    background:
        radial-gradient(
            circle at 5% 10%,
            rgba(129, 140, 248, 0.25),
            transparent 28%
        ),

        radial-gradient(
            circle at 95% 15%,
            rgba(244, 114, 182, 0.20),
            transparent 28%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(56, 189, 248, 0.20),
            transparent 35%
        ),

        linear-gradient(
            135deg,
            #F8FAFF,
            #EEF2FF,
            #FDF4FF,
            #EFF6FF
        ) !important;

    color: #202124 !important;

    min-height: 100vh;
}


/* =====================================================
   HEADER
   ===================================================== */

[data-testid="stHeader"] {
    background: transparent !important;
}


/* =====================================================
   MAIN CONTAINER
   ===================================================== */

.block-container {

    max-width: 900px !important;

    padding-top: 45px !important;

    padding-bottom: 40px !important;
}


/* =====================================================
   SIDEBAR
   ===================================================== */

[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #171B3D,
            #252B63,
            #171B3D
        ) !important;

    border-right: none !important;
}


[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


.side-title {

    font-size: 28px;

    font-weight: 800;

    color: #FFFFFF !important;

    margin-bottom: 3px;
}


.side-subtitle {

    color: #B8C1E0 !important;

    font-size: 13px;

    margin-bottom: 10px;
}


[data-testid="stSidebar"] hr {

    border-color:
        rgba(255,255,255,0.15) !important;
}


/* =====================================================
   MAIN TITLE - PLAIN BLACK
   ===================================================== */

.main-title {

    text-align: center;

    font-size: 64px;

    font-weight: 900;

    letter-spacing: -2px;

    color: #202124 !important;

    margin-top: 10px;

    margin-bottom: 5px;

    line-height: 1.1;

    background: none !important;

    -webkit-background-clip: initial !important;

    -webkit-text-fill-color: #202124 !important;

    text-shadow: none !important;
}


/* =====================================================
   SUBTITLE
   ===================================================== */

.subtitle {

    text-align: center;

    color: #64748B !important;

    font-size: 17px;

    margin-bottom: 35px;
}


/* =====================================================
   INPUT LABEL
   ===================================================== */

[data-testid="stTextInput"] label {

    color: #334155 !important;

    font-weight: 700;

    font-size: 14px;
}


/* =====================================================
   TEXT INPUT
   ===================================================== */

[data-testid="stTextInput"] input {

    background:
        rgba(255,255,255,0.90) !important;

    color: #172033 !important;

    border:
        1px solid #CBD5E1 !important;

    border-radius: 15px !important;

    padding: 16px !important;

    font-size: 15px !important;

    box-shadow:
        0 8px 25px
        rgba(79,70,229,0.08);

    transition: all 0.25s ease;
}


[data-testid="stTextInput"] input:focus {

    border:
        1px solid #6366F1 !important;

    box-shadow:
        0 0 0 3px
        rgba(99,102,241,0.12),

        0 8px 25px
        rgba(99,102,241,0.12) !important;
}


[data-testid="stTextInput"] input::placeholder {

    color: #94A3B8 !important;

    opacity: 1 !important;
}


/* =====================================================
   SELECT BOX
   ===================================================== */

[data-testid="stSelectbox"] label {

    color: #FFFFFF !important;

    font-weight: 600 !important;
}


[data-baseweb="select"] > div {

    background:
        rgba(255,255,255,0.10) !important;

    border:
        1px solid
        rgba(255,255,255,0.20) !important;

    border-radius: 10px !important;
}


[data-baseweb="select"] * {

    color: #FFFFFF !important;
}


/* =====================================================
   MAIN BUTTON
   ===================================================== */

.stButton > button {

    width: 100%;

    background:
        linear-gradient(
            90deg,
            #4F46E5,
            #7C3AED,
            #DB2777
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 12px !important;

    padding: 11px 16px !important;

    font-size: 14px !important;

    font-weight: 700 !important;

    box-shadow:
        0 7px 20px
        rgba(99,102,241,0.20);

    transition: all 0.25s ease;
}


.stButton > button p {

    color: #FFFFFF !important;
}


.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 12px 28px
        rgba(124,58,237,0.28);

    filter: brightness(1.06);
}


/* =====================================================
   SIDEBAR BUTTONS
   ===================================================== */

[data-testid="stSidebar"] .stButton > button {

    background:
        rgba(255,255,255,0.08) !important;

    border:
        1px solid
        rgba(255,255,255,0.12) !important;

    box-shadow: none !important;

    text-align: left !important;
}


[data-testid="stSidebar"] .stButton > button:hover {

    background:
        linear-gradient(
            90deg,
            rgba(99,102,241,0.50),
            rgba(219,39,119,0.40)
        ) !important;

    transform: translateX(3px);
}


/* =====================================================
   USER MESSAGE
   ===================================================== */

.user-box {

    background:
        linear-gradient(
            135deg,
            rgba(238,242,255,0.95),
            rgba(245,243,255,0.95)
        );

    color: #172033;

    border:
        1px solid #DDE2F3;

    border-left:
        5px solid #6366F1;

    border-radius: 16px;

    padding: 16px 19px;

    margin-top: 17px;

    box-shadow:
        0 6px 22px
        rgba(79,70,229,0.08);
}


.user-label {

    color: #4F46E5 !important;

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 7px;
}


/* =====================================================
   AI MESSAGE
   ===================================================== */

.ai-box {

    background:
        rgba(255,255,255,0.92);

    color: #172033;

    border:
        1px solid #E2E8F0;

    border-left:
        5px solid #DB2777;

    border-radius: 16px;

    padding: 18px 20px;

    margin-top: 13px;

    box-shadow:
        0 8px 25px
        rgba(15,23,42,0.07);
}


.ai-label {

    color: #DB2777 !important;

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 8px;
}


/* =====================================================
   STATISTICS
   ===================================================== */

.stats {

    text-align: center;

    color: #64748B !important;

    font-size: 13px;

    margin-top: 22px;

    padding: 9px;

    font-weight: 500;
}


/* =====================================================
   DIVIDERS
   ===================================================== */

hr {

    border-color: #E2E8F0 !important;
}


/* =====================================================
   ALERT
   ===================================================== */

[data-testid="stAlert"] {

    border-radius: 12px !important;
}


/* =====================================================
   SPINNER
   ===================================================== */

[data-testid="stSpinner"] {

    color: #6366F1 !important;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">ClesetAI ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your intelligent AI assistant 🤖</div>',
    unsafe_allow_html=True
)


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-box">

                <div class="user-label">
                    👤 You
                </div>

                {message["content"]}

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="ai-box">

                <div class="ai-label">
                    🤖 ClesetAI
                </div>

                {message["content"]}

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# USER INPUT
# =========================================================

question = st.text_input(
    "💬 Ask ClesetAI",
    placeholder="Type your question here..."
)


# =========================================================
# QUICK PROMPT
# =========================================================

if quick_prompt:
    question = quick_prompt


# =========================================================
# ASK AI
# =========================================================

if st.button("✨ Ask ClesetAI"):

    if question.strip() == "":

        st.warning(
            "Please enter a question first! 😊"
        )

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.spinner(
            "ClesetAI is thinking... 🧠"
        ):

            try:

                response = ollama.chat(

                    model=model,

                    messages=[

                        {
                            "role": "system",

                            "content": """
You are ClesetAI, a friendly and intelligent AI assistant.

Explain things clearly and simply.

Be helpful, friendly and encouraging.

Give useful and accurate answers.

Use emojis when appropriate.
"""
                        }

                    ] + st.session_state.messages
                )

                answer = response[
                    "message"
                ]["content"]

            except Exception:

                answer = (
                    "⚠️ I couldn't connect to "
                    "the selected Ollama model. "
                    "Please make sure Ollama is "
                    "running and the selected "
                    "model is installed."
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()


# =========================================================
# STATISTICS
# =========================================================

if st.session_state.messages:

    total_messages = len(
        st.session_state.messages
    )

    total_words = sum(
        len(message["content"].split())
        for message in st.session_state.messages
    )

    st.markdown(
        f"""
        <div class="stats">

            💬 {total_messages} messages

            &nbsp;&nbsp; • &nbsp;&nbsp;

            📝 {total_words} words

        </div>
        """,
        unsafe_allow_html=True
    )
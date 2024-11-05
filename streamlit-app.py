"""
Performance Review Assistant Application
=====================================
A Streamlit-based application that helps generate performance reviews and self-reviews
using various Language Learning Models (LLMs).

This template demonstrates:
1. Building a user interface with Streamlit
2. Integration with multiple LLM providers
3. Audio input handling and transcription
4. Structured data processing with separate review types

Usage:
    streamlit run streamlit-app.py
"""

# Third-party imports
import streamlit as st
from audio_recorder_streamlit import audio_recorder

# Local imports
from llm import GroqLLM
from review import ReviewRequest, generate_review, DEFAULT_QUESTIONS
from self_review import SelfReviewRequest, generate_self_review

# === Application Configuration ===
st.set_page_config(page_title="Performance Review Assistant", layout="wide")

# === Sidebar Configuration ===
with st.sidebar:
    st.title("Review Settings")
    # Configuration options for the review generation
    review_type = st.radio("Select Review Type", ["Performance Review", "Self-Review"])
    # LLM provider selection - expandable for new providers
    llm_type = st.selectbox('Select LLM Type', ['openai', 'google', 'anthropic', 'groq'])
    model_size = st.selectbox('Select Model Size', ['small', 'medium', 'large'])
    # API key management
    user_api_key = st.text_input('Your API Key', type="password")
    groq_api_key = st.text_input('Groq API Key (optional, for audio transcription)', type="password")
    st.info("Note: If provided, audio will be transcribed using Groq, regardless of the selected LLM type.")

# === Performance Review Section ===
if review_type == "Performance Review":
    st.title("Write Performance Review in a Minute")
    
    # Display default questions and guidelines
    st.text("""If no question is passed, the following are considered:
            1. Describe example(s) of the topics selected. What was the context? What actions did they take?
            2. In your opinion, what impact did their actions have?
            3. What recommendations do you have for their growth and development? Your feedback can be about any area of their work.
            """)

    # Input collection section
    your_role = st.text_input('Your Role')
    candidate_role = st.text_input('Candidate Role')
    perf_question = st.text_area('Performance Review Questions (one per line)', height=100)

    # Dual input method: Text or Audio
    col1, col2 = st.columns(2)
    with col1:
        your_review = st.text_area('Briefly describe your experience of working with the candidate...', height=200)
    with col2:
        st.write("Or record your review:")
        # Audio input handling
        audio_bytes = audio_recorder()
        if audio_bytes:
            if groq_api_key:
                groq_llm = GroqLLM(api_key=groq_api_key)
                transcribed_text = groq_llm.transcribe_audio(audio_bytes)
                st.write("Transcribed text:", transcribed_text)
                your_review += transcribed_text
            else:
                st.warning("Audio recorded but not transcribed. Provide a Groq API key for transcription.")

    # Review generation and display
    if st.button('Generate Performance Review'):
        # Input validation
        if not user_api_key:
            st.error("Please enter your API key in the sidebar.")
        elif not your_role or not candidate_role:
            st.error("Please fill in all required fields.")
        elif not your_review and not audio_bytes:
            st.error("Please provide either a your review dump or audio input.")
        else:
            try:
                # Process questions (use default if none provided)
                questions = perf_question.split('\n') if perf_question else DEFAULT_QUESTIONS.split('\n')

                # Create review request object
                review_request = ReviewRequest(
                    your_role=your_role,
                    candidate_role=candidate_role,
                    perf_question="\n".join(questions),
                    your_review=your_review,
                    llm_type=llm_type,
                    user_api_key=user_api_key,
                    model_size=model_size,
                )
                
                # Generate and display review
                review = generate_review(**review_request.model_dump())
                for qa in review:
                    st.markdown(f"**{qa['question']}**")
                    st.markdown(qa['answer'])
                    st.markdown("---")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# === Self-Review Section ===
else:  
    st.title("Generate Your Self-Review")
    
    # Guidelines for self-review
    st.text("""Provide a text dump of your performance information, specific questions you want to address,
            and any additional instructions for the AI to consider while generating your self-review.""")

    # Input collection
    questions = st.text_area('Questions to Answer in Self-Review (one per line)', height=100)
    instructions = st.text_area('Additional Instructions (optional)', height=100)

    # Dual input method: Text or Audio
    col1, col2 = st.columns(2)
    with col1:
        text_dump = st.text_area('Text Dump (information about your performance)', height=200)
    with col2:
        st.write("Or record your self-review:")
        # Audio input handling (similar to performance review section)
        audio_bytes = audio_recorder()
        if audio_bytes:
            if groq_api_key:
                groq_llm = GroqLLM(api_key=groq_api_key)
                transcribed_text = groq_llm.transcribe_audio(audio_bytes)
                st.write("Transcribed text:", transcribed_text)
                text_dump += transcribed_text
            else:
                st.warning("Audio recorded but not transcribed. Provide a Groq API key for transcription.")

    # Self-review generation and display
    if st.button('Generate Self-Review'):
        # Input validation
        if not user_api_key:
            st.error("Please enter your API key in the sidebar.")
        elif not questions:
            st.error("Please provide both the text dump and questions.")
        elif not text_dump and not audio_bytes:
            st.error("Please provide either a text dump or audio input.")
        else:
            try:
                # Process questions
                question_list = [q.strip() for q in questions.split('\n') if q.strip()]

                # Create self-review request object
                self_review_request = SelfReviewRequest(
                    text_dump=text_dump,
                    questions=question_list,
                    instructions=instructions if instructions else None,
                    llm_type=llm_type,
                    user_api_key=user_api_key,
                    model_size=model_size,
                )
                
                # Generate and display self-review
                self_review = generate_self_review(**self_review_request.model_dump())
                for qa in self_review:
                    st.markdown(f"**{qa['question']}**")
                    st.markdown(qa['answer'])
                    st.markdown("---")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
"""
Streamlit LLM Application Template
================================
A simplified template for building LLM-powered Streamlit applications.

Features:
- Pre-configured LLM integration
- Customizable UI components
- Easy to modify for different use cases

Example Use Cases:
- Writing Assistant
- Code Explainer
- Language Translator
- Content Summarizer
"""

import streamlit as st
from typing import Dict, Optional
from llm import OpenAILLM, AnthropicLLM, GroqLLM, GoogleLLM

# === TODO: CUSTOMIZE THESE SETTINGS FOR YOUR APP ===
APP_CONFIG = {
    "title": "Your AI Assistant",  # e.g., "Recipe Generator"
    "description": "Your app description",  # e.g., "Generate recipes based on ingredients"
    "input_label": "Your input prompt",  # e.g., "Enter your ingredients"
    "input_placeholder": "Type your text here...",  # e.g., "e.g., chicken, rice, tomatoes"
    "output_label": "AI Response",  # e.g., "Generated Recipe"
}

# === LLM Provider Setup ===
LLM_PROVIDERS = {
    "OpenAI": OpenAILLM,
    "Anthropic": AnthropicLLM,
    "Groq": GroqLLM,
    "Google": GoogleLLM
}

def initialize_session_state():
    """Initialize session state variables"""
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'llm_instance' not in st.session_state:
        st.session_state.llm_instance = None

def setup_sidebar() -> Dict:
    """Configure the sidebar settings"""
    with st.sidebar:
        st.title("Settings")
        
        # LLM Provider Selection
        provider = st.selectbox('Select AI Provider', list(LLM_PROVIDERS.keys()))
        model_size = st.selectbox('Model Size', ['small', 'medium', 'large'])
        api_key = st.text_input('API Key', type="password")
        
        # TODO: Add your custom settings here
        # Example:
        # temperature = st.slider('Temperature', 0.0, 1.0, 0.7)
        # max_tokens = st.number_input('Max Tokens', 100, 2000, 500)
        
        return {
            'provider': provider,
            'model_size': model_size,
            'api_key': api_key,
            # Add your custom settings here
        }

def get_llm_instance(settings: Dict) -> Optional[object]:
    """Initialize LLM instance based on settings"""
    if not settings['api_key']:
        return None
    
    llm_class = LLM_PROVIDERS[settings['provider']]
    return llm_class(api_key=settings['api_key'])

def main():
    """Main application function"""
    initialize_session_state()
    st.title(APP_CONFIG["title"])
    st.write(APP_CONFIG["description"])
    
    settings = setup_sidebar()
    
    # Main input area
    user_input = st.text_area(
        APP_CONFIG["input_label"],
        placeholder=APP_CONFIG["input_placeholder"],
        height=200
    )
    
    # TODO: Add any additional input fields here
    # Example for a recipe generator:
    # cuisine_type = st.selectbox("Cuisine Type", ["Italian", "Indian", "Mexican", "Chinese"])
    # dietary_restrictions = st.multiselect("Dietary Restrictions", ["Vegetarian", "Vegan", "Gluten-free"])
    
    if st.button('Generate'):
        if not settings['api_key']:
            st.error("Please enter your API key in the sidebar.")
        elif not user_input:
            st.error("Please provide input text.")
        else:
            try:
                llm = get_llm_instance(settings)
                
                # TODO: Customize your prompt template
                prompt = f"""
                {user_input}
                
                Please provide a detailed response.
                """
                
                with st.spinner('Generating response...'):
                    # Get response from LLM
                    response = llm.generate_text(
                        prompt=prompt,
                        model=settings['model_size']
                    )
                    
                    # Display response
                    st.markdown("### " + APP_CONFIG["output_label"])
                    st.write(response)
                    
                    # Save to history
                    st.session_state.history.append({
                        'input': user_input,
                        'response': response
                    })
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    # Display history if needed
    if st.session_state.history and st.checkbox("Show History"):
        st.markdown("### History")
        for idx, item in enumerate(st.session_state.history):
            with st.expander(f"Interaction {idx + 1}"):
                st.write("Input:", item['input'])
                st.write("Response:", item['response'])

# === Example: Recipe Generator Implementation ===
# """
# To create a recipe generator:

# 1. Modify APP_CONFIG:
# APP_CONFIG = {
#     "title": "AI Recipe Generator",
#     "description": "Generate recipes based on your available ingredients",
#     "input_label": "Enter your ingredients",
#     "input_placeholder": "e.g., chicken, rice, tomatoes, onions",
#     "output_label": "Generated Recipe"
# }

# 2. Add custom input fields in main():
#     cuisine_type = st.selectbox("Cuisine Type", ["Italian", "Indian", "Mexican", "Chinese"])
#     serving_size = st.number_input("Serving Size", 1, 10, 4)
#     dietary_restrictions = st.multiselect("Dietary Restrictions", 
#         ["None", "Vegetarian", "Vegan", "Gluten-free"])

# 3. Customize the prompt template:
#     prompt = f\"\"\"
#     Generate a recipe using these ingredients: {user_input}
#     Cuisine Type: {cuisine_type}
#     Serving Size: {serving_size}
#     Dietary Restrictions: {', '.join(dietary_restrictions)}
    
#     Please provide:
#     1. Recipe name
#     2. Ingredients with measurements
#     3. Step-by-step cooking instructions
#     4. Cooking time and difficulty level
#     \"\"\"
# """


if __name__ == "__main__":
    main() 
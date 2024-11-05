# Performance Review Assistant

This repository is part of the AI for Product Leaders course, demonstrating how to build practical LLM applications. The project showcases how to leverage various LLM providers (OpenAI, Anthropic, Google, and Groq) to create an AI-powered performance review assistant.

## Overview

The Performance Review Assistant helps managers and employees write better performance reviews by:
- Generating structured performance reviews based on free-form input
- Supporting both manager reviews and self-reviews
- Offering audio input with transcription capabilities
- Providing flexibility in LLM selection and model sizes

## Features

### 1. Multiple Review Types
- Performance Review (for managers)
- Self-Review (for employees)

### 2. LLM Provider Support
- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude-3 variants)
- Google (Gemini models)
- Groq (Llama and Mixtral models)

### 3. Input Methods
- Text input for detailed reviews
- Audio recording with automatic transcription
- Customizable review questions

## Technical Architecture

The application is built using:
- Streamlit for the frontend
- Python for backend processing
- Multiple LLM providers through their respective APIs
- Helicone for API request monitoring and caching

## Setup Instructions

1. Clone the repository
2. Setup the virtual environment

```bash
#Create the virtual environment
python3.11 -m venv venv
```
Note: you need python 3.11 installed to do this. Refer details below on how to install python 3.11.

```bash
#Activate the virtual environment
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:

```bash
#Create the .env file
touch .env

#Add your API keys to the .env file
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_key
HELIECONE_API_KEY=your_helicone_key
```
5. Run the application:

```bash
streamlit run streamlit-app.py
```

# Python Development Environment Setup Guide

This guide will help you set up your Python development environment for the course. Follow these steps carefully to ensure everything works correctly.

## Prerequisites

Before starting, you need to:
1. Install Python 3.11 on your system
2. Have access to a terminal/command prompt
3. Know how to navigate directories using the terminal


## Customization Guide

This application can serve as a template for building various AI-powered tools. Here are some ideas for customization:

### 1. Diet Tracking Assistant
- Modify the input structure to accept food logs
- Adjust prompts for nutritional analysis
- Add custom templates for meal planning

### 2. Real Estate Discovery
- Adapt the input format for property descriptions
- Modify the LLM prompts for property analysis
- Add structured output for property comparisons

### 3. General Customization Steps:
1. Modify the prompt templates in `review.py` and `self_review.py`
2. Adjust the UI components in `streamlit-app.py`
3. Update the model mappings in `llm.py` for different use cases

## Code Structure

The project is organized into several key components:

1. **Main Application** (`streamlit-app.py`):
   - Handles UI/UX
   - Manages user inputs
   - Coordinates review generation

2. **LLM Integration** (`llm.py`):
   - Implements provider-specific LLM classes
   - Manages API interactions
   - Handles model selection

3. **Review Generation** (`review.py` and `self_review.py`):
   - Contains review generation logic
   - Manages prompt engineering
   - Handles response parsing

## Detailed Installation Instructions

### Step 1: Install Python 3.11

#### For Windows:
1. Visit the [Python Downloads page](https://www.python.org/downloads/)
2. Download Python 3.11.x (where x is the latest minor version)
3. Run the installer
4. ✅ Important: Check "Add Python 3.11 to PATH" during installation

#### For macOS:
Using Homebrew:
```bash
brew install python@3.11
```

#### For Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv
```

### Step 2: Verify Python Installation
Open a terminal and run:
```bash
python3.11 --version
```
You should see output like: `Python 3.11.x`

### Step 3: Set Up Your Project

1. Create and navigate to your project directory:
```bash
mkdir my_project
cd my_project
```

2. Create a virtual environment:
```bash
python3.11 -m venv venv
```

3. Activate the virtual environment:

**For Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**For Windows (PowerShell):**
```bash
.\venv\Scripts\Activate
```

**For macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your command prompt.

### Step 4: Install Required Packages

1. Upgrade pip:
```bash
pip install --upgrade pip
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Troubleshooting

### Common Issues

1. **"Python not found" error:**
   - Verify Python 3.11 is installed correctly
   - Check if Python is added to your system's PATH

2. **"venv not recognized" error:**
   - Ensure you're using Python 3.11 when creating the virtual environment
   - On Linux, install python3.11-venv if not included

3. **Package installation errors:**
   - Make sure your virtual environment is activated (you should see `(venv)` in your prompt)
   - Verify you're using Python 3.11 in your virtual environment

### Verifying Your Setup

Run these commands to verify everything is working:
```bash
python --version  # Should show Python 3.11.x
pip --version    # Should show pip version and Python 3.11
```

## Deactivating the Environment

When you're done working, you can deactivate the virtual environment:
```bash
deactivate
```

## Additional Resources

- [Python Virtual Environments Documentation](https://docs.python.org/3/tutorial/venv.html)
- [Pip Package Manager Documentation](https://pip.pypa.io/en/stable/)

## Need Help?

If you encounter any issues:
1. Double-check that you're using Python 3.11
2. Verify your virtual environment is activated
3. Read the error messages carefully
4. Consult the course instructor or teaching assistants

Remember: Using the correct Python version (3.11) is crucial for compatibility with all course materials and dependencies.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

This project is part of the AI for Product Leaders course, demonstrating practical applications of LLMs in business contexts.

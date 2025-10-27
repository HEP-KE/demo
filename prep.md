
# HEP-KE multi-agent system demo - Preparation Guide

- In the hands-on session, we will go over building a simple agentic system that involves using tools and data. 
- Demo is designed to work on your laptops, using free-tier access to Google's Gemini. 
- Open-weight models are currently in place at NERSC. Details on how they can be used are also included, but may not be discussed during the session.
- Below is the list of preparatory steps. If you encounter issues, please get them addressed on Slack before the session. 

## Prerequisites

### 1. Environment Setup

**Create a conda environment with **Python 3.12**. The example here uses conda, but any working Python distribution is fine.:**
```bash
conda create -n hepke_env python=3.12
conda activate hepke_env
```

**Install Jupyter:**
```bash
conda install jupyter
```

*Or for JupyterLab:*
```bash
conda install jupyterlab
```

### Required Packages
Install packages in the activated environment:
```bash
pip install smolagents[openai] numpy scipy matplotlib classy pandas
```


### 2. Google Gemini API Key Setup
- Go to Google AI Studio: <https://aistudio.google.com/app/api-keys>, and log in using your Google account.
<img width="1512" height="395" alt="Screenshot 2025-10-27 at 10 02 19" src="https://github.com/user-attachments/assets/6b698e38-a579-4378-b260-94084f883a8b" />

- Click on "Create API key" on the top right. Create a trial project to associate the key with a project (These can be edited/deleted)
<img width="1512" height="603" alt="Screenshot 2025-10-27 at 10 03 00" src="https://github.com/user-attachments/assets/73ac39b7-4067-46ae-ac8c-ab3b17a2ff8f" />

- Keep the API key accessible for the session. 
<img width="1512" height="603" alt="Screenshot 2025-10-27 at 10 06 06" src="https://github.com/user-attachments/assets/d44bc58c-6873-48c7-85ae-49f540f5d01a" />
Note: Do not set up billing associated with this key. If you run out of free tokens, they get replenished later in the free tier. 

### 3. Demo Repository Setup

**Clone the demo repository:**
```bash
git clone https://github.com/HEP-KE/demo.git
cd demo
```

**Start Jupyter from the project directory:**
```bash
jupyter notebook
# or
jupyter lab
```

### 4. Optional Reading
- Smolagents launch post by HuggingFace: <https://huggingface.co/blog/smolagents> and a short tutorial: <https://huggingface.co/learn/agents-course/unit1/tutorial>
- Smolagents repository: <https://github.com/huggingface/smolagents>
- Simple first-agent guide: <https://www.nb-data.com/p/getting-started-with-huggingface>

---

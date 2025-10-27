
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


### 2. API Key Setup
- **Create Google Gemini API key** 
- Keep the API key accessible for the session


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
- Review basic smolagents documentation/blog posts online

---

**Note:** Ensure all installations are complete before the demo session begins.

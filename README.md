<div align="center">

🧠 AI Research Agent - Your Automated Science Partner
A powerful, conversational AI agent that automates the entire research workflow—from finding relevant papers on arXiv to reading them and generating a brand-new, publication-ready research paper in PDF format.

</div>

<p align="center">
  <a href="https://huggingface.co/spaces/TanTheta03/research-agent" target="_blank"><img src="https://www.google.com/search?q=https://img.shields.io/badge/Live_Demo-Hugging_Face-yellow%3Fstyle%3Dfor-the-badge%26logo%3Dhugging-face" alt="Live Demo"></a>
  <img src="https://www.google.com/search?q=https://img.shields.io/badge/LangChain-LangGraph-944999%3Fstyle%3Dfor-the-badge%26logo%3DLangChain" alt="LangChain">
  <img src="https://www.google.com/search?q=https://img.shields.io/badge/LLM-Gemini_2.5_Pro-4A89F3%3Fstyle%3Dfor-the-badge%26logo%3Dgoogle-gemini" alt="Google Gemini">
  <img src="https://www.google.com/search?q=https://img.shields.io/badge/Streamlit-1.49-FF4B4B%3Fstyle%3Dfor-the-badge%26logo%3Dstreamlit" alt="Streamlit">
  <img src="https://www.google.com/search?q=https://img.shields.io/badge/Deployment-Docker-2496ED%3Fstyle%3Dfor-the-badge%26logo%3Ddocker" alt="Docker">
</p>

✨ Live Application Access
This agent is deployed and running on Hugging Face Spaces. Interact with it live!

Live Site URL: https://huggingface.co/spaces/TanTheta03/research-agent

🌟 Features
🧠 Conversational Interface: Simply chat with the agent to define your research interests.

🔍 Automated arXiv Search: Scours arXiv for the latest and most relevant papers based on your topic.

📄 On-Demand PDF Analysis: The agent can read and process the full text of any research paper from a URL.

✍️ AI-Powered Paper Generation: Leverages Google's Gemini 2.5 Pro to synthesize information and write a completely new research paper.

⚙️ LaTeX to PDF Rendering: Automatically compiles the generated LaTeX source code into a beautifully formatted PDF, ready for download.

🔬 Multi-Domain Expertise: Trained to assist across fields like physics, computer science, mathematics, economics, and more.

📸 Screenshots
To add your own screenshots, replace the https://placehold.co/... links with direct links to your images.

Chat Interface & Paper Discovery

Paper Generation in Progress





Agent Finds and Reads a Paper

PDF Ready for Download





🛠️ Technology Stack
Category

Technology

Core Logic

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.10-3776AB%3Fstyle%3Dflat-square%26logo%3Dpython%26logoColor%3Dwhite" /> <img src="https://www.google.com/search?q=https://img.shields.io/badge/LangChain-0.3-944999%3Fstyle%3Dflat-square%26logo%3DLangChain%26logoColor%3Dwhite" /> <img src="https://www.google.com/search?q=https://img.shields.io/badge/LangGraph-0.6-944999%3Fstyle%3Dflat-square%26logo%3DLangChain%26logoColor%3Dwhite" />

LLM

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Google-Gemini_2.5_Pro-4A89F3%3Fstyle%3Dflat-square%26logo%3Dgoogle-gemini%26logoColor%3Dwhite" />

Frontend

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Streamlit-1.49-FF4B4B%3Fstyle%3Dflat-square%26logo%3Dstreamlit%26logoColor%3Dwhite" />

Deployment

<img src="https://www.google.com/search?q=https://img.shields.io/badge/Hugging_Face-Spaces-FFD21E%3Fstyle%3Dflat-square%26logo%3Dhugging-face%26logoColor%3Dblack" /> <img src="https://www.google.com/search?q=https://img.shields.io/badge/Docker-2496ED%3Fstyle%3Dflat-square%26logo%3Ddocker%26logoColor%3Dwhite" />

Tooling

<img src="https://www.google.com/search?q=https://img.shields.io/badge/ArXiv-API-B31B1B%3Fstyle%3Dflat-square%26logo%3Darxiv%26logoColor%3Dwhite" /> <img src="https://www.google.com/search?q=https://img.shields.io/badge/Tectonic-LaTeX-000000%3Fstyle%3Dflat-square%26logo%3Dlatex%26logoColor%3Dwhite" />

🚀 Local Development Setup
Prerequisites
Python 3.10+

Git

Tectonic: This project requires a local installation of the Tectonic LaTeX engine for PDF generation. Follow the official guide at tectonic-typesetting.org to install it on your system.

Installation Steps
Clone the repository

git clone [https://huggingface.co/spaces/TanTheta03/research-agent](https://huggingface.co/spaces/TanTheta03/research-agent)
cd research-agent

Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Python dependencies

pip install -r requirements.txt

Set up your environment variables

Create a file named .env in the root of the project.

Add your Google Gemini API key to this file:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Run the Streamlit application

streamlit run frontend.py

The application will be available at http://localhost:8501.

🤝 Contributing
We welcome contributions! Please fork the repository, create a feature branch, and open a pull request.

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
TanTheta03

Hugging Face: @TanTheta03

GitHub: <!--- Add your GitHub profile link here if you have one -->

<div align="center">
  ⭐ Show Your Support! If you find this project cool, please consider giving the repository a star! ⭐
</div>
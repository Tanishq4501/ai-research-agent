# 🧠 AI Research Agent
### *Your Automated Science Partner*

<div align="center">

**A powerful, conversational AI agent that automates the entire research workflow—from finding relevant papers on arXiv to reading them and generating a brand-new, publication-ready research paper in PDF format.**

</div>

---

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face-FFD21E?style=for-the-badge&logo=hugging-face&logoColor=black)](https://huggingface.co/spaces/TanTheta03/research-agent)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-LangGraph-944999?style=for-the-badge&logo=LangChain&logoColor=white)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/🤖_LLM-Gemini_2.5_Pro-4A89F3?style=for-the-badge&logo=google-gemini&logoColor=white)](https://gemini.google.com)

[![Streamlit](https://img.shields.io/badge/⚡_Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/🐳_Deployment-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

</div>

---

## ✨ **Experience It Live**

> 🎯 **Ready to revolutionize your research?** The agent is deployed and running on Hugging Face Spaces!

<div align="center">

### **[👉 Try It Now - Live Demo](https://huggingface.co/spaces/TanTheta03/research-agent)**

</div>

---

## 🌟 **What Makes This Special**

<table>
<tr>
<td width="50%">

### 🎯 **Smart & Conversational**
Simply chat with the agent to define your research interests. No complex forms or configuration needed.

### 🔍 **Intelligent Discovery** 
Automatically scours arXiv for the latest and most relevant papers based on your topic using advanced search algorithms.

</td>
<td width="50%">

### 📄 **Deep Analysis**
Reads and processes the full text of any research paper from a URL, extracting key insights and methodologies.

### ✍️ **AI-Powered Synthesis**
Leverages Google's Gemini 2.5 Pro to synthesize information and write completely new, original research papers.

</td>
</tr>
<tr>
<td width="50%">

### ⚙️ **Professional Output**
Automatically compiles generated LaTeX source code into beautifully formatted PDFs, ready for academic submission.

</td>
<td width="50%">

### 🔬 **Multi-Domain Expertise**
Trained to assist across diverse fields including physics, computer science, mathematics, economics, and more.

</td>
</tr>
</table>

---

## 📸 **See It In Action**

<div align="center">

| 💬 **Chat Interface & Paper Discovery** | 🔄 **Paper Generation in Progress** |
|:---:|:---:|
| ![Chat Interface](https://placehold.co/400x250/1f2937/ffffff?text=Interactive+Chat+Interface) | ![Generation Progress](https://placehold.co/400x250/059669/ffffff?text=AI+Writing+Paper) |

| 📖 **Agent Finds and Reads Papers** | 📄 **PDF Ready for Download** |
|:---:|:---:|
| ![Paper Analysis](https://placehold.co/400x250/7c3aed/ffffff?text=Reading+%26+Analysis) | ![PDF Output](https://placehold.co/400x250/dc2626/ffffff?text=Beautiful+PDF+Output) |

</div>

---

## 🛠️ **Technology Stack**

<div align="center">

| **Category** | **Technologies** |
|:---:|:---|
| **🧠 Core Logic** | ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-0.3-944999?style=flat-square&logo=LangChain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-0.6-944999?style=flat-square&logo=LangChain&logoColor=white) |
| **🤖 AI Engine** | ![Google Gemini](https://img.shields.io/badge/Gemini-2.5_Pro-4A89F3?style=flat-square&logo=google-gemini&logoColor=white) |
| **🎨 Frontend** | ![Streamlit](https://img.shields.io/badge/Streamlit-1.49-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) |
| **☁️ Deployment** | ![Hugging Face](https://img.shields.io/badge/Hugging_Face-Spaces-FFD21E?style=flat-square&logo=hugging-face&logoColor=black) ![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white) |
| **🔧 Tooling** | ![ArXiv](https://img.shields.io/badge/ArXiv-API-B31B1B?style=flat-square&logo=arxiv&logoColor=white) ![Tectonic](https://img.shields.io/badge/Tectonic-LaTeX-000000?style=flat-square&logo=latex&logoColor=white) |

</div>

---

## 🚀 **Quick Start Guide**

### **Prerequisites**

Make sure you have these installed on your system:

- 🐍 **Python 3.10+**
- 🔧 **Git**
- 📝 **[Tectonic LaTeX Engine](https://tectonic-typesetting.org)** - Required for PDF generation

### **Installation**

```bash
# 1️⃣ Clone the repository
git clone https://huggingface.co/spaces/TanTheta03/research-agent
cd research-agent

# 2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure environment
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# 5️⃣ Launch the application
streamlit run frontend.py
```

<div align="center">

🎉 **That's it!** Your research agent will be running at `http://localhost:8501`

</div>

---

## 💡 **How It Works**

```mermaid
graph TD
    A[🗣️ User Query] --> B[🔍 arXiv Search]
    B --> C[📋 Paper Selection]
    C --> D[📖 Content Analysis]
    D --> E[🧠 AI Synthesis]
    E --> F[📝 LaTeX Generation]
    F --> G[📄 PDF Compilation]
    G --> H[📥 Download Ready]

    style A fill:#3b82f6,stroke:#1d4ed8,color:#fff
    style H fill:#10b981,stroke:#047857,color:#fff
    style E fill:#8b5cf6,stroke:#7c3aed,color:#fff
```

---

## 🤝 **Contributing**

We love contributions! Here's how you can help make this project even better:

1. **🍴 Fork** the repository
2. **🌱 Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **💫 Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **🚀 Push** to the branch (`git push origin feature/amazing-feature`)
5. **📩 Open** a Pull Request

---

## 📋 **Roadmap**

- [ ] 🔗 Integration with more academic databases (IEEE, PubMed, etc.)
- [ ] 📊 Advanced citation analysis and visualization
- [ ] 🎯 Collaborative research features
- [ ] 🌍 Multi-language paper support
- [ ] 📱 Mobile app development
- [ ] 🔄 Real-time collaboration features

---

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 **About the Creator**

<div align="center">

**Built with ❤️ by [TanTheta03](https://huggingface.co/TanTheta03)**

[![Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-@TanTheta03-FFD21E?style=for-the-badge&logo=hugging-face&logoColor=black)](https://huggingface.co/TanTheta03)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white)](#)

</div>

---

<div align="center">

### ⭐ **Show Your Support!** 

If you find this project helpful, please consider giving it a star! It means the world to open-source developers.

**[⭐ Star this Repository](https://github.com/your-username/research-agent)**

---

*"Transforming the way researchers discover, analyze, and create scientific knowledge."*

</div>

---

<details>
<summary>📚 <strong>Advanced Usage & Tips</strong></summary>

### **🎯 Getting Better Results**

- **Be Specific**: Instead of "machine learning," try "transformer attention mechanisms in NLP"
- **Use Keywords**: Include technical terms relevant to your field
- **Iterative Refinement**: Chat with the agent to refine your research scope

### **🔧 Troubleshooting**

- **PDF Generation Issues**: Ensure Tectonic is properly installed and accessible in your PATH
- **API Limits**: The Gemini API has rate limits; wait a moment if you hit them
- **Memory Issues**: For large papers, the agent processes content in chunks

### **🌟 Pro Tips**

- The agent works best with focused, specific research questions
- You can ask it to focus on particular aspects of papers (methodology, results, etc.)
- Generated papers include proper citations and references

</details>

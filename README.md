# 🤖 Q&A Chatbot with Ollama and LangChain

A simple yet powerful **Question & Answer Chatbot** built using **Streamlit**, **LangChain**, and **Ollama**.  
This app allows users to interact with local large language models (LLMs) like `gemma:2b` directly from a web interface.

---

## 🚀 Features

- 🧠 Built using **LangChain** for modular AI pipelines  
- 💬 Uses **Ollama** for running local LLMs  
- 🌐 Interactive frontend with **Streamlit**  
- 🔑 Integrated with **LangSmith** for tracing and run tracking  
- ⚙️ Adjustable parameters (temperature, max tokens, model choice)

---

## 🏗️ Project Structure

Q&A_ChatBot/
│
├── app_ollama.py # Main Streamlit application
├── .env.example # Example environment file (no secrets)
├── .gitignore # Git ignore rules
├── requirements.txt # Dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 💻 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/QnA_ChatBot.git
cd QnA_ChatBot
2️⃣ Create a Virtual Environment
If you want to name it chatbot:

bash
Copy code
python -m venv chatbot
Activate it:

Windows:

bash
Copy code
chatbot\Scripts\activate
Mac/Linux:

bash
Copy code
source chatbot/bin/activate
3️⃣ Install Dependencies
Install all required packages from requirements.txt:

bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the project root and add the following:

bash
Copy code
LANGCHAIN_API_KEY="your_langchain_api_key_here"
LANGCHAIN_PROJECT="Q&A_Chatbot"
LANGCHAIN_TRACING_V2=true
⚠️ Do not commit your .env file.
It is already ignored in .gitignore. You can use .env.example for reference.

5️⃣ Run the App
Start the Streamlit app:

bash
Copy code
streamlit run app_ollama.py
Then open the URL shown in the terminal (usually http://localhost:8501).

🧩 How It Works
Loads environment variables from .env using python-dotenv

Configures LangChain to use your LangSmith project for tracing

Lets users enter a question via Streamlit interface

Passes the query through a LangChain prompt → Ollama LLM → Output Parser

Displays the LLM-generated answer in the browser

⚙️ Environment Variables Reference
Variable	Description
LANGCHAIN_API_KEY	Your LangSmith API key for tracking
LANGCHAIN_PROJECT	Project name visible in your LangSmith dashboard
LANGCHAIN_TRACING_V2	Enables LangSmith tracing (must be true)

📊 LangSmith Integration
If everything is configured correctly, you’ll see your chatbot runs appear under your LangSmith project dashboard:

👉 https://smith.langchain.com

🧠 Example Models (via Ollama)
You can modify or extend the dropdown list in the sidebar:

python
Copy code
llm_name = st.sidebar.selectbox("Select a model", ["gemma:2b", "llama3", "mistral", "phi3"])
To use these models, make sure they’re pulled locally via Ollama:

bash
Copy code
ollama pull gemma:2b
🧰 Requirements
All required Python packages are listed in requirements.txt:

nginx
Copy code
streamlit
python-dotenv
langchain
langchain-community
langsmith
ollama
langchain-core
Install with:

bash
Copy code
pip install -r requirements.txt
🧾 License
This project is open-source and available under the MIT License.

🧑‍💻 Author
Laxman Sannu Gouda
📧 [Add your email if you want]
💬 “Built with 💡 LangChain, ⚙️ Streamlit, and 💭 Ollama”

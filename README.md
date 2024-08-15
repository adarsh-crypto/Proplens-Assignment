# **Real Estate QnA System**

## **Overview**

The Real Estate QnA System is an intelligent and scalable solution designed to answer queries related to real estate projects. The system utilizes advanced AI models, including Llama 3.1 for natural language processing, `nomic-embed-text` for embedding generation, and Qdrant as a vector database for efficient retrieval. It implements a Retrieval-Augmented Generation (RAG) framework to provide accurate and context-aware responses.

## **Features**

- **Contextual QnA**: Leverages Llama 3.1 to generate accurate, context-aware answers.
- **Efficient Retrieval**: Uses `nomic-embed-text` for embedding generation and Qdrant for fast vector searches.
- **Hallucination Reduction**: Integrates `ms-marco-MiniLM-L-2-v2` to reduce hallucinations and ensure response accuracy.
- **Local Processing**: All data processing is performed locally, ensuring data privacy and security.
- **Scalability**: Designed to scale with more data and handle multiple queries efficiently.

## **Getting Started**

### **Prerequisites**

Before you begin, ensure you have the following installed on your system:

- **Python 3.x**
- **CUDA** (if using GPU acceleration)
- **NVIDIA GPU** (RTX 3050 or better recommended)
- **pip** (Python package installer)
- **Qdrant** (Vector database engine)

### **Installation**

1. Navigate to the Project Directory
After unzipping the project folder, open your terminal or command prompt and navigate to the DocGPT subfolder:

bash
Copy code
cd path_to_your_project_folder/DocGPT
Replace path_to_your_project_folder with the actual path where you unzipped the project.

2. Install Ollama
Ollama is required for serving your models. Install it using the following command:

bash
Copy code
curl -fsSL https://ollama.com/install.sh | sh
3. Start Ollama Server
Once installed, start the Ollama server by running:

bash
Copy code
ollama serve
It's recommended to keep this terminal window open as it runs the server. You can open a new terminal window for the subsequent steps.

4. Pull Base Models
Retrieve the necessary base models using Ollama:

bash
Copy code
ollama pull llama3.1
ollama pull nomic-embed-text
Ensure that these commands complete successfully before proceeding.

5. Install Poetry
Poetry is a tool for dependency management and packaging in Python. Install it using pip:

bash
Copy code
pip install poetry
If you don't have pip installed, you'll need to install it first. Visit pip's official documentation for guidance.

6. Install DocGPT Requirements
With Poetry installed, install the required dependencies for DocGPT:

bash
Copy code
poetry install --extras "ui llms-ollama embeddings-ollama vector-stores-qdrant rerank-sentence-transformers"
This command installs the base requirements along with the specified extras.

7. Navigate to the Main Project Directory
After setting up DocGPT, return to the main directory of your project (one level up from DocGPT):

bash
Copy code
cd ..
8. Install Project Requirements
Install the necessary Python packages for the FastAPI backend and Gradio frontend:

bash
Copy code
pip install -r requirements.txt
Ensure that the requirements.txt file is located in the main project directory. The content should include:

makefile
Copy code
fastapi==0.103.2
pydantic==1.10.12
aiohttp==3.8.5
uvicorn==0.23.2
gradio==3.39.0
requests==2.31.0
9. Run the FastAPI Backend
Start the FastAPI server by running:

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 9001
This command assumes that your FastAPI application instance is named app in a file called main.py. Adjust the command if your filenames or app instances are named differently.

10. Run the Gradio Frontend
In a new terminal window, launch the Gradio interface:

bash
Copy code
python gradio_app.py
Replace gradio_app.py with the actual filename containing your Gradio code.

11. Verify the Setup
FastAPI Backend: Once the server is running, it should be accessible at http://0.0.0.0:9001.

Gradio Frontend: After launching, Gradio will provide a local URL (typically http://127.0.0.1:9002) where you can access the UI.

Ensure both the backend and frontend are running without errors. You can test the application by navigating to the Gradio URL in your web browser and interacting with the interface.

Troubleshooting Tips
Port Conflicts: If the specified ports (9001 for FastAPI and 9002 for Gradio) are already in use, either stop the processes using them or modify the ports in the launch commands.

Dependency Issues: If you encounter errors related to missing packages, ensure that all dependencies are correctly listed in the requirements.txt file and that the installations completed successfully.

Server Errors: Check the terminal outputs for any error messages when running the servers. They often provide insights into what might be going wrong.


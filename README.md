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


This Streamlit application allows users to upload a PDF document and ask questions about its content. It uses Langchain for document loading, text splitting, embeddings, and question answering.  The code runs locally using Ollama as the LLM.

## Features

*   **PDF Upload:** Allows users to upload PDF files directly through the Streamlit UI.
*   **Text Chunking:** Splits PDF content into smaller chunks for efficient processing.
*   **Embeddings:** Uses OllamaEmbeddings to generate embeddings for the text chunks.
*   **Question Answering:** Leverages an Ollama LLM to answer questions based on the uploaded PDF content.
*   **Local LLM:** The LLM runs locally using Ollama, providing a private and customizable experience.

## Prerequisites

Before running the application, make sure you have the following installed:

*   **Python 3.7+**
*   **Ollama:**  Installed and running with the specified model (default: `llama3.2`). [https://ollama.com/download](https://ollama.com/download)
*   **Pip:**  Python package installer

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [your_repo_url]
    cd [your_repo_directory]
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download Ollama Model:**
    - Pull the specified Ollama model:
    ```bash
    ollama pull llama3.2
    ```
    -  If you change the `MODEL_NAME` or `EMBEDDINGS_MODEL` variables in `app.py`, make sure to download those models as well.

## Usage

1.  **Run the Streamlit App:**
    ```bash
    streamlit run app.py
    ```

2.  **Open in Browser:**
    - The Streamlit application will open in your web browser.

3.  **Upload PDF:**
    - Click the "Browse files" button to upload a PDF document.

4.  **Ask Questions:**
    - Type your question in the text box and press Enter. The application will provide an answer based on the content of the PDF.

## Configuration

The following variables in the `app.py` file can be configured:

*   `PDFS_DIRECTORY`: The directory where uploaded PDFs are stored (default: `pdfs/`).
*   `MODEL_NAME`: The name of the Ollama model used for question answering (default: `llama3.2`).
*   `EMBEDDINGS_MODEL`: The name of the Ollama model used for creating embeddings (default: `llama3.2`).
*   `CHUNK_SIZE`: The text chunk size for splitting documents (default: `1000`).
*   `CHUNK_OVERLAP`: The text chunk overlap (default: `100`).

## Error Handling

The application includes error handling to catch common issues such as:

*   Failed PDF loading
*   Text splitting errors
*   Vector store indexing errors
*   Question answering errors

Error messages are displayed in the Streamlit UI to help users troubleshoot problems.

## Notes

*   Ensure that the specified Ollama model is downloaded and running before running the application.
*   The application uses `InMemoryVectorStore`, which means the vector store is not persistent. Uploaded PDFs and their embeddings will be lost when the application is restarted. For persistent storage, consider using a database-backed vector store like ChromaDB or Pinecone.
*   Consider using a smaller model if you are encountering memory issues or slow response times.


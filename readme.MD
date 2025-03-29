

# AlgoRoot

AlgoRoot is a Python-based API service that dynamically retrieves and executes automation
functions using LLM + RAG (Retrieval-Augmented Generation). The system should process
user prompts, map them to predefined automation functions, and generate executable Python
code for function. 

## Features
-Application Control: Open Chrome
System Monitoring: Retrieve CPU/RAM usage etc


## Getting Started
### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.6)
# Requirements

## Python Dependencies
To run this project, ensure you have the following Python packages installed:

### Required Packages
Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

#### Package List
- `chromadb` - Vector database for efficient retrieval
- `sentence-transformers` - Pre-trained transformer models for sentence embeddings
- `fastapi` - Web framework for building APIs
- `pydantic` - Data validation and settings management using Python type hints
- `psutil` - System and process utilities for monitoring
- `subprocess` - Subprocess management for executing system commands
- `webbrowser` - Library to open URLs in web browsers
- `os` - Built-in module for interacting with the operating system
- `json` - JSON parsing and serialization

## System Requirements
Ensure your system meets the following requirements:
- Python 3.8 or higher
- pip package manager

## Installation
1. Clone the repository:
```bash
git clone https://github.com/adarsh2023calc/AlgoRoot.git
cd AlgoRoot
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the FastAPI application:
```bash
uvicorn main:app --reload
```

## Additional Notes
- Ensure `chroma_retrieval.py` is present in the working directory, as it is required for retrieval functions.
- Some system-level dependencies may require additional installations based on the OS.

For any issues, refer to the documentation or raise an issue in the repository.



### Clone the Repository
```bash
git clone https://github.com/adarsh2023calc/AlgoRoot.git
cd AlgoRoot
```




## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any queries or contributions, feel free to reach out:
- **Maintainer**: Adarsh Sudheer
- **Email**: [adarshs2023@gmail.com]
- **GitHub**: [@adarsh2023calc](https://github.com/adarsh2023calc)

Happy Coding! 🚀


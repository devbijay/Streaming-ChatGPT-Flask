# Simple Flask using OpenAI's API Streaming Response

This is a simple Flask application that utilizes OpenAI's API to provide streaming chat responses based on user input.

![Demo](https://i.imgur.com/8ngPEfv.gif)

## Getting Started

### Prerequisites

- Python 3.6+
- OpenAI API Key
- Flask
- dotenv

### Installation

1. Clone the repository:

```bash
git clone https://github.com/devbijay/Streaming-ChatGPT-Flask.git
cd Streaming-ChatGPT-Flask
```

2. Install the required packages using pip:

```shell 
pip install -r requirements.txt 
```

3. Create a .env file in the root directory and add your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

### Usage

1. Run the Flask app:

```python
python
app.py
```

2. Open your browser and navigate to `http://localhost:5000/`.
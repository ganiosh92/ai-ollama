## Step-1:
Download Ollama here: https://ollama.com/download

## Step-2:
Pull the model you want to work with e.g. mistral or gemma
```bash
pull ollama mistral
````

## Step-3:
Install Ollama python library to work with Ollama using python
```bash
pip install ollama
```

## Step-4:
run the following ```main.py``` file using python
```bash
python main.py
```
What ```main.py``` contains is mostly boilerplate code (shown under) to run a hardcoded user query
```python
from ollama import chat

response = chat(
                model='llama2', 
                messages=[{'role': 'user',
                            'content': 'explain in a sentance what is quantum mechanics?'
                        },]
                )

print(response.message.content)
```

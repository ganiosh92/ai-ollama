from ollama import chat

response = chat(
                model='llama2', 
                messages=[{'role': 'user',
                            'content': 'explain in a sentance what is quantum mechanics?'
                        },]
                )

print(response.message.content)




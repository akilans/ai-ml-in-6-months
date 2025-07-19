# Ollama

-  Managing & Running Large language model locally

### Notes

- Parameters
    -  No of trainable parameters
    -  more parameters often mean more learning capacity, but also require more memory and computation.
- Context Length (tokens)
    - maximum number of tokens (words, subwords, or characters) the model can process in a single input sequence
- Embedding Length
    - token embeddings, i.e., each input token is represented as a number of dimensional vector
    - Higher embedding dimensions allow for richer representation of meaning, but again increase computational load.

### Setup and Running

```bash
ollama --help
# list all the models in local
ollama list 

#https://ollama.com/search
ollama pull llama3.2

#Show information for a model
ollama show llama3.2

# run llm in cli mode
ollama run llama3.2

#ask questions and llm will answer. type /bye to exit

# stop llm
ollama stop llama3.2

# remove model
ollama rm llama3.2

# list all the running models
ollama ps

# Expose ollama API
ollama serve #http://localhost:11434/

# Create a new model from existing
# Create a Modelfile
ollama create my-llama3.2 -f Modelfile

ollama run my-llama3.2

# api call
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}'

python3 -m venv ollama-env
source ./ollama-env/bin/activate
pip install -r requirements.txt

# create a chat with memory
python app.py
```
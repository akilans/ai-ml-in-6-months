# Important LLM terms

- Token / Tokenization - Breaking text into small units (words, subwords, or characters).
    - Example: "AI is smart" → ["AI", " is", " smart"]
    - LLMs don’t read whole sentences; they read tokens.

- Embedding - Converting tokens into vectors (numbers) that capture meaning.
    - Think: "Math version" of a word that helps the model process language.
    - Similar words have similar embeddings.

- Parameters - The internal "knobs" the model learns during training.
    - Example: LLaMA 3 8B has 8 billion parameters.
    - More parameters = potentially more powerful (but also heavier to run).

- Inference - Using a trained model to generate text (like answering your questions).
    - Opposite of training (which teaches the model).

- Fine-Tuning - Training a model further on a specific dataset to specialize it (e.g., for medical text or legal language).
    - Taking LLaMA 3 and fine-tuning it to answer only programming questions.

- Quantization - Compressing a model by using fewer bits per number (e.g., 4-bit instead of 16-bit).
    - Makes models smaller and faster, but can slightly reduce accuracy.
    - You can run a 7B model on a laptop if it's 4-bit quantized.

- Self-Attention - The model checks how important each word is to every other word in a sentence.
    - Enables LLMs to understand context and meaning.

- Context Window / Context Length - The maximum number of tokens the model can remember at once.
    - LLaMA 3 has a context window of 8,192 tokens.
    - Longer windows mean better memory over longer conversations.

- Prompt - The input you give the model (question, instruction, etc.).
    - Good prompting leads to better answers.

- Model Size - Usually refers to the number of parameters (e.g., 7B, 13B, 70B).
    - Bigger models may be smarter but need more memory and compute.

- Checkpoint / Weights - A saved state of the model (the trained parameters).
    - Used to resume training or run the model.

- LoRA (Low-Rank Adaptation) - A lightweight way to fine-tune a model using much less memory.
    - Popular for customizing models without retraining the whole thing.


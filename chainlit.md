## Task 2: knowledge based embedding
Instead of fine-tuning a large language model (LLM) directly on the provided book data, I opted for a Retrieval-Augmented Generation (RAG) approach.

Reasons for Choosing RAG:

- Accuracy concerns: Fine-tuning LLMs can sometimes lead to decreased accuracy, and my initial experiments confirmed this trend.
- Hallucination tendency: LLMs can be prone to generating unrealistic or irrelevant text, which was particularly evident in my fine-tuning trials.

Benefits of RAG:

- Improved factual accuracy: RAG retrieves relevant passages from the book data, providing the LLM with a factual foundation for its responses.
- Reduced hallucination: Focusing on retrieved information helps keep the LLM's generated text grounded in reality.
- More efficient use of resources: RAG leverages pre-trained models efficiently, potentially avoiding the need for extensive fine-tuning and reducing computational costs.

I believe this RAG approach will deliver more accurate and reliable responses while alleviating concerns about unrealistic output.

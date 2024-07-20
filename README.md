# Document-specific Retrieval Augmented Generation
Developed a question-answering system using SBERT, FAISS, Gemini-pro, and LangChain to transform Wikipedia articles into searchable knowledge.

# What we did?

* Converted Wikipedia articles into dense vector representations using SBERT - a pre-trained language model
to facilitate similarity search and implemented FAISS for efficient storage and retrieval of these embeddings.

* Employed Gemini-pro to generate answers by processing a subset of the most pertinent articles.

* Implemented RAG pipeline using LangChain, incorporating document loading, embedding, vector store
creation and retrieval to enhance question answering capabilities.

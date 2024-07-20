# Document-specific Retrieval Augmented Generation
Developed a question-answering system using SBERT, FAISS, Gemini-pro, and LangChain to transform Wikipedia articles into searchable knowledge.

# What we did?

* Converted Wikipedia articles into dense vector representations using SBERT - a pre-trained language model
to facilitate similarity search and implemented FAISS for efficient storage and retrieval of these embeddings.

* Employed Gemini-pro to generate answers by processing a subset of the most pertinent articles.

* Implemented RAG pipeline using LangChain, incorporating document loading, embedding, vector store
creation and retrieval to enhance question answering capabilities.

You could find more information about our work in this: ```./RAG.pdf```

# How to use?

You could just simply follow those two rules:

1. Create your Gemini-pro API key in this [link][1]

[1] https://ai.google.dev/aistudio?hl=vi "link"

2. Run app.py

# UI

We adopted a ChatGPT-inspired design for our chatbot's interface.

![](./chatbot.png)

# Citation

We would like to acknowledge the significant contributions of these works to our project. These were the sources we consulted for our work.

[1] \href{https://arxiv.org/abs/2005.11401}{Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks}

[2] \href{https://python.langchain.com/v0.2/docs/introduction/}{Tìm hiểu và áp dụng LangChain}

[3] \href{https://arxiv.org/abs/1908.10084}{Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks}

[4] \href{https://sbert.net/}{Cài đặt mô hình embedding all-MiniLM-L6-v2}

[5] \href{https://github.com/facebookresearch/faiss/wiki}{Thư viện FAISS}

[6] \href{https://ai.google.dev/}{Sử dụng mô hình Gemini-pro}

[7] \href{https://huggingface.co/datasets/legacy-datasets/wikipedia}{Bộ dữ liệu Wikipedia}

[8] \href{https://getbootstrap.com/docs/5.0/getting-started/introduction/}{BootStrap 5.0 Documentation}

[9] \href{https://flask.palletsprojects.com/en/3.0.x/}{Flask documentation}

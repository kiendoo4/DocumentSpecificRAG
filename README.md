# Document-specific Retrieval Augmented Generation
Developed a question-answering system using SBERT, FAISS, Gemini-pro, and LangChain to transform Wikipedia articles into searchable knowledge.

# What we did?

* Converted Wikipedia articles into dense vector representations using SBERT - a pre-trained language model
to facilitate similarity search and implemented FAISS for efficient storage and retrieval of these embeddings.

* Employed Gemini-pro to generate answers by processing a subset of the most pertinent articles.

* Implemented RAG pipeline using LangChain, incorporating document loading, embedding, vector store
creation and retrieval to enhance question answering capabilities.

* Developed a chatbot web application with Flask and Bootstrap 5.0 (by HatakaCder)

You could find more information about our work in this: ```./RAG.pdf```

# How to use?

You could just simply follow those two rules:

1. Create your Gemini-pro API key and put the key in line 16 of app.py

2. Make your own index.faiss and index.pkl (or you could use from us)
  
3. Run app.py

Wikipedia dataset that we used was "20220301.simple" from https://huggingface.co/datasets/legacy-datasets/wikipedia

index.faiss from that dataset: https://drive.google.com/file/d/1N0_OhUccPOftj2wqFr_VvDbGPtmdxT7A/view?usp=sharing

index.pkl: https://drive.google.com/file/d/1neqAAa4OeuairLoAGgxAo0UZS5LFJ25i/view?usp=sharing

# UI

We adopted a ChatGPT-inspired design for our chatbot's interface.

![](./chatbot.png)

# Citation

We would like to acknowledge the significant contributions of these works to our project. These were the sources we consulted for our work.

1. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks: https://arxiv.org/abs/2005.11401

2. LangChain: https://python.langchain.com/v0.2/docs/introduction/

3. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks: https://arxiv.org/abs/1908.10084

4. all-MiniLM-L6-v2: https://sbert.net/

5. FAISS: https://github.com/facebookresearch/faiss/wiki

6. Gemini-pro: https://ai.google.dev/

7. Wikipedia dataset: https://huggingface.co/datasets/legacy-datasets/wikipedia

8. BootStrap 5.0 Documentation: https://getbootstrap.com/docs/5.0/getting-started/introduction/

9. Flask documentation: https://flask.palletsprojects.com/en/3.0.x/

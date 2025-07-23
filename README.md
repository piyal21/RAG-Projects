

* RAG Pipeline : 
   
<img width="589" height="766" alt="RAG - visual selection" src="https://github.com/user-attachments/assets/04d83dd5-10f6-4fc2-bf39-ad2b3c216503" />

1. Setup Guide
   - Clone the repository
   - create a virtual environment
   - Install all the requirements [ requirements.txt ]
   - Create a .env file [ hold the openai api key ]

2. Tools Used
   - Language Model : OpenAI GPT
   - Embeddings : OpenAIEmbeddings (langchain)
   - Vectore Store : FAISS
   - Documnet Parsing : PyMuPDF
   - API Framework : FLASK
   - Coding Environment : VS Code

3. Sample Questions / Query
   - user query : বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?
   - output : ১৫ বছর

4. API documentation
   - Description: This FLASK API accepts a user query and returns an answer generated from the most relevant context in the document using a RAG (Retrieval-Augmented Generation) pipeline.

5. Evaluation Metrics
  - Groundness score is calculated in the [Rag_evaluation.ipynb] file




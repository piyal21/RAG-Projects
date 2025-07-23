# RAG-Projects

# Rag Pipeline : 
   
<img width="589" height="766" alt="RAG - visual selection" src="https://github.com/user-attachments/assets/04d83dd5-10f6-4fc2-bf39-ad2b3c216503" />

1. Setup Guide
   1.1 Clone the repository
   1.2 create a virtual environment
   1.3 Install all the requirements [ requirements.txt ]
   1.4 Create a .env file [ hold the openai api key ]

2. Tools Used
   - Language Model : OpenAI GPT
   - Embeddings : OpenAIEmbeddings (langchain)
   - Vectore Store : FAISS
   - Documnet Parsing : PyMuPDF
   - API Framework : FLASK
   - Coding Environment : VS Code

3. Sample Questions / Query
   user query : বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?
   output : ১৫ বছর

4. API documentation
   Description : Accepts the user qury and returns an answer generated based on the context from the document
   Request body :
     {
       "query":"question"
     }

   Response :
     {
       "answer" : "generate_answer"
     }

5. Evaluation Metrics
   Groundness score is calculated in the [Rag-_evaluation.ipynb] file

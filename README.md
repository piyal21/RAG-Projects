

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


6.Q/A : 
   - To extract text from the PDF I used  'fitz' library which is python binding for 'PyMuPDF'. Yes I have faced some challages during the extraction. As the library is not familiar with Bengali text,during extraction it would loose some meaningful words.So I used openAI[gpt -4.0-mini]  to hold the meaningful words during extraction.
   - Chunking is based on the character limit. I implemented the chunking using python but same as text extraction from pdf the chunking is leaving meaningful text no matter the chunk size or overlaping size . So I also used openAI to chunk the text and hold the meaning of the text.The meaning of the text is most important because without it the retrieval function will retrieve irrelevant data.
   - Embedding model used - OpenAIEmbeddings ( text-embedding-ada-002 ) from the langchain library.This models gives state-of-the-art semantic representations of the text. This embedding gives similar words position closely in the vector data base which is used for long-term-memory.
   - The comparison is done by embedding the query with the same embedding model and then computing similarity score with the stored chunks. For storing the chunks I used ( FAISS ) . The similarity searh method is ( Cosine Similarity )
   - By using the same embedding model to embed the query and the document chunks into the same semantic vector space, meaningful comparison is guaranteed. The system can interpret both inputs with the same contextual understanding because of this consistency.If the query does not contain enough data the retrieval may return less relevant data/chunks and the llm may hallucinate .But the system prompt is given in such a way that it will not asnwer if it does not know/get  the accurate [ground truth] answer.
   -  The rsults seems relevant, and if it doesn't show relevant information better chunking , improving the embedding and adding a post-retrieval filtering may enhance the performance.
     

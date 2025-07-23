import fitz
import openai
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


# Load API key from .env
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


#extract text from the pdf 
def extract_raw_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    texts = []
    for page in doc:
        texts.append(page.get_text())
    return "\n".join(texts)


# Clean the raw text using OpenAI
def clean_text_with_openai(raw_text):
    
    prompt = f"""
The following is raw extracted text from a Bangla literature PDF. 
Please clean it up into readable paragraphs, fix broken sentences, and keep the semantic meaning intact.

Raw text:
{raw_text}

Cleaned text:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()

pdf_path = "data/HSC26_Bangla_1st_Paper.pdf"
raw_text = extract_raw_pdf_text(pdf_path)
cleaned_text = clean_text_with_openai(raw_text)

print(cleaned_text[:100])


# Split the cleaned text into semantic chunks [ using OpenAI ]
def split_into_semantic_chunks(cleaned_text, desired_chunk_count=20):
    prompt = f"""
You are a helpful assistant. The following is a cleaned Bangla literature text.

Your task is to split the text into around {desired_chunk_count} semantically meaningful chunks. 
Each chunk should represent a complete idea, paragraph, or topic without breaking the meaning.
Separate each chunk using this delimiter:
====CHUNK====

Text:
{cleaned_text[:3500]}  # You can loop this if text is longer

Semantic Chunks:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    chunks_text = response.choices[0].message.content.strip()
    chunks = [chunk.strip() for chunk in chunks_text.split("====CHUNK====") if chunk.strip()]
    return chunks

semantic_chunks = split_into_semantic_chunks(cleaned_text)


embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
vector_store = FAISS.from_texts(chunks, embedding)
vector_store.save_local("index/faiss_index")


# Retrieve similar chunks using FAISS vector store
def retrieve_similar_chunks(user_query, top_k=3):
    
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

    vector_store = FAISS.load_local(
        "index/faiss_index",
        embedding,
        allow_dangerous_deserialization=True  
    )

    results = vector_store.similarity_search(user_query, k=top_k)
    return [doc.page_content for doc in results]


# implementing short term memory for the chatbot
short_term_memory = []
def update_short_term_memory(user_question, bot_answer, max_len=5):
    global short_term_memory
    if len(short_term_memory) >= max_len:
        short_term_memory.pop(0)  
    short_term_memory.append(f"User: {user_question}\nBot: {bot_answer}")
    
    


# Answer generation function using OpenAI
def generate_answer(query, short_term_memory, top_k=3):
    relevant_texts = retrieve_similar_chunks(query, top_k=top_k)
    context = "\n\n".join(relevant_texts)
    short_memory_context = "\n".join(short_term_memory) if short_term_memory else "No prior chat history."

    prompt = f"""
You are a knowledgeable assistant for Bangla literature Q&A.
Answer the user's question based on the context from a textbook.
Use both retrieved document and chat history if needed.

Chat History:
{short_memory_context}

Context:
{context}

User Question:
{query}

Answer very briefly, in one short phrase or word, directly and factually.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful and precise Bangla literature expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    answer = response['choices'][0]['message']['content'].strip()
    update_short_term_memory(query, answer)
    return answer


#sample imput 
if __name__ == "__main__":
    user_query = "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"
    answer = generate_answer(user_query, short_term_memory)
    print(f"User: {user_query}\nBot: {answer}")


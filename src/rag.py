from langchain_core.tools import tool

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma(
    persist_directory="database",
    embedding_function=embeddings,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


@tool
def rag_search(question: str) -> str:
    """
    Search the local AWS knowledge base.
    Use this tool whenever the user asks about AWS,
    Amazon Bedrock, IAM, EC2, S3, Lambda,
    VPC, SageMaker or Amazon Q.
    """

    docs = retriever.invoke(question)

    seen = set()
    context = []

    for doc in docs:
        if doc.page_content not in seen:
            context.append(doc.page_content)
            seen.add(doc.page_content)

    return "\n\n".join(context)

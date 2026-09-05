import os

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader
)

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_qdrant import QdrantVectorStore


QDRANT_URL = "http://localhost:6333"

COLLECTION_NAME = "ocp_knowledge"


DOCUMENT_PATH = (
    "app/knowledge/documents"
)


def load_markdown_documents():

    loader = DirectoryLoader(
        DOCUMENT_PATH,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={
            "encoding": "utf-8"
        }
    )


    documents = loader.load()


    print(
        f"Loaded documents: {len(documents)}"
    )


    return documents



def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,

        separators=[
            "\n# ",
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            " "
        ]
    )


    chunks = splitter.split_documents(
        documents
    )


    print(
        f"Generated chunks: {len(chunks)}"
    )


    return chunks



def create_embeddings():

    embeddings = HuggingFaceEmbeddings(

        model_name=
        "BAAI/bge-small-en-v1.5",

        model_kwargs={
            "device":"cpu"
        },

        encode_kwargs={
            "normalize_embeddings":True
        }
    )


    return embeddings



def save_to_qdrant(
        chunks,
        embeddings
):

    vectorstore = (
        QdrantVectorStore.from_documents(

            documents=chunks,

            embedding=embeddings,

            url=QDRANT_URL,

            collection_name=
            COLLECTION_NAME
        )
    )


    print(
        "Successfully stored into Qdrant"
    )


    return vectorstore



def main():

    docs = load_markdown_documents()


    chunks = split_documents(
        docs
    )


    embeddings = create_embeddings()


    save_to_qdrant(
        chunks,
        embeddings
    )



if __name__ == "__main__":

    main()
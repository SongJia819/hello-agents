import asyncio

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore


QDRANT_URL = "http://localhost:6333"

COLLECTION_NAME = "ocp_knowledge"


def create_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",

        model_kwargs={
            "device": "cpu"
        },

        encode_kwargs={
            "normalize_embeddings": True
        }
    )


    vectorstore = (
        QdrantVectorStore.from_existing_collection(
            collection_name=COLLECTION_NAME,
            url=QDRANT_URL,
            embedding=embeddings
        )
    )


    return vectorstore



async def test_query(
        vectorstore,
        query
):

    print("\n")
    print("=" * 80)
    print("QUERY:")
    print(query)
    print("=" * 80)


    docs = vectorstore.similarity_search_with_score(
        query,
        k=5
    )


    for index, (doc, score) in enumerate(docs):

        print("\n")
        print(
            f"TOP {index+1}"
        )

        print(
            f"Score: {score}"
        )


        print(
            "Metadata:"
        )

        print(
            doc.metadata
        )


        print(
            "Content:"
        )

        print(
            doc.page_content[:500]
        )


        print("-"*50)



async def main():

    vectorstore = create_vectorstore()


    test_cases = [

        "How to create openshift cluster"

    ]


    for query in test_cases:

        await test_query(
            vectorstore,
            query
        )



if __name__ == "__main__":

    asyncio.run(main())
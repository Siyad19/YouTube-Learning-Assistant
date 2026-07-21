from tools.embeddings import create_vectorstore

def test_create_vectorstore():

    transcript = "This is a sample transcript for testing the create_vectorstore function."
    vector_store = create_vectorstore(transcript)

    assert vector_store is not None

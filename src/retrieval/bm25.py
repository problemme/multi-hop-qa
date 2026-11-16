from src.common import Document

class BM25Retriever:
    def __init__(self, documents: list[Document]):
        from rank_bm25 import BM25Okapi
        self.documents = documents
        self.index = BM25Okapi([d.text.lower().split() for d in documents])

    def retrieve(self, query: str, top_k: int = 5) -> list[Document]:
        if not self.documents:
            return []
        scores = self.index.get_scores(query.lower().split())
        indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [Document(self.documents[i].doc_id, self.documents[i].text,
                         float(scores[i]), self.documents[i].source) for i in indices]

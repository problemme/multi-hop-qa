from dataclasses import dataclass, asdict
from typing import Protocol

@dataclass
class Document:
    doc_id: str
    text: str
    score: float = 0.0
    source: str = ""

class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int = 5) -> list[Document]: ...

class Generator(Protocol):
    def generate(self, prompt: str) -> str: ...

def to_dict(item):
    return asdict(item)

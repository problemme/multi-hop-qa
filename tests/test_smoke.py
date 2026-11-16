from src.common import Document
from src.baselines.ircot import run_ircot
from src.baselines.react import run_react
from src.evaluation.metrics import exact_match, token_f1

class FakeGenerator:
    def generate(self, prompt):
        if "Choose exactly" in prompt:
            return "FINAL: Paris"
        if "Answer the question" in prompt:
            return "Paris"
        return "Find the capital"

class FakeRetriever:
    def retrieve(self, query, top_k=5):
        return [Document("doc1", "Paris is the capital of France.")]

def test_ircot():
    result = run_ircot("Capital of France?", FakeGenerator(), FakeRetriever())
    assert result["answer"] == "Paris"
    assert result["evidence"][0]["doc_id"] == "doc1"

def test_react():
    result = run_react("Capital of France?", FakeGenerator(), FakeRetriever())
    assert result["answer"] == "Paris"

def test_metrics():
    assert exact_match("Paris!", "paris") == 1.0
    assert token_f1("Paris France", "Paris") > 0


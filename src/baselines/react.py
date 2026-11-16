"""Bounded ReAct-style controller with explicit search action parsing."""
import re
from dataclasses import asdict

def run_react(question, generator, retriever, max_steps=3, top_k=3):
    history = []
    evidence = {}
    for step in range(max_steps):
        response = generator.generate(
            f"Question: {question}\nHistory: {history}\n"
            "Choose exactly one line: SEARCH: <query> or FINAL: <answer>"
        ).strip()
        match = re.search(r"(?im)^\s*(SEARCH|FINAL)\s*:\s*(.+)$", response)
        if match and match.group(1).upper() == "FINAL":
            return {"question": question, "answer": match.group(2).strip(),
                    "steps": history, "evidence": [asdict(d) for d in evidence.values()]}
        query = match.group(2).strip() if match and match.group(1).upper() == "SEARCH" else question
        docs = retriever.retrieve(query, top_k)
        evidence.update({d.doc_id: d for d in docs})
        history.append({"step": step + 1, "query": query,
                        "observations": [{"doc_id": d.doc_id, "text": d.text} for d in docs]})
    answer = generator.generate(
        f"Question: {question}\nEvidence: {[asdict(d) for d in evidence.values()]}\n"
        "Give the final short answer, or unknown if unsupported."
    )
    return {"question": question, "answer": answer, "steps": history,
            "evidence": [asdict(d) for d in evidence.values()]}

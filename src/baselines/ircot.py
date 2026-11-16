"""Minimal IRCoT-style iterative retrieve-then-reason controller."""
from dataclasses import asdict

def run_ircot(question, generator, retriever, max_steps=2, top_k=3):
    trace = []
    thoughts = []
    evidence = {}
    query = question
    for step in range(max_steps):
        docs = retriever.retrieve(query, top_k)
        evidence.update({d.doc_id: d for d in docs})
        context = "\n".join(f"[{d.doc_id}] {d.text}" for d in docs)
        thought = generator.generate(
            f"Question: {question}\nPrior reasoning: {' '.join(thoughts)}\n"
            f"Evidence:\n{context}\nWrite one concise reasoning step and identify what remains unknown."
        )
        thoughts.append(thought)
        trace.append({"step": step + 1, "query": query,
                      "doc_ids": [d.doc_id for d in docs], "thought": thought})
        query = thought
    context = "\n".join(f"[{d.doc_id}] {d.text}" for d in evidence.values())
    answer = generator.generate(
        f"Answer the question using only the evidence. If insufficient, say unknown.\n"
        f"Question: {question}\nEvidence:\n{context}\nAnswer:"
    )
    return {"question": question, "answer": answer, "steps": trace,
            "evidence": [asdict(d) for d in evidence.values()]}

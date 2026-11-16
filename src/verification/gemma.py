"""Verifier contract; Gemma loading is opt-in and separate from Qwen."""
class GemmaVerifier:
    def __init__(self, model_id="google/gemma-2-2b-it"):
        from transformers import pipeline
        self.pipe = pipeline("text-generation", model=model_id,
                             device_map="auto", torch_dtype="auto")

    def verify(self, claim, evidence):
        context = "\n".join(f"[{d['doc_id']}] {d['text']}" for d in evidence)
        prompt = ("Assess whether the claim is supported by evidence. "
                  "Begin with SUPPORTED, UNSUPPORTED, or INSUFFICIENT_EVIDENCE.\n"
                  f"Claim: {claim}\nEvidence:\n{context}")
        messages = [{"role": "user", "content": prompt}]
        raw = self.pipe(messages, max_new_tokens=128, do_sample=False)[0]["generated_text"]
        text = raw[-1]["content"] if isinstance(raw, list) else str(raw)
        verdict = next((v for v in ("INSUFFICIENT_EVIDENCE", "UNSUPPORTED", "SUPPORTED")
                        if text.strip().upper().startswith(v)), "INSUFFICIENT_EVIDENCE")
        return {"verdict": verdict, "reason": text, "evidence_ids": [d["doc_id"] for d in evidence]}

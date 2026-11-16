# Starter code quickstart

This is a scaffold, not a validated research result. No model weights belong in Git.

## Install
```bash
pip install -r requirements.txt
pip install transformers accelerate torch rank-bm25 pytest
pytest -q
```

## Qwen on a GPU runtime
```python
from src.models.qwen import QwenGenerator
model = QwenGenerator("Qwen/Qwen2.5-1.5B-Instruct")
print(model.generate("Answer briefly: What is multi-hop QA?"))
```

The model is fetched from Hugging Face on first run and cached locally.
Gemma model access may require accepting the model license and authenticating to Hugging Face.
For a limited GPU, do not load Qwen and Gemma simultaneously until memory has been measured.

## Next steps
Replace naive whitespace BM25 tokenization for the target corpus, add dataset loaders,
persistent indexes, strict JSONL logs, verified evidence citations, structured ReAct
parsing and rigorous evaluator integration. Run model-backed integration tests on GPU.

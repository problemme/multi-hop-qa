"""Lazy Hugging Face Qwen loader. GPU recommended."""
class QwenGenerator:
    def __init__(self, model_id="Qwen/Qwen2.5-1.5B-Instruct", max_new_tokens=256):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, torch_dtype="auto", device_map="auto"
        )
        self.max_new_tokens = max_new_tokens

    def generate(self, prompt: str) -> str:
        import torch
        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        with torch.inference_mode():
            output = self.model.generate(**inputs, max_new_tokens=self.max_new_tokens,
                                         do_sample=False)
        return self.tokenizer.decode(output[0][inputs.input_ids.shape[-1]:],
                                     skip_special_tokens=True)

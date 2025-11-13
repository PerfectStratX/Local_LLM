# ...existing code...
from llama_cpp import Llama
import traceback
import os

# Optional: local tokenizer support (uncomment if you have tokenizers installed and a tokenizer.json)
# from tokenizers import Tokenizer
# tokenizer_path = "tokenizer.json"
# if os.path.exists(tokenizer_path):
#     tokenizer = Tokenizer.from_file(tokenizer_path)
# else:
#     tokenizer = None

# ── 1. Load the GGUF model with llama-cpp-python ──
model_path = "deepseek-coder-6.7b-instruct.Q2_K.gguf"   # <-- change if you downloaded another

# Load the GGUF model directly with error reporting
try:
    model = Llama(
        model_path=model_path,
        n_gpu_layers=-1,  # -1 means use GPU if available, 0 means CPU only
        n_ctx=4096,       # context window size
        verbose=False
    )
except Exception as e:
    print("Failed to load model:", e)
    traceback.print_exc()
    raise

# ── 2. Chat loop ───────────────────────────────────────────────────────
print("Local LLM ready. Type 'quit' to exit.\n")
while True:
    try:
        user = input("You: ").strip()
    except EOFError:
        break

    if user.lower() in {"quit", "exit"}:
        break
    if not user:
        continue

    # Call the model using __call__ (most reliable for llama-cpp-python)
    resp = None
    try:
        resp = model(
            prompt=user,
            max_tokens=256,
            temperature=0.7,
            top_p=0.9
        )
    except Exception as e:
        print("model() call failed:", e)
        traceback.print_exc()
        continue

    # Robust extraction of text from different return shapes
    reply = None
    try:
        reply = resp["choices"][0]["text"]
    except Exception:
        try:
            reply = resp.choices[0].text
        except Exception:
            reply = str(resp)

    reply = reply.strip()
    if reply.startswith(user):
        reply = reply[len(user):].strip()

    print("AI:", reply, "\n")
# ...existing code...
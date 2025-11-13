# Local LLM Chat

A simple local chatbot using Deepseek Coder 6.7B (or any other model: scroll to setup)  with llama-cpp-python.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [How It Works](#how-it-works)
4. [Setup](#setup)
5. [Usage](#usage)

## Overview

This project runs a quantized Deepseek Coder model locally on your machine for interactive chat. No API calls, no internet required—everything runs offline.

## Requirements

- Python 3.8+
- `llama-cpp-python` library
- `deepseek-coder-6.7b-instruct.Q2_K.gguf` model file (quantized GGUF format)
- 4GB+ RAM (or VRAM if using GPU acceleration)

## How It Works

### 1. **Model Loading**
The script loads the GGUF quantized model using `llama-cpp-python`, a Python binding for llama.cpp.
- GPU layers: `-1` means use GPU if available; set to `0` to force CPU-only
- Context window: 4096 tokens (max input/output length)

### 2. **Chat Loop**
The program enters an interactive loop:
- Waits for user input (`You: `)
- Passes the prompt to the model
- Returns the AI response (`AI: `)
- Repeats until you type `quit` or `exit`

### 3. **Response Handling**
The code handles different return formats from llama-cpp-python and cleans up the response:
- Extracts text from `resp["choices"][0]["text"]`
- Strips whitespace and removes echoed prompts

## Setup

1. **Install dependencies**
   ```bash
   pip install llama-cpp-python
   ```

2. **Place the model file**
   Download `deepseek-coder-6.7b-instruct.Q2_K.gguf` (or any other GGUF model) and save it in the same directory as `local_LLM.py`.
   
   Other popular models you can use:
   - `mistral-7b-instruct.Q4_K_M.gguf` (Mistral 7B)
   - `neural-chat-7b.Q4_K_M.gguf` (Intel Neural Chat)
   - `orca-mini-7b.Q4_K_M.gguf` (Orca Mini)
   - `llama-2-7b-chat.Q4_K_M.gguf` (Llama 2)

3. **Adjust the model path in the code** (if using a different model)
   
   Open `local_LLM.py` and find this line:
   ```python
   model_path = "deepseek-coder-6.7b-instruct.Q2_K.gguf"   # <-- change if you downloaded another
   ```
   
   Replace the filename with your model:
   ```python
   model_path = "mistral-7b-instruct.Q4_K_M.gguf"  # Example: use Mistral instead
   ```
   
   That's it! The rest of the code will work with any GGUF model.

3. **(Optional) Use GPU acceleration**
   - NVIDIA: Install `llama-cpp-python[cuda]`
   - Metal (macOS): Should work automatically
   - ROCm (AMD): Install `llama-cpp-python[rocm]`

## Usage

```bash
python3 local_LLM.py
```

Example session:
```
Local LLM ready. Type 'quit' to exit.

You: What is Python?
AI: Python is a high-level, interpreted programming language...

You: quit
```

Type `quit` or `exit` to stop the chat.

---

**Note:** First run may be slow as the model loads into memory. Subsequent responses depend on your hardware (typically 5-30 seconds on CPU).

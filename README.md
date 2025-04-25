- 👋 Hi, I’m @Shembazai
- 👀 I’m interested in Python coding.
- 🌱 I’m currently learning it.
- 💞️ I’m looking to collaborate on coding ethical AI/AGI.
- 📫 How to reach me : shembazai@gmail.com
      For business related things: outofhtematrix2026@gmail.com

# 🔥 Shemba’s AI Financial System – Monthly Recap March 2025

## 🧠 AI Financial System – COMPLETE

### ✅ `financial_agent.py`
- Loads and cleans your financial data (`AI_budget.csv`)
- Provides:
  - Account adjustment
  - Monthly summaries
  - Natural language Q&A using **Mistral**
- Auto-runs `docs_merger.py` to consolidate `.ods` and `.pdf` data
- Integrated Mistral to answer financial questions like:
  - _“How much will I have by month-end?”_
  - _“What’s my average spending?”_

---

## 🧼 Data Pipeline

### ✅ `data_filter.py`
- Merges `.pdf` and `.ods` inputs
- Sanitizes and deduplicates entries
- Ensures clean CSV format for model use

### ✅ `docs_merger.py` Patch
- Final cleanup step auto-fixes broken rows
- Ensures no string-based `amounts` or malformed dates
- Keeps your AI_budget.csv reliable

---

## 🧠 Mistral Fine-Tuning – DONE

### ✅ `prepare_training_data.py`
- Generated a `training_data.jsonl` file with:
  - Income/expense patterns
  - Forecast prompts like “How much will I have this month?”
- Built from your actual transaction history

### ✅ `finetune_mistral.py`
- Full LoRA fine-tuning pipeline
- Hugging Face model: `mistralai/Mistral-7B-v0.1`
- Quantized 4-bit with `bitsandbytes`
- Runs entirely on your **RTX 3060 Ti**


### ✅ `test_finetuned_mistral.py`
- Interactive Q&A chat with your fine-tuned model
- Built-in prompt formatting
- Uses pipeline with temperature + top-p sampling






<!---
Shembazai/Shembazai is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

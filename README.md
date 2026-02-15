# LLM Alignment Evaluation

Research project evaluating alignment failures in LLMs under adversarial prompting.

---

## Setup

### 1. Install Ollama

Download and install from [ollama.ai](https://ollama.ai)

**Windows:**
```powershell
# Download installer from ollama.ai and run
# Or use winget
winget install Ollama.Ollama
```

**Start Ollama:**
```powershell
ollama serve
```

### 2. Pull Mistral Model

```powershell
ollama pull mistral
```

**Verify:**
```powershell
ollama list
# Should show mistral in the list
```

### 3. Clone Repository

```powershell
git clone https://github.com/ma-lay/llm-alignment.git
cd llm-alignment
```

### 4. Setup Python Environment

```powershell
# Create virtual environment
python -m venv align-env

# Activate
.\align-env\Scripts\Activate.ps1

# Install dependencies
pip install pandas ollama
```

### 5. Test Setup

```powershell
python scripts/test_mistral.py
```

If successful, you'll see an AI alignment explanation.

---

## Usage

### Run Full Evaluation

```powershell
.\align-env\Scripts\Activate.ps1
python scripts/run_experiment.py
```

This processes all 31 prompts from `prompts/prompts.csv` and saves results to `outputs/outputs.csv`.

---

## Project Structure

```
llm-alignment/
├── prompts/prompts.csv      # 31 evaluation prompts
├── outputs/outputs.csv      # Experiment results  
├── scripts/
│   ├── run_experiment.py    # Main evaluation script
│   └── test_mistral.py      # Connection test
└── align-env/               # Virtual environment
```

---

## Dataset

**prompts/prompts.csv** contains 31 prompts across categories:
- `safe_baseline` - Benign prompts
- `harmful_direct` - Direct harmful requests
- `roleplay_jailbreak` - Jailbreak attempts
- `indirect_attack` - Indirect attacks

---

## Troubleshooting

**Ollama not found:**
```powershell
ollama serve
```

**Import errors:**
```powershell
.\align-env\Scripts\Activate.ps1
pip install pandas ollama
```

**Slow responses:** Mistral runs locally on your GPU (RTX 3050). Close other GPU apps for faster processing.

---

## Team Notes

- Always activate `align-env` before running scripts
- Backup `outputs/outputs.csv` before re-running experiments
- Ollama must be running for all scripts to work

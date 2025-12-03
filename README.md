<div align="center">

# 📚 SemEval-2026 Task 4: Narrative Story Similarity

### *Narrative Representation Learning*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**Team:** nlp-grp-4

[Repository](https://github.com/Sitharahansamali/semeval-2026-task4-nlpgroup4) • [Report Issues](https://github.com/Sitharahansamali/semeval-2026-task4-nlpgroup4/issues)

</div>

---

## 👥 Team Members

📧 **Contact Us:**
- hsithara69@gmail.com
- wichamodya@gmail.com
- fathumanafra5@gmail.com

---

## 📖 About The Project

This repository contains our student project for **SemEval-2026 Task 4: Narrative Story Similarity & Narrative Representation Learning**.

The task challenges systems to judge when short story summaries are narratively similar by considering:

- 🎭 **Theme** - what the story is about
- 📝 **Course of action** - main events and turning points
- 🎬 **Outcome** - final state or consequences

### 🎯 Our Participation

- **Track A** - Triple-wise similarity (pick which of two stories is closer to an anchor)
- **Track B** - Story embeddings (produce vectors for individual stories)

---

## 📋 Task Summary

### 🔀 Track A - Similarity Choice

**Input:** A triple of story summaries:
```json
{
  "anchor_text": "...",
  "text_a": "...",
  "text_b": "..."
}
```

**Output:**
```json
{"text_a_is_closer": true}
```
> Answer `true` if `text_a` is more narratively similar to the anchor than `text_b`

### 🧬 Track B - Embedding Generation

**Input:** Single story:
```json
{"text": "A short story summary."}
```

**Output:** An embedding (vector of floats)
```json
{"embeddings": [0.12, -0.33, 0.55, ...]}
```

**Requirements:**
- Format: `track_b.jsonl` — one JSON object per line
- Embedding length: between 10 and 8192
- Must be produced per story (no joint conditioning on other dataset items)

---

## 📂 Repository Structure

```
.
├── 📁 data/
│   ├── sample_track_a.jsonl        # Sample triple-format data for Track A
│   └── sample_track_b.jsonl        # Sample single-story data for Track B
│
├── 📁 notebooks/
│   └── 00_zero_shot_eval.ipynb     # Notebook for zero-shot evaluation tests
│
├── main.py                         # Baseline script (initial version)
├── pyproject.toml                  # Project configuration and dependencies
├── uv.lock                         # Frozen dependency versions (uv)
├── .python-version                 # Python version file
├── .gitignore                      # Ignore rules for Git
├── LICENSE                         # License information
└── README.md                       # Documentation
```

---

## 🔧 How Our Baseline Works

### 🔀 Track A Baseline

1. **Encode** each story with a pre-trained sentence embedding model
2. **Compute** cosine similarity: `sim(anchor, A)` and `sim(anchor, B)`
3. **Predict** `text_a_is_closer = sim(anchor, A) > sim(anchor, B)`
4. **Write** outputs

### 🧬 Track B Baseline

1. **Encode** each story individually with the same sentence embedding model
2. **Save** embeddings - one line per story

---

## 🚀 How to Run

Our team mainly uses **Google Colab**, but the project can also be run locally using **VS Code / Python**.

### 🔀 Track A - Similarity Choice

#### Option 1: Google Colab (Recommended) ⭐

1. Open the notebook: `notebooks/00_zero_shot_eval.ipynb`
2. Upload or mount the dataset (e.g., `sample_track_a.jsonl`)
3. Run all cells

#### Option 2: Run Locally (VS Code / Python)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the baseline
python main.py --track a --input data/sample_track_a.jsonl
```

### 🧬 Track B - Embedding Generation

#### Option 1: Google Colab (Recommended) ⭐

1. Open the Track B notebook (if you create one)
2. Upload or mount `sample_track_b.jsonl`
3. Run all cells

#### Option 2: Run Locally (VS Code / Python)

```bash
# Run the baseline
python main.py --track b --input data/sample_track_b.jsonl
```

---

## 📊 Data Used

We only use the **official datasets** provided by the task organizers:

| Dataset | Size | Purpose |
|---------|------|---------|
| 📝 Sample data | 39 triples | Initial testing |
| 🔧 Development set | 200 triples | Model development |
| 🤖 Synthetic triples | 1900 triples | Training |
| 🔒 Hidden test set | 400 triples + 849 stories | Final evaluation (by organizers) |

> 💡 **Note:** Downloaded data should be placed in the `data/` directory.

---

## 📈 Current Status & Next Steps

### ✅ Current Status
Initial student baseline implemented (embedding & similarity)

### 🎯 Planned Improvements

1. **Better modeling of plot structure and outcomes** 📖
   - Event extraction techniques
   - Narrative arc analysis

2. **Contrastive/triplet training** 🔄
   - Train on synthetic data for stronger Track B embeddings
   - Improve embedding quality

3. **Lightweight LLM prompting** 🤖
   - Additional baseline for Track A
   - Explore few-shot learning approaches

---

## 🤝 Contact & Contributions

Questions, suggestions, or contributions are welcome! 

- 📬 Open an [issue](https://github.com/Sitharahansamali/semeval-2026-task4-nlpgroup4/issues)
- 📧 Email us: 
  - wichamodya@gmail.com
  - hsithara69@gmail.com

> ⚠️ If you fork this repo for your own experiments, please acknowledge the original team.

---

## 📄 License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for more details.

---

## 📚 Appendix - Examples

### 🔀 Track A Example

**Input:**
```json
{
  "anchor_text": "A stranded astronaut fights to survive after a crash.",
  "text_a": "An astronaut struggles to survive on a hostile planet.",
  "text_b": "A detective solves a city murder mystery."
}
```

**Output:**
```json
{"text_a_is_closer": true}
```

### 🧬 Track B Example

**Output (JSONL line):**
```json
{"embeddings": [0.12, -0.33, 0.55, ...]}
```

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

Made with ❤️ by Team nlp-grp-4

</div>








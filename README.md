SemEval-2026 Task 4: Narrative Story Similarity and Narrative Representation Learning

Team : nlp-grp-4
Repository:  https://github.com/Sitharahansamali/semeval-2026-task4-nlpgroup4
Contact: hsithara69@gmail.com
         wichamodya@gmail.com
         fathumanafra5@gmail.com

This repository contains our student project for SemEval-2026 Task 4: Narrative Story Similarity & Narrative Representation Learning.
The task asks systems to judge when short story summaries are narratively similar - considering:

Theme - what the story is about

Course of action - main events and turning points

Outcome - final state or consequences

We participate in:

Track A - Triple-wise similarity (pick which of two stories is closer to an anchor)

Track B - Story embeddings (produce vectors for individual stories)

**1. Task Summary**

_Track A - Similarity Choice_

Input : a triple of story summaries:

anchor_text
text_a
text_b

Output per triple:

{"text_a_is_closer": true}

(Answer **true** if **text_a** is more narratively similar to the anchor than **text_b**)

_Track B - Embedding Generation_

Input: Single story:

{"text": "A short story summary."}

Output: an embedding (vector of floats).Accepted formats:
  track_b.jsonl — one JSON object per line: {"embeddings": [ ... ]}

Embedding length must between 10 and 8192. Track B embeddings must produced per story(no joint conditioning on other dataset items).

**2. Repo Structure**

.
├── data/
│   ├── sample_track_a.jsonl        # Sample triple-format data for Track A
│   └── sample_track_b.jsonl        # Sample single-story data for Track B
│
├── notebooks/
│   └── 00_zero_shot_eval.ipynb     # Notebook for zero-shot evaluation tests
│
├── main.py                         # Baseline script (initial version)
├── pyproject.toml                  # Project configuration and dependencies
├── uv.lock                         # Frozen dependency versions (uv)
├── .python-version                 # Python version file
├── .gitignore                      # Ignore rules for Git
├── LICENSE                         # License information
└── README.md                       # Documentation


**3. How our baseline works**

_Track A baseline_

1.Encode each story with a pre-trained sentence embedding model.
2.Compute cosine similarity: sim(anchor, A) and sim(anchor, B).
3.Predict text_a_is_closer = sim(anchor, A) > sim(anchor, B).
4.Write outputs

_Track B baseline_

1.Encode each story individually with the same sentence embedding model.
2.Save embeddings-one line per story.

**4.How to Run**

Our team mainly uses Google Colab, but the project can also be run locally using VS Code / Python.
Both methods are described below.

_Track A - Similarity Choice_

Option 1: Run in Google Colab (Recommended)

1.Open the notebook:

notebooks/00_zero_shot_eval.ipynb

2.Upload or mount the dataset (e.g., sample_track_a.jsonl).

3.Run all cells.

Option 2: Run Locally (VS Code / Python)

_Track B — Embedding Generation_

Option 1: Run in Google Colab (Recommended)

1.Open the Track B notebook (if you create one).

2.Upload or mount sample_track_b.jsonl.

3.Run all cells.

Option 2: Run Locally (VS Code / Python)



**5. Data used**

We only use the official datasets provided by the task organizers:

Sample data (39 triples)

Development set (200 triples)

Synthetic triples (1900) for training

Hidden test set (400 triples + 849 stories) - evaluated by the organizers

(Downloaded data should be placed in data/.)

**6. Current status & next steps**

Status: Initial student baseline implemented (embedding & similarity).
Planned improvements:

 1.Better modeling of plot structure and outcomes (event extraction).

2.Contrastive/triplet training on synthetic data for stronger Track B embeddings.

3.Lightweight LLM prompting as an additional baseline for Track A.

**7. Contact & contributions**

Questions, suggestions, or contributions are welcome - open an issue or contact: wichamodya@gmail.com , hsithara69@gmail.com . If you fork this repo for your own experiments, please acknowledge the original team.

**8.License**

This project is released under the MIT License.

**9.Appendix-example**

_Track A example input:_

{
  "anchor_text": "A stranded astronaut fights to survive after a crash.",
  "text_a": "An astronaut struggles to survive on a hostile planet.",
  "text_b": "A detective solves a city murder mystery."
}

_Track A example output:_

{"text_a_is_closer": true}

_Track B example output (JSONL line):_

{"embeddings": [0.12, -0.33, 0.55, ...]}








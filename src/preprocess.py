import json

def build_prompt(anchor, A, B):
    return f"""
You are an expert in analyzing narrative similarity. 
Your job is to decide whether Story A or Story B is more narratively similar to the anchor story.

Anchor story:
{anchor}

Story A:
{A}

Story B:
{B}

Answer only with A or B.
"""

def convert_file(input_path, output_path):
    with open(output_path, "w") as out:
        with open(input_path) as f:
            for line in f:
                row = json.loads(line)
                prompt = build_prompt(row["anchor_text"], row["text_a"], row["text_b"])
                answer = row["text_a_is_closer"]
                out.write(json.dumps({"prompt": prompt, "answer": answer}) + "\n")

if __name__ == "__main__":
    convert_file("data/sample_track_a.jsonl", "data/sample_track_a_prepared.jsonl")
    convert_file("data/dev_track_a.jsonl", "data/dev_track_a_prepared.jsonl")

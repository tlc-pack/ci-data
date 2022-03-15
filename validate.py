import argparse
import json
import yaml
import unittest


from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
FILES_DIR = REPO_ROOT / "files"
README = REPO_ROOT / "README.md"


README_PREAMBLE = """
This repo is used to house binary files used in [TVM's](https://github.com/apache/tvm) Jenkins [CI](https://ci.tlcpack.ai).

To add a file to this repo, send a PR with:

1. The file itself. For example:
    ```bash
    cd files
    curl -LO https://github.com/tensorflow/tflite-micro/raw/main/tensorflow/lite/micro/examples/micro_speech/micro_speech.tflite
    ```
2. An entry into [`files.json`](files.json) and run `python validate.py` to insert an entry into the table below
    ```bash
    pip install -r requirements.txt
    python validate.py
    git add .
    ```

| Filename | Source URL |
| -------- | ---------- |
""".lstrip()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate the state of binary files in the repo. Every file should have an entry in files.json and exist in the repo at the specified path')
    parser.add_argument('--check', action='store_true', help="don't update README.md, exit if there are changes")

    args = parser.parse_args()

    with open(REPO_ROOT / "files.yml") as f:
        files = yaml.safe_load(f)

    table_lines = []
    seen_files = set()
    for item in files:
        source_url = item["source"]
        filename = FILES_DIR / item["filename"]
        seen_files.add(str(filename.relative_to(REPO_ROOT)))

        if not filename.exists():
            raise RuntimeError(f"Expected to find file {filename} from {source_url} but file did not exist")
        
        table_lines.append(f"| [`{filename.relative_to(FILES_DIR)}`]({filename.relative_to(REPO_ROOT)}) | {source_url} |")

    for filename in FILES_DIR.glob("*"):
        if str(filename.relative_to(REPO_ROOT)) not in seen_files:
            raise RuntimeError(f"Missing entry in files.yml for {filename.relative_to(FILES_DIR)}")

    new_readme = README_PREAMBLE + "\n".join(table_lines)

    if args.check:
        tc = unittest.TestCase()
        tc.maxDiff = float('inf')

        with open(README) as f:
            current_readme = f.read()
        
        tc.assertEqual(current_readme, new_readme)
    else:
        with open(README, "w") as f:
            f.write(new_readme)

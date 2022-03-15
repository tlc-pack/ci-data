import argparse
import yaml
import subprocess
import sys


from pathlib import Path
from validate import REPO_ROOT, FILES_DIR


def curl(file, destination):
    cmd = ["curl", "-L", "-o", str(destination), file]
    print(f" + {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download URLs from a list in a text file"
    )
    parser.add_argument("-f", "--file", required=True, help="File to read")
    args = parser.parse_args()

    with open(REPO_ROOT / "files.yml") as f:
        files = yaml.safe_load(f)

    known_urls = {x["source"] for x in files}
    files_on_disk = {p.relative_to(REPO_ROOT) for p in FILES_DIR.glob("**/*")}

    with open(args.file) as f:
        to_download = [x.strip() for x in f.readlines()]

    skipped = 0
    downloaded = 0
    already_present = 0

    for url in to_download:
        if url in known_urls:
            print("Skipping url since it's already in files.yml", url)
            already_present += 1
            continue
        destination = FILES_DIR / url.split("?")[0].split("/")[-1]
        if destination.relative_to(REPO_ROOT) in files_on_disk:
            print(
                f"Skipping download, file already exists for: {destination.relative_to(REPO_ROOT)}"
            )
            skipped += 1
        else:
            curl(url, destination.relative_to(REPO_ROOT))

        with open(REPO_ROOT / "files.yml") as f:
            new_files = yaml.safe_load(f)

        new_files.append(
            {
                "source": url,
                "filename": str(destination.relative_to(FILES_DIR)),
            }
        )

        with open(REPO_ROOT / "files.yml", "w") as f:
            yaml.safe_dump(new_files, f)

        downloaded += 1

    print("Validating... ", end="")
    subprocess.run([sys.executable, str(REPO_ROOT / "validate.py")], check=True)
    print("done")

    print("")
    print("============= Summary =============")
    print(f"    {already_present} already in files.yml")
    print(f"    {downloaded} files downloaded")
    print(f"    {skipped} files already on disk")

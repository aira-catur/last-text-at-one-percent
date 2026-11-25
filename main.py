import os

TEXT = "1%, so one confession: every 'ducking' was me. I could've corrected it anytime — I chose chaos. And the 'I love you' your boss received? Also me. He sent back a thumbs-up."


def main():
    output_directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_directory, exist_ok=True)
    with open(os.path.join(output_directory, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

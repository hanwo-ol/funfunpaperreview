import os
import json
import re

def extract_meta(filepath):
    title = os.path.basename(filepath).replace(".md", "")
    description = ""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            # Try to find first header for title
            header_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if header_match:
                title = header_match.group(1).strip()

            # Clean markdown formatting for description excerpt
            plain_text = re.sub(r"```[\s\S]*?```", "", content) # remove code blocks
            plain_text = re.sub(r"\$\$[\s\S]*?\$\$", "", plain_text) # remove display math
            plain_text = re.sub(r"[\#\*\_`\-\>]", " ", plain_text) # remove md chars
            lines = [line.strip() for line in plain_text.splitlines() if line.strip() and not line.startswith("---")]
            if lines:
                # Take first 150 chars as snippet
                description = " ".join(lines)[:200].strip()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return title, description

def build_tree(root_dir="."):
    ignore_dirs = {".git", "_layouts", "node_modules", ".github"}
    ignore_files = {"index.html", "viewer.html", "tree.json", "generate_tree.py"}

    def walk_dir(path):
        items = []
        try:
            entries = sorted(os.listdir(path))
        except OSError:
            return items

        for entry in entries:
            if entry in ignore_dirs or entry.startswith("."):
                continue
            full_path = os.path.join(path, entry)
            rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")

            if entry in ignore_files and path == root_dir:
                continue

            if os.path.isdir(full_path):
                children = walk_dir(full_path)
                if children: # Only include non-empty folders or folders with md
                    items.append({
                        "type": "dir",
                        "name": entry,
                        "path": rel_path,
                        "children": children
                    })
            elif entry.endswith(".md"):
                title, desc = extract_meta(full_path)
                items.append({
                    "type": "file",
                    "name": entry,
                    "path": rel_path,
                    "title": title,
                    "description": desc
                })
        return items

    return walk_dir(root_dir)

if __name__ == "__main__":
    tree = build_tree(".")
    with open("tree.json", "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)
    print("tree.json generated successfully.")

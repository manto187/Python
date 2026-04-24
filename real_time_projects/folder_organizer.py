"""
folder_organizer.py
-------------------
Automatically organizes your Downloads folder by file type.
For detailed instructions, see the README.md file.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIGURATION — edit this to customize
# ─────────────────────────────────────────────

# Automatically finds your Downloads folder.
# You can also hardcode it, e.g.:
#   DOWNLOADS = Path("C:/Users/YourName/Downloads")   # Windows
#   DOWNLOADS = Path("/home/yourname/Downloads")       # Linux
DOWNLOADS = Path.home() / "Downloads"

# Which subfolder each extension goes into.
# Add or change any extension → folder mapping here.
FILE_CATEGORIES = {
    # Images
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg",
               ".webp", ".ico", ".tiff", ".heic", ".raw"],

    # Videos
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv",
               ".flv", ".webm", ".m4v", ".3gp"],

    # Audio
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg",
              ".wma", ".m4a", ".opus"],

    # Documents
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt",
                  ".rtf", ".pages", ".md", ".epub"],

    # Spreadsheets
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".numbers"],

    # Presentations
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],

    # Archives (zip files etc.)
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz",
                 ".bz2", ".xz", ".iso"],

    # Code and scripts
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json",
             ".xml", ".sql", ".sh", ".bat", ".java", ".cpp",
             ".c", ".h", ".rs", ".go", ".rb", ".php"],

    # Executables and installers
    "Programs": [".exe", ".msi", ".dmg", ".deb", ".rpm",
                 ".apk", ".appimage"],

    # Fonts
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
}

# Files with these extensions (or no extension) go here
OTHERS_FOLDER = "Others"

# ─────────────────────────────────────────────
# CORE LOGIC — no need to edit below this line
# ─────────────────────────────────────────────

def build_extension_map(categories):
    """Flip the category dict into extension → folder_name."""
    ext_map = {}
    for folder_name, extensions in categories.items():
        for ext in extensions:
            ext_map[ext.lower()] = folder_name
    return ext_map


def get_safe_destination(destination_path):
    """
    If a file with this name already exists at the destination,
    add a number suffix instead of overwriting. E.g.:
        photo.jpg → photo_2.jpg → photo_3.jpg
    """
    if not destination_path.exists():
        return destination_path

    stem = destination_path.stem
    suffix = destination_path.suffix
    parent = destination_path.parent
    counter = 2

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        candidate = parent / new_name
        if not candidate.exists():
            return candidate
        counter += 1


def organize(downloads_path, ext_map, dry_run=False):
    """
    Walk the top level of downloads_path and move files into subfolders.
    Set dry_run=True to preview changes without actually moving anything.
    """
    if not downloads_path.exists():
        print(f"ERROR: Folder not found: {downloads_path}")
        print("Please check the DOWNLOADS path at the top of this script.")
        return

    moved = []
    skipped = []
    errors = []

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Organizing: {downloads_path}\n")
    print("─" * 55)

    for item in sorted(downloads_path.iterdir()):
        # Only process files at the top level — skip subfolders
        if not item.is_file():
            continue

        # Skip hidden files (e.g. .DS_Store on macOS)
        if item.name.startswith("."):
            skipped.append((item.name, "hidden file"))
            continue

        extension = item.suffix.lower()
        category = ext_map.get(extension, OTHERS_FOLDER)

        destination_folder = downloads_path / category
        destination = get_safe_destination(destination_folder / item.name)

        if dry_run:
            print(f"  WOULD MOVE  {item.name}")
            print(f"         → {category}/")
            moved.append((item.name, category))
            continue

        try:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
            print(f"  MOVED  {item.name}")
            print(f"     → {category}/")
            moved.append((item.name, category))
        except Exception as e:
            print(f"  ERROR  {item.name}: {e}")
            errors.append((item.name, str(e)))

    # Summary
    print("\n" + "─" * 55)
    print(f"  Done at {datetime.now().strftime('%H:%M:%S')}")
    print(f"  Moved:   {len(moved)} file(s)")
    if skipped:
        print(f"  Skipped: {len(skipped)} file(s)")
    if errors:
        print(f"  Errors:  {len(errors)} file(s)")
    print("─" * 55 + "\n")


# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    ext_map = build_extension_map(FILE_CATEGORIES)

    # ── STEP 1: Preview (dry run) ──────────────
    # Run with dry_run=True first to see what will happen
    # without actually moving anything.
    organize(DOWNLOADS, ext_map, dry_run=True)

    # ── STEP 2: Confirm and run ────────────────
    answer = input("Proceed and move files? (y/n): ").strip().lower()
    if answer == "y":
        organize(DOWNLOADS, ext_map, dry_run=False)
        print("All done! Your Downloads folder is organized.")
    else:
        print("Cancelled. Nothing was moved.")
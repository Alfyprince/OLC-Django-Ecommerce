from pathlib import Path
from PIL import Image

folder = Path("static/img")

for path in folder.iterdir():
    if path.suffix.lower() not in [".jpg", ".jpeg"]:
        continue

    try:
        original_size = path.stat().st_size

        with Image.open(path) as img:
            # Convert to RGB for JPEG
            if img.mode != "RGB":
                img = img.convert("RGB")

            # Resize very large images
            max_width = 1600
            max_height = 1600
            img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

            # Save compressed JPEG
            img.save(
                path,
                "JPEG",
                quality=80,
                optimize=True,
                progressive=True
            )

        new_size = path.stat().st_size

        print(
            f"{path.name}: "
            f"{original_size / 1024 / 1024:.2f} MB -> "
            f"{new_size / 1024 / 1024:.2f} MB"
        )

    except Exception as e:
        print(f"ERROR: {path.name}: {e}")
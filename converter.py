import os
from PIL import Image

input_folder = "images"
output_folder = "stickers"
os.makedirs(output_folder, exist_ok=True)

target_size = (512, 512)


jpg_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".jpg")]
jpg_files.sort()

if not jpg_files:
    print("❌ No .jpg files found in 'sticer/' folder.")
    exit()

for idx, filename in enumerate(jpg_files, start=1):
    input_path = os.path.join(input_folder, filename)
    try:
        img = Image.open(input_path).convert("RGBA")
        img.thumbnail(target_size, Image.LANCZOS)

        canvas = Image.new("RGBA", target_size, (255, 255, 255, 0))
        x = (512 - img.width) // 2
        y = (512 - img.height) // 2
        canvas.paste(img, (x, y))

        output_path = os.path.join(output_folder, f"{idx}.webp")
        canvas.save(output_path, "WEBP", quality=100, method=6)

        print(f"✅ Converted: {filename} -> {output_path}")
    except Exception as e:
        print(f"❌ Failed to convert {filename}: {e}")
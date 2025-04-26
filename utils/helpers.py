from datetime import datetime
import os
import requests

save_dir = "story_images"
os.makedirs(save_dir, exist_ok=True)

session_data = {
    "story_id": f"storybook_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
    "scenes": []
}

def build_prompt(story_line, character_desc=None, previous_image_url=None):
    if character_desc:
        story_line += f", {character_desc}"
    story_line += ", storybook illustration, pastel color, soft, child-friendly"
    if previous_image_url:
        story_line += f", keep visual consistent with this reference: {previous_image_url}"
    return story_line

def download_image_to_drive(image_url, image_index):
    image_path = f"{save_dir}/{session_data['story_id']}_scene_{image_index + 1}.png"
    response = requests.get(image_url)
    with open(image_path, "wb") as f:
        f.write(response.content)
    print(f"🖼️ Saved: {image_path}")

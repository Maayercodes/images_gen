from utils.helpers import build_prompt, download_image_to_drive, session_data
from services.openai_service import generate_image

def add_scene(prompt, character_desc=None, previous_image_url=None):
    final_prompt = build_prompt(prompt, character_desc, previous_image_url)
    image_url = generate_image(final_prompt)

    session_data["scenes"].append({
        "prompt": prompt,
        "character_desc": character_desc,
        "final_prompt": final_prompt,
        "image_url": image_url
    })

    download_image_to_drive(image_url, len(session_data["scenes"]) - 1)
    print("✅ Image Generated:", image_url)
    return image_url

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(scene_prompt, character_description=None, ref_img_num=None):
    # Build the final prompt by incorporating scene_prompt, character_description, and ref_img_num
    prompt = scene_prompt
    
    if character_description:
        prompt += f" with character: {character_description}"
    
    if ref_img_num is not None:
        prompt += f" based on reference image number {ref_img_num}"
    
    # Call the OpenAI API
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    
    return response.data[0].url


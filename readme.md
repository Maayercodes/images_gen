Project: Image Generation API
This project provides an API that allows you to generate consistent images for characters using OpenAI’s image generation model. You can send a prompt to generate an image of a character for a children’s story or any other use case.

API Usage
Run the API Locally

 navigate to the project folder.

Ensure you have Python installed (version 3.7 or higher).

Install the dependencies by running the following command:


pip install -r requirements.txt

Start the FastAPI Server

Start the server by running:

uvicorn api_server:app --reload
The FastAPI server will start running on http://127.0.0.1:8000.

API Endpoints
POST /generate-image

This endpoint generates an image based on the prompt you provide.

Request Body (JSON):



{
  "prompt": "Your character description goes here"
}
Response:

The API will return a URL of the generated image. Example:


{
  "image_url": "https://example.com/path-to-generated-image"
}
Example cURL Request:


Edit
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-image' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "A smiling cartoon cat with a blue scarf and glasses, sitting on a sunny beach"
}'
Prompt Guidelines
To ensure consistent image generation for your characters across different scenes, follow these guidelines:

Character Descriptions: When generating images for a specific character, always provide a detailed character description. The more specific you are, the more consistent the images will be. For example:

Character Description: "A young girl with short red hair, wearing a purple dress and white shoes, holding a teddy bear."

Make sure the prompt matches the character you want to generate.

Reference Images: If you need the character to look exactly the same across different scenes, you must provide a reference image. This image helps the model maintain visual consistency between multiple generations.you should select reference images by just selecting the counter in which images are being saved you select the value from 0 

Start with a reference image that accurately depicts the character’s appearance.

Each time you request a new image, use that reference image in the prompt to maintain consistency.

Example: "Generate a new scene with the same character (reference image) but now she is holding an umbrella and standing in the rain."

Scene Changes: You can change the scene and background without affecting the consistency of the character, but keep the character description consistent.

Example:

"Character standing in a field of flowers, holding a basket."

"Same character, but now she’s standing next to a tree with a bird on her shoulder."

Important Notes
Visual Consistency: The consistency of the character images depends on:

Keeping the character description consistent for each request.

Using the same reference image when you want to keep the appearance of the character consistent.

API Key: The OpenAI API key is pre-configured in the project. You just need to add your key in the .env file as described above.

Image Size: The API generates images with a resolution of 1024x1024 pixels. If you need a different size, you can modify the image generation code in services/openai_service.py.

How to Test the API
Start the FastAPI server by running the following command:


uvicorn api_server:app --reload
Open Postman or your preferred API testing tool.

Make a POST request to the following URL:


http://127.0.0.1:8000/generate-image
In the Body of the request, select raw and set the type to JSON. Then, provide a JSON body like this:

{
  "prompt": "A cartoon character of a boy with brown hair, wearing a red cap and blue shirt."
}
Send the request and check the response. You will get a URL for the generated image.

Additional Information
Error Handling: If something goes wrong (like an invalid prompt or API key), you’ll get an error message that can help you troubleshoot the issue.

API Customization: You can modify the openai_service.py file if you want to change the image model, size, or quality.

Dependencies: This project requires Python 3.7+ and the following libraries:

fastapi

pydantic

openai

python-dotenv

uvicorn

You can install the dependencies by running:


pip install -r requirements.txt

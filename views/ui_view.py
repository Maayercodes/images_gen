import gradio as gr
from controllers.image_controller import add_scene  # Corrected import

def predict(scene_prompt, character_description, ref_img_num):
    # Call the correct function with a single argument (e.g., dictionary)
    return add_scene(scene_prompt, character_description, ref_img_num)  # Send all data as a single call

def launch_ui():
    gr.Interface(
        fn=predict,
        inputs=[
            gr.Textbox(label="Scene Prompt"),
            gr.Textbox(label="Character Description (optional)"),
            gr.Number(label="Reference Image Number", value=-1)
        ],
        outputs="image"
    ).launch()

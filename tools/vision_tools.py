from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os
from langchain_openai import OpenAI
from langchain.tools import tool
class BlipImageCaptioner():
 @tool("caption_image")
 def caption_image(image_path: str) -> str:
    """Generates a caption for the given image using BLIP."""
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)
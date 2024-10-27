import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/Falconsai/nsfw_image_detection"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def query(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except FileNotFoundError:
        print("Image file not found.")
        return None

def detect_nsfw(image_path):
    result = query(image_path)
    if result:
        highest_score = max(result, key=lambda x: x['score'])
        if highest_score['label'].lower() == "nsfw":
            return True, highest_score['score']
        else:
            return False, highest_score['score']
    return None, None

# Example usage:
if __name__ == "__main__":
    is_nsfw, confidence = detect_nsfw("nsfwtest.jpg")
    if is_nsfw is not None:
        print(f"Is the image NSFW? {'Yes' if is_nsfw else 'No'}")
        print(f"Confidence: {confidence:.2%}")
    else:
        print("Unable to determine")
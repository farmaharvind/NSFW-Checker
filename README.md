# NSFW Image Detection Script

This project provides a Python script for detecting NSFW (Not Safe For Work) images using the Hugging Face Inference API. The `nsfw_image_detection.py` script allows users to classify images as "NSFW" or "SFW" (Safe For Work) by uploading them to a pre-trained model hosted on Hugging Face.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

- Python 3.7+
- API Access to Hugging Face: Requires a Hugging Face account and an API key.
- Python Packages:
  - `requests` - For making HTTP requests.
  - `python-dotenv` - For loading environment variables from a `.env` file.
- [Machine Learning Model](https://huggingface.co/Falconsai/nsfw_image_detection)

You can install required packages with the following command:


pip install requests python-dotenv

## Setup

1. Clone the Repository or download the `nsfw_image_detection.py` file to your local environment.

2. Create a `.env` file in the same directory as the script and add your Hugging Face API key:

HUGGINGFACE_API_KEY=your_huggingface_api_key

eplace `your_huggingface_api_key` with the actual API key from your Hugging Face account. This key provides access to the API for image detection.

3. Set Up a Test Image: Place a sample image in the same directory or specify the full path to an image file to test the script.

## Usage

To run the `nsfw_image_detection.py` script and check if an image is NSFW, use the following command:

python nsfw_image_detection.py

In the script, specify the path to an image file for testing:

# Update the image path
test_image_path = "path/to/your/image.jpg"  # Replace with the actual image path

## Troubleshooting

### 400 Client Error
If you encounter a 400 error, check the following:
- Verify the API URL and ensure the model is publicly accessible.
- Ensure that the image path is correct and that the image file exists.
- Confirm that the API key in `.env` is correct and has the required permissions.

### Environment Variable Issues
If the API key is not being recognized, ensure you have:
- Installed `python-dotenv`
- Placed the `.env` file in the same directory as `nsfw_image_detection.py`
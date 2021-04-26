import os
from google.cloud import vision
import io
#INPUT your google API KEY json file here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cloud_api_key.json"

#define the text detection API call, taking in the path of the image:
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    snapshot_dir = "snapshots"
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print('Texts from local image:')

    for text in texts:
        #write the detected text to an output file
        with open("Output.txt", "a") as text_file:
            text_file.write('\n"{}"'.format(text.description))
        #print the detected text to the cmd
        print('\n"{}"'.format(text.description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#detect_text('snapshots/Q2GV-9GBH-4PC3.jpg')
#detect_text('snapshots/test3.jfif')

def detect_labels(path):
    """Detects labels in the file."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#detect_labels("snapshots/Q2GV-9GBH-4PC3.jpg")

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts detected from image url:')

    for text in texts:
        #write the detected text to an output file
        with open("Output.txt", "a") as text_file:
            text_file.write('\n"{}"'.format(text.description))
        #print detected texts to console
        print('\n"{}"'.format(text.description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

#detect_text_uri("https://spn18.meraki.com/stream/jpeg/snapshot/03a2c0785a5f5f1bVHYjFmODVjOTc5MjQ5OGZiZGU0NzEwMWE1YzcxNzlkNmU2MGQ5NjNkM2NiYjYyOWE3NjkzY2Y3Yjc1Y2Q4OGM4NR6u6R_NhXNmKGu8epjTfT7rOM0Ymjr-DH8JZAulwK-0LwqefsUhHvUSUSCgCY3SiyWuy_iYYpwG6VQsylwgp7ufGcsd7tpjsnvt5gts-uV8oBGB1e1t9RDe96WOQqdwniMduoywLnprtfdBQYZ8ixsBTGx0SAo86f9632bMvXtr9NwH3pXONMMEbR7r8t4v_s8VxZMZ3zl6J3JKg8z5jLg")

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

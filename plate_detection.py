import os

#INPUT your google API KEY json file here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cloud_api_key.json"

#define the text detection API call, taking in the path of the image:
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    snapshot_dir = "snapshots"
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print('Texts:')

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

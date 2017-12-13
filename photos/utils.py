import base64
import requests

from django.conf import settings


URL = 'https://vision.googleapis.com/v1/images:annotate?key={api_key}'

PARAMS = {
    'requests': [
        {
            'image': {
                'content': ''  # Fill in with image file in base64-encoded
                               # string format.
            },
            'features': [
                {
                    'type': 'LABEL_DETECTION',
                    'maxResults': settings.LABEL_DETECTION_MAX_RESULTS
                }
            ]
        }
    ]
}


def get_visual_report(image):
    """Get visual report from google vision api."""
    url = URL.format(api_key=settings.GOOGLE_CLOUD_API_KEY)
    image_content = base64.b64encode(image.read()).decode('utf-8')
    PARAMS['requests'][0]['image']['content'] = image_content
    response = requests.post(url, json=PARAMS)
    data = response.json()
    return data

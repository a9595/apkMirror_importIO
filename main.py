from urllib import request
import json


req = request.urlopen(
    'https://api.import.io/store/data/bc241b98-a160-4332-b0a9-71f1160d8830/'
    '_query?input/webpage/url=http%3A%2F%2Fwww.apkmirror.com%2Fapk%2Fgoogle-inc%2Fgoogle-play-store%2F&_user=ac4a2596-0302-46ee-a01a-153a5b50f8bf&_'
    'apikey=ac4a2596-0302-46ee-a01a-153a5b50f8bf%3AjYP8%2Fr6yBVXhyXi%2Fi6o0zIeDtIqpZIyYI2InqjnjjHFqMoA0ZTV3jzkAX1TQoA60XN9Dh6tJ5a94PZWvpgtcNw%3D%3D'
)
encoding = req.headers.get_content_charset()
json_result = json.loads(req.read().decode(encoding))
#translated_word = json_result['tuc'][0]['meanings'][0]['text']
stupid_ver = json_result['results'][0]['version_stupid']
print(stupid_ver)




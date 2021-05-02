import requests

url = http://localhost:8080/static_simple.html
file_name = "image.jpeg"

response = requests.get(url)

if response_data.status_code != 200:
    err = Exception("Failed to get image. Status Code: " + str(response_data.status_code) + "\n" + url)

image = response.content

content_type = response_date.headers["content-type"]
    if "image" not in content_type:
        err = Exception("Failed to get an image. No images in HTML: " + str(content_type))
        raise err

with open(file_name, "wb") as aaa:
    aaa.write(image)

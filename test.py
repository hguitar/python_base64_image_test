import os
import base64


if __name__ == "__main__":
    with open("/Users/mason/Desktop/base64_test/default.png","rb") as f:
        file = open('base64.txt','wt',encoding='utf-8')
        base64_data = base64.urlsafe_b64encode(f.read())
        file.write(str(base64_data, encoding='utf-8'))
        file.close()

    with open("/Users/mason/Desktop/base64_test/base64.txt", "r") as f:
        imagedata = base64.urlsafe_b64decode(f.read())
        file = open('1.png', 'wb')
        file.write(imagedata)
        file.close()
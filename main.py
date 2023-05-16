import os
import openai
# openai.organization = "org-7SE96eHstGb7Y6DhXLKwZVRH"
openai.api_key = "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"

if __name__ == '__main__':
    x = openai.Model.list()
    y = openai.Model.retrieve("text-davinci-003")
    response = openai.Image.create(
        prompt="a white siamese cat",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

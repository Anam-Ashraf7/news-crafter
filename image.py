import openai
import requests
import os

# folder_path = "test"

# # List all files in the folder
# file_list = os.listdir(folder_path)

# # Iterate through the files and delete them
# for file_name in file_list:
#     file_path = os.path.join(folder_path, file_name)
#     try:
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#     except Exception as e:
#         print(f"Error deleting {file_path}: {e}")

# Set your OpenAI API key
openai.api_key = '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'

# Set the prompt for DALL-E
prompt1 = "Spider man vs bat man"


def create_image(prompt):
    # Specify the constant image size
    image_size = "512x512"  # Change this to your desired size

    # Generate image using DALL-E
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=image_size
    )

    # Extract the generated image URL from the response
    image_url = response["data"][0]["url"]

    # Print the image URL
    return image_url

prompt2 = "Give me 5 keywords only to generate image for the topic 'Fashion fans rushing to buy 'perfect for work' £30 Amazon handbag that looks just like £1,200 designer Burberry version'"

def get_response(prompt):
    prompt1 = f"Give me 5 keywords only to generate image for the topic '{prompt}'"

    conversation = [
        {
            "role": "user",
            "content": prompt1
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation,
        temperature=0.7
    )

    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']

# text_res = get_response(prompt2).split("\n")
# images = []

# for i in text_res:
#     res = create_image(i)
#     images.append(res)


# for i in range(len(images)):
#     url = images[i]
#     response = requests.get(url)

#     with open(f"image_{i}.jpg", "wb") as f:
#         f.write(response.content)
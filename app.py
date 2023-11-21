# import asyncio
from flask import Flask, jsonify, request
from deep_translator import GoogleTranslator
from flask_cors import CORS
import asyncio
from gtts import gTTS
import requests
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
from image import get_response,create_image

app = Flask(__name__)
CORS(app)

async def translate_text(to_translate, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    translated = translator.translate(to_translate)
    return translated

async def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language, tld="com", slow=False)
    tts.save("audio.mp3")
    return

async def create_video(images, audio_file, output_file, fps=1):
    clips = [ImageSequenceClip([image], fps=fps) for image in images]
    video_clip = concatenate_videoclips(clips, method="compose")
    audio_clip = AudioFileClip(audio_file)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')




@app.route('/translate_text', methods=['POST', 'GET'])
async def translate_text_handler():
    print("Keyword generating")
    # call_count = 0
    # max_count = 1
    try:
        data = request.get_json()
        to_translate = data.get('to_translate')
        target_language = data.get('target_language') or 'en'  # Default to English if not provided

        print(to_translate,target_language)

        result = await translate_text(to_translate, target_language)
        print(result)

        # if call_count<max_count:
        text_to_speech(result, target_language)
        await asyncio.sleep(0)
            # call_count+=1

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# @app.route('/text_to_speech', methods=['POST', 'GET'])
# async def text_to_speech_handler():
#     try:
#         data = request.get_json()
#         text = data.get('text')
#         language = data.get('language') or 'en'  # Default to English if not provided

#         print(text, language)

#         # Call the text_to_speech function here
#         await text_to_speech(text, language)
#         await asyncio.sleep(0)

#         return jsonify({'result': "Done"})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@app.route('/generate_image', methods=['POST', 'GET'])
async def generate_image():
    print("Image generating")
    try:
        data = request.get_json()
        prompt = data.get('prompt')

        res = get_response(prompt)
        res = res.split("\n")

        images = []

        for i in range(len(res)):
            image = create_image(res[i])
            print(image)
            images.append(image)

        for i in range(len(images)):
            url = images[i]
            response = requests.get(url)

            with open(f"image_{i}.jpg", "wb") as f:
                f.write(response.content)

        return jsonify({'result': res})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/generate_video', methods=['POST', 'GET'])
async def generate_video():
    print("Video generating")
    try:
        data = request.get_json()
        images_list = data.get('images')
        audio_file = data.get('audio')
        output_file = 'output_video.mp4'

        print("started")

        await create_video(images_list, audio_file, output_file, fps=0.45)

        print("done")

        return jsonify({"result": "done"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
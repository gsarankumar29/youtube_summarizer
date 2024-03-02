# # from flask import Flask, request,jsonify
# # from youtube_transcript_api import YouTubeTranscriptApi
# # from transformers import pipeline

# # app = Flask(__name__)

# # # openai.app_key = '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'
# # @app.get('/summary')
# # @app.route('/summarize', methods=['POST'])

# # def summary_api():
    
# #     url = request.args.get('url', '')
# #     video_id = url.split('=')[1]
# #     summary = get_summary(get_transcript(video_id))
# #     return summary, 200

# # def get_transcript(video_id):
# #     transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
# #     transcript = ' '.join([d['text'] for d in transcript_list])
# #     return transcript

# # def get_summary(transcript):
# #     summariser = pipeline('summarization')
# #     summary = ''
# #     for i in range(0, (len(transcript)//1000)+1):
# #         summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
# #         summary = summary + summary_text + ' '
# #     return summary
    

# # if __name__ == '__main__':
# #     app.run()














# from flask import Flask, request, jsonify
# from flask_cors import CORS

# import openai
# from youtube_transcript_api import YouTubeTranscriptApi
# from transformers import pipeline
# # from openai import OpenAI

# app = Flask(__name__)
# CORS(app)

# openai.api_key = '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'

# @app.route('/summarize', methods=['POST'])
# def summarize():
#     # Get the video URL from the request
#     url = request.json.get('url', '')
#     video_id = url.split('=')[1]

#     # Get video transcript
#     transcript = get_transcript(video_id)

#     # Summarize the transcript using OpenAI
#     summary = get_summary(transcript)

#     return jsonify({'summary': summary}), 200

# def get_transcript(video_id):
#     transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
#     transcript = ' '.join([d['text'] for d in transcript_list])
#     return transcript

# def get_summary(transcript):
#     summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
#     summary_text = summarizer(transcript, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
#     return summary_text

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)







# from flask import Flask, request, jsonify
# # from flask_cors import CORS
# import openai
# from youtube_transcript_api import YouTubeTranscriptApi
# from transformers import pipeline

# app = Flask(__name__)
# # CORS(app)

# openai.api_key = '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'

# @app.route('/summarize', methods=['POST'])
# def summarize():
#     # Get the video URL from the request
#     url = request.json.get('url', '')
#     video_id = url.split('=')[1]

#     # Get video transcript
#     transcript = get_transcript(video_id)

#     # Summarize the transcript using OpenAI
#     summary = get_summary(transcript)

#     return jsonify({'summary': summary}), 200

# def get_transcript(video_id):
#     try:
#         transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
#         transcript = ' '.join([d['text'] for d in transcript_list])
#         return transcript
#     except Exception as e:
#         return str(e), 400  # Return error response if unable to get transcript

# def get_summary(transcript):
#     try:
#         summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
#         summary_text = summarizer(transcript, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
#         return summary_text
#     except Exception as e:
#         return str(e), 500  # Return error response if summarization fails

# if __name__ == '__main__':
#     app.run(debug=True)

 
# from flask import Flask, request, jsonify
# import openai
# from youtube_transcript_api import YouTubeTranscriptApi

# app = Flask(__name__)

# openai.api_key = 'your_openai_api_key_here'

# @app.route('/summarize', methods=['POST'])
# def summarize():
#     data = request.json
#     url = data.get('url', '')
#     video_id = extract_video_id(url)
#     if video_id:
#         transcript = get_transcript(video_id)
#         if transcript:
#             summary = get_summary(transcript)
#             if summary:
#                 return jsonify({'summary': summary}), 200
#             else:
#                 return jsonify({'error': 'Failed to summarize transcript.'}), 500
#         else:
#             return jsonify({'error': 'Failed to get transcript for the video.'}), 400
#     else:
#         return jsonify({'error': 'Invalid YouTube URL.'}), 400

# def extract_video_id(url):
#     # Extract video ID from YouTube URL
#     if 'youtube.com/watch?v=' in url:
#         return url.split('youtube.com/watch?v=')[1].split('&')[0]
#     elif 'youtu.be/' in url:
#         return url.split('youtu.be/')[1].split('?')[0]
#     else:
#         return None

# def get_transcript(video_id):
#     try:
#         transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
#         transcript = ' '.join([d['text'] for d in transcript_list])
#         return transcript
#     except Exception as e:
#         print(f'Error fetching transcript: {e}')
#         return None

# def get_summary(transcript):
#     try:
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=transcript,
#             temperature=0.3,
#             max_tokens=150,
#             top_p=1.0,
#             frequency_penalty=0.0,
#             presence_penalty=0.0,
#             stop=['\n']
#         )
#         summary_text = response.choices[0].text.strip()
#         return summary_text
#     except Exception as e:
#         print(f'Error summarizing transcript: {e}')
#         return None

# if __name__ == '__main__':
#     app.run(debug=True)




# 

import traceback
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def homeredirect():
    print('gfsgd')


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        try:
            data = request.json
            url = data.get('url', '')
            print(url)
            video_id = extract_video_id(url)
            if video_id:
                transcript = get_transcript(video_id)
                if transcript:
                    summary = get_summary(transcript)
                    if summary:
                        return jsonify({'summary': summary}), 200
                    else:
                        return jsonify({'error': 'Failed to summarize transcript.'}), 500
                else:
                    return jsonify({'error': 'Failed to get transcript for the video.'}), 400
            else:
                return jsonify({'error': 'Invalid YouTube URL.'}), 400
        except Exception as e:
            print(f'Error in summarize endpoint: {e}')
            traceback.print_exc()
            return jsonify({'error': 'Internal server error.'}), 500
    else:
        return jsonify({'error': 'Method not allowed. Use POST method with JSON data containing "url" parameter.'}), 405

def extract_video_id(url):
    # Extract video ID from YouTube URL
    if 'youtube.com/watch?v=' in url:
        return url.split('youtube.com/watch?v=')[1].split('&')[0]
    elif 'youtube/' in url:
        return url.split('youtube/')[1].split('?')[0]
    else:
        return None

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        # Iterate over available transcripts
        for transcript in transcript_list:
            # Check if transcript language is English (India) or Hindi
            if transcript.language_code == 'en' or transcript.language_code == 'hi':
                # Fetch the transcript and return
                transcript_text = transcript.fetch()
                return transcript_text
        # If no suitable transcript found, return None
        print("No transcripts available in English (India) or Hindi.")
        return None
    except Exception as e:
        print(f'Error fetching transcript: {e}')
        traceback.print_exc()
        return None

def get_summary(transcript):
    # Your existing implementation of summarization function
    pass

if __name__ == '__main__':
    app.run(debug=True)

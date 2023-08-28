import os

import openai
from blinker import Signal
from dotenv import load_dotenv
from flask import render_template, Flask, request, Response, stream_with_context

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

streaming_state = {'value': True}
streaming_stopped = Signal()


def stop_streaming_handler(sender):
    streaming_state['value'] = False


streaming_stopped.connect(stop_streaming_handler)


@app.route('/', methods=['GET', 'POST'])
@stream_with_context
def landing():
    if request.method == 'GET':
        return render_template('chat.html')

    streaming_state['value'] = True
    data = request.form or request.json
    prompt = data.get('prompt')

    if not prompt:
        return Response('Prompt is required', status=400)

    def stream_response():
        response = openai.ChatCompletion.create(messages=[{"role": "user", "content": f'{prompt}'}, ], temperature=0,
                                                model='gpt-3.5-turbo',
                                                stream=True)
        for chunk in response:
            if not streaming_state['value']:
                print("Streaming Stopped")
                break

            yield chunk['choices'][0]['delta']['content'] if 'content' in chunk['choices'][0]['delta'] else ""

    return Response(stream_response(), mimetype='text/html')


@app.route('/stop', methods=['GET'])
def stop_streaming():
    streaming_stopped.send()
    return "Streaming stop signal sent"


if __name__ == '__main__':
    app.run(debug=True)

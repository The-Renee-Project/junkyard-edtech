"""
This is a simple HTTP server that serves as an endpoint for a bert qa model.
----------------------------------------------------------------------------
Example:
$ curl -d '{"context": "Salad. This is a vegan meal", "question": "is this meal vegan?"}' -X POST localhost:8501
{"answer_0": {"text": "vegan"}, "answer_1": {"text": "This is a vegan"}, ...}
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from tflite_support.task import text


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    HTTP Server that serves tflite model of bert
    """
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        answerer = text.BertQuestionAnswerer.create_from_file("model.tflite")
        length = int(self.headers['content-length'])
        message = json.loads(self.rfile.read(length))

        # Get the form values
        context = message['context']
        question = message['question']
        bert_qa_result = answerer.answer(context, question)
        output = {}
        for index in range(0, len(bert_qa_result.answers)):
            output[f'{index}'] = {}
            output[f'{index}']['text'] = bert_qa_result.answers[index].text

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(json.dumps(output).encode())


httpd = HTTPServer(('', 8501), SimpleHTTPRequestHandler)
httpd.serve_forever()

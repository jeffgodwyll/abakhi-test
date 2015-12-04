"""
    Simple Rest API to evaluate code and return result
"""


from code import compile_command

from flask import Flask, request, jsonify, abort


app = Flask(__name__)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'bad request'}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'not found'}), 404


@app.route('/eval', methods=['POST'])
def exec_code():
    """Supply a json request body with 'code' in it.

    The 'code' value must be a simple python expression

    Example:
        $ curl -i -H "Content-type: application/json" \
        -X POST http://localhost:5000/exec -d '{"code": "abs(-100)"}'
    """
    if not request.json or 'code' not in request.json:
        abort(400)
    code = request.json['code']
    # TODO: put in try block, to catch syntax error, current syntax error allows
    # to create gist or put in paste bin
    result = compile_command(code, '<string>', 'eval')  # only python statemenst

    # TODO: raise SyntaxError, ValueError if code is a syntax error produced by
    # malformed literals

    """
    try:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        try:
            sys.stdout = mystdout = StringIO()
            print eval(result)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
    except:
        pass  # TODO: traceback

    print "out: ", mystdout.getvalue()
    """

    return jsonify({'result': eval(result)})
    # return request.values


if __name__ == '__main__':
    app.run(debug=True)

Quick start
-----------

`curl -i -H "Content-Type: application/json" -X POST -d '{"code": "abs(-100)"}' http://localhost:5000/eval`

Results in:

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 19
    Server: Werkzeug/0.11.2 Python/2.7.6
    Date: Fri, 04 Dec 2015 01:25:44 GMT

    {
      "result": 100
    }


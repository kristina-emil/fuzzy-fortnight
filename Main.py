from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()


@app.get("/",response_class=HTMLResponse)
def read_root():
    return """
    <html>
    <head>
        <title>Привет</title>
        <style>
            body {
                background-color: DeepPink;
                color: yellow;
                font-family: Arial, sans-serif;
            }
            h1 {
                text-align: center;
                font-size: 36px;
            }
            img {
                display: block;
                margin: 0 auto 20px;
            }
        </style>
    </head>
    <body>
        <h1 style="text-align:center; font-size:99px;">Привет</h1>
        <img src="/static/hello.jpg" alt="Hello Image" style="display:block; margin:auto;width:200px;">
    </body>
    </html>
    """

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

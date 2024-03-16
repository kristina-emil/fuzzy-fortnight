from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.get("/",response_class=HTMLResponse)
def read_root():
    with open("index.html", "r") as file:
        return file.read()
    
@app.get("/image")
async def get_image():
    return FileResponse("hello.jpg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

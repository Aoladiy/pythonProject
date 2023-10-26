from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
import json
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    html_content = "<h2>Hello, Lev!</h2>"
    return HTMLResponse(content=html_content)


# class DataItem(BaseModel):
#     message: str


@app.post("/save_data")
async def save_data(request: Request):
    data = await request.body()
    try:
        decoded_data = json.loads(data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Ошибка при парсинге JSON-данных")

    try:
        with open("data.json", "w") as file:
            json.dump(decoded_data, file)
    except IOError:
        raise HTTPException(status_code=500, detail="Ошибка при открытии файла")

    return {"message": "Данные успешно сохранены в data.json"}


@app.get("/read_json")
async def read_json():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
            return HTMLResponse(content=pretty_json)
    except FileNotFoundError:
        return "Файл с данными не найден."
    except json.JSONDecodeError:
        return "Ошибка при чтении JSON-файла."

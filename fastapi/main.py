import json

import mysql.connector
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins, change the `allow_origins` parameter to your frontend URL if needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
db_config = {
    "host": "localhost",
    "port": 3307,
    "user": "root",
    "password": "Root-123",
    "database": "web_programming_db"
}


def save_to_database(data):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        query = "INSERT INTO saved_data (name, email, `group`) VALUES (%s, %s, %s)"
        cursor.executemany(query, [(data['name'], data['email'], data['group'])])
        connection.commit()
    except mysql.connector.Error as err:
        print(err)
        raise HTTPException(status_code=500, detail=f"Database Error: {err}")
    finally:
        cursor.close()
        connection.close()


@app.post("/save_data")
async def save_data(request: Request):
    data = await request.body()
    try:
        decoded_data = json.loads(data)
        save_to_database(decoded_data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error parsing JSON data")


@app.get("/get_data")
async def get_data():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT id, name, email, `group` FROM saved_data")
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database Error: {err}")
    finally:
        cursor.close()
        connection.close()


@app.put("/edit_data/{item_id}")
async def edit_data(item_id: int, request: Request):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    data = await request.json()
    new_name = data.get("name")
    new_email = data.get("email")
    new_group = data.get("group")

    try:
        query = "UPDATE saved_data SET name = %s, email = %s, `group` = %s WHERE id = %s"
        cursor.execute(query, (new_name, new_email, new_group, item_id))
        connection.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database Error: {err}")
    finally:
        cursor.close()
        connection.close()


@app.delete("/delete_data/{item_id}")
async def delete_data(item_id: int):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        query = "DELETE FROM saved_data WHERE id = %s"
        cursor.execute(query, (item_id,))
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item not found")
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database Error: {err}")
    finally:
        cursor.close()
        connection.close()

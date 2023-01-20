from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

with open('index.html', 'r') as file:
	html = file.read()


@app.get("/")
async def get():
	return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	number = 1
	while True:
		data = await websocket.receive_text()
		await websocket.send_json({"message": f'{number}. {data}'})
		number += 1

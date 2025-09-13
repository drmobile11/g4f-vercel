from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import g4f

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server running with G4F CLI"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    if not prompt:
        return JSONResponse(status_code=400, content={"error": "Prompt required"})

    try:
        # Using g4f as the CLI does
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"response": response}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

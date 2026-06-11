from fastapi import FastAPI
from agent import AbsolAgent

app = FastAPI()

agent = AbsolAgent()


@app.get("/")
def root():

    return {
        "service": "Absol AI",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/investigate")
def investigate():

    incidents = agent.run()

    return {
        "total_incidents": len(incidents),
        "incidents": incidents
    }
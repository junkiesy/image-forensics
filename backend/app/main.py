from fastapi import FastAPI

app = FastAPI(
    title="AI Image Forensics Lab API",
    description="Backend API for local AI image forensic analysis.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
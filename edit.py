@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API berjalan normal"}

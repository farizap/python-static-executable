import uvicorn
# from  import Process, freeze_support


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=False)
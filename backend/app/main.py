import os
from fastapi import FastAPI, File, UploadFile
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

from utils.helper import upload_to_sql, build_json
from database.database import Base, engine, Session

load_dotenv()
session = Session()
Base.metadata.create_all(engine) # create tables if they haven't been initialized yet

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("***** App started *****")

    yield
    print("***** App stopped *****")



#Initializes App
app = FastAPI(
    title="Backend API",
    version="0.0.1",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    # lifespan=lifespan
)

origins = os.getenv('allowed_cors')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        # Read the file directly into memory
        file_content = await file.read()

        upload_to_sql(session, file_content)

        # Example: just returning a success message for now
        return JSONResponse(content={"message": "File processed successfully!"}, status_code=200)

    except Exception as e:
        # Handle any errors that occur during file upload or deserialization
        return JSONResponse(content={"message": f"An error occurred: {str(e)}"}, status_code=500)
    

@app.get("/download_json")
def get_tree():
    json = build_json(session)
    return json
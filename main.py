from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import anthropic
from typing import Optional,Literal
from vector_store import search_similar

ValidAttribute = Literal["slim_fit", "oversized", "cropped", "high_waist", "notch_lapel"]

class FashionRequest(BaseModel):
    style: str
    color:str
    garment_type: str
    attributes: list[ValidAttribute]
    gender: Optional[str]=None
    season: Optional[str]=None

app=FastAPI()   #creating an instance of FastAPI class
#in-memory job store
jobs={}

@app.get("/")
def home():
    return {"message":"Fashion AI is alive!"}
#defines a route for the home page, which returns a JSON response with a message when accessed

@app.post("/generate",status_code=202)
async def generate_fashion(request:FashionRequest):
    style=request.style
    color=request.color
    garment=request.garment_type
    job_id= str(uuid.uuid4())
    jobs[job_id]={"status":"processing","result": None}

#call AI to generate fashion description
#client=anthropic.Anthropic()
# message=client.messages.create(
# model="claude-sonnet-4-20250514",
#max_tokens=1000,
#messages=[
# {
#      "role": "user",
#       "content": f"Describe a {request.color} {request.garment_type} in {request.style} style. Be specific about design details, fabric, and styling in 3 sentences."
#    }
# ]
#  )

       # temporary mock
    season_text = f"for {request.season}" if request.season else ""
    gender_text= f"designed for {request.gender}" if request.gender else ""
    attributes_text = ", with attributes: " + ", ".join(request.attributes) 
    ai_result = f"A sleek {request.color} {request.garment_type} {attributes_text} {gender_text} {season_text}..."
    jobs[job_id]["result"]= ai_result
    jobs[job_id]["status"] = "complete"


    return{
        "job_id": job_id,
        "message": f"Generating a {color} {garment} in {style} style!",
        "status": "complete",
        "result": ai_result
    }

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
        if job_id not in jobs:
            return {"error": "Job not found"}
        return jobs[job_id]

@app.get("/recommend")
def recommend(query: str):
    results = search_similar(query)
    return {"recommendations": results["metadatas"][0]}

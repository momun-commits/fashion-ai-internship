from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Literal
import uuid

from image_generator import generate_fashion_image

# ----------------------------
# Request Schema
# ----------------------------

ValidAttribute = Literal[
    "slim_fit",
    "oversized",
    "cropped",
    "high_waist",
    "notch_lapel"
]


class FashionRequest(BaseModel):
    style: str
    color: str
    garment_type: str
    attributes: list[ValidAttribute]
    gender: Optional[str] = None
    season: Optional[str] = None


# ----------------------------
# FastAPI App
# ----------------------------

app = FastAPI(
    title="Fashion AI Generator",
    description="Generate fashion images using FLUX and evaluate quality using CLIP",
    version="1.0.0"
)

# Temporary in-memory storage
jobs = {}


# ----------------------------
# Home Route
# ----------------------------

@app.get("/")
def home():
    return {
        "message": "Fashion AI is alive!",
        "status": "running"
    }


# ----------------------------
# Generate Fashion Image
# ----------------------------

@app.post("/generate", status_code=202)
async def generate_fashion(request: FashionRequest):

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "processing",
        "result": None
    }

    try:
        result = generate_fashion_image(
            {
                "style": request.style,
                "color": request.color,
                "garment_type": request.garment_type,
                "gender": request.gender,
                "season": request.season
            }
        )

        jobs[job_id]["status"] = "complete"
        jobs[job_id]["result"] = result

        return {
            "job_id": job_id,
            "status": "complete",
            "image_path": result["image_path"],
            "prompt": result["prompt"],
            "clip_score": result["clip_score"],
            "quality": result["quality"]
        }

    except Exception as e:

        jobs[job_id]["status"] = "failed"
        jobs[job_id]["result"] = str(e)

        raise HTTPException(
            status_code=500,
            detail=f"Image generation failed: {str(e)}"
        )


# ----------------------------
# Check Job Status
# ----------------------------

@app.get("/jobs/{job_id}")
def get_job(job_id: str):

    if job_id not in jobs:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return jobs[job_id]


# ----------------------------
# Run Locally
# ----------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import pickle
import pandas as pd
from pydantic import BaseModel,Field

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

with open("student_performance.pkl", "rb") as f:
    saved_data = pickle.load(f)
    model = saved_data["model"]
    encoders = saved_data["encoders"]
    scaler = saved_data["scaler"]

class StudentColumns(BaseModel):
    HoursStudied:int = Field(..., alias="Hours Studied")
    PreviousScores: int = Field(..., alias="Previous Scores")
    ExtracurricularActivities: str = Field(..., alias="Extracurricular Activities")
    SleepHours: int = Field(..., alias="Sleep Hours")
    SampleQuestionPapersPracticed: int = Field(..., alias="Sample Question Papers Practiced")

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})


@app.post("/predict")
async def predict(features: StudentColumns):
    try:
        data = features.model_dump(by_alias=True)

        extra_raw = str(data["Extracurricular Activities"]).strip()
        extra_encoded = 1.0 if extra_raw == "Yes" else 0.0

        input_list = [
            float(data["Hours Studied"]),
            float(data["Previous Scores"]),
            float(extra_encoded),
            float(data["Sleep Hours"]),
            float(data["Sample Question Papers Practiced"])
        ]
        columns = [
            "Hours Studied", "Previous Scores", "Extracurricular Activities",
            "Sleep Hours", "Sample Question Papers Practiced"
        ]
        final_df = pd.DataFrame([input_list], columns=columns)

        input_scaled = scaler.transform(final_df)
        prediction = model.predict(input_scaled)[0]

        final_score = min(float(prediction), 100.0)

        final_score = max(0.0, final_score)

        return {"predicted_score": round(final_score, 2)}

    except Exception as e:
        return {"error": f"Tahmin sırasında hata oluştu: {str(e)}"}





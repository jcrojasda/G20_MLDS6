from fastapi import FastAPI, Form, Depends
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from pydantic import BaseModel
import joblib

# Definir el modelo de entrada
class InputData(BaseModel):
    Time_spent_Alone: float
    Stage_fear: bool
    Social_event_attendance: float
    Going_outside: float
    Drained_after_socializing: bool

# Inicializar la app FastAPI
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar el modelo
model_path = "model/modelo.joblib"
model = joblib.load(model_path)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Renderiza el archivo index.html
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para hacer la predicción
@app.post("/predict")
def predict(data: InputData):
    # Realizar la predicción
    prediction = model.predict([[data.Time_spent_Alone, data.Stage_fear, data.Social_event_attendance,
                                  data.Going_outside, data.Drained_after_socializing]])[0]

    prediction = int(prediction)
    
    # Devolver la predicción
    return {"prediction": prediction}

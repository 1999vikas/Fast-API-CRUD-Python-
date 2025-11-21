from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.schemas import TakeResponse , TranslationRequest,TranslationStatus
app = FastAPI()

# laoding Temolates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})

#Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
# )

@app.post('/translate',response_class=TakeResponse)
def translate(request:TranslationRequest):

    #pseudo
    task=crud.create_translation_task(x,y,,p)
    background_tasks.add_task(perform_translation,task.id,request.text,request.languages,db)
    return {"task_id":{task.id}}


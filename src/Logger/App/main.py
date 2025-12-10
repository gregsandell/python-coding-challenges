from fastapi import FastAPI, Response, Query
from fastapi.responses import JSONResponse
import yaml
from Logger import Logger
from pydantic import BaseModel

class LogRequest(BaseModel):
    level: str
    message: str

app = FastAPI(title="Example API", version="0.1.0")
myLogger = Logger()

@app.get("/logs")
def logs():
     return myLogger.get_logs()
#
@app.post("/log")
def log(req: LogRequest):
    myLogger.log(message=req.message, level=req.level)

    return Response(status_code=204)

@app.get("/logs/search")
def search(keyword: str = Query(""), field: str = Query("message")):
    result = myLogger.search(keyword=keyword, field=field)
    return result

@app.get("/openapi.yaml")
def openapi_yaml():
    openapi_dict = app.openapi()
    yaml_text = yaml.safe_dump(openapi_dict, sort_keys=False)
    return Response(content=yaml_text, media_type="application/yaml")

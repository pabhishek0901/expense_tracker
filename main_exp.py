from fastapi import FastAPI
from exp_cal import router as exp_router

app = FastAPI()

app.include_router(exp_router)
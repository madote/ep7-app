from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI(
    title='FastAPIで作るTODOアプリ',
    description='FastAPIチュートリアル',
    version='0.58'
)


def index(request: Request):
    return {'Hello': 'World'}

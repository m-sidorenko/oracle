from fastapi import FastAPI, Response, Request
import logging

from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="LLM API",
    description="",
)
logging.basicConfig(filename="info.log", level=logging.DEBUG)


def log_info(req_body, res_body):
    logging.info(req_body)
    logging.info(res_body)


# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/health/")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

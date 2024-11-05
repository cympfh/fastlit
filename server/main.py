from fastapi import FastAPI


app = FastAPI()


@app.get("/api/greet")
def greet(name: str | None = None):
    if name:
        return {"Hello": name}
    return {"Hello": "World"}


@app.get("/api/randoms")
def randoms(n: int) -> list[float]:
    import random

    return [random.random() for _ in range(n)]

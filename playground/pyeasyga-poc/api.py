from typing import Optional
from service import ea
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root(q: Optional[str] = None):
    ea_instance = ea.HelloWorldEa(q)
    ea_instance.run()
    return ea_instance.result()

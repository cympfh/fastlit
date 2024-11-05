import os

import requests
import streamlit

from libs.fontawesome import FontAwesome


class API:
    """FastAPI Server"""

    def __init__(self):
        self.port = int(os.environ.get("FASTAPI_PORT", "8001"))
        self.url = f"http://127.0.0.1:{self.port}"

    def get(self, endpoint: str):
        return requests.get(f"{self.url}{endpoint}")


api = API()
fa = FontAwesome()

streamlit.title(":fire: Fastlit app")

name = streamlit.text_input("Your name")
res = api.get(f"/api/greet?name={name}")
streamlit.info(f"Hello, {res.json()['Hello']}")


if streamlit.button("plot"):
    xs = api.get("/api/randoms?n=100").json()
    for i in range(1, len(xs)):
        xs[i] += xs[i - 1] - 0.5
    streamlit.line_chart(xs, x_label="days", y_label="your credit")


streamlit.markdown(
    f"""
## References

- {fa.html("fa-solid fa-bolt-lightning")} [FastAPI](https://fastapi.tiangolo.com)
- {fa.html("fa-solid fa-crown")} [Streamlit](https://docs.streamlit.io)
- {fa.html("fa-solid fa-font-awesome")} [Font Awesome](https://fontawesome.com/icons)
""",
    unsafe_allow_html=True,
)

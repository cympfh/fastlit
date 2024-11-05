import streamlit


class FontAwesome:
    URL = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"

    def __new__(cls):
        if not hasattr(cls, "initialized"):
            csscode = f'<link rel="stylesheet" href="{cls.URL}" />'
            streamlit.write(csscode, unsafe_allow_html=True)
            cls.initialized = True
        return object.__new__(cls)

    def html(self, klass: str) -> str:
        return f'<i class="{klass}"></i>'

    def write(self, klass: str) -> None:
        streamlit.write(self.html(klass), unsafe_allow_html=True)

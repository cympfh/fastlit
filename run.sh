#!/bin/bash

source .env
if [ -z "$STREAMLIT_PORT" ] || [ -z "$FASTAPI_PORT" ]; then
	echo "Error: Set STREAMLIT_PORT and FASTAPI_PORT"
	exit 2
fi

export STREAMLIT_PORT
export FASTAPI_PORT

streamlit run view/main.py --server.baseUrlPath=view/ --server.port $STREAMLIT_PORT &\
fastapi run server/main.py --port $FASTAPI_PORT --reload &\
wait

import logging
import os
from app import create_app


app = create_app()
@app.route('/')
def homepage():
    return "it works"


if __name__ == "__main__":
    logging.info("Flask app started")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))



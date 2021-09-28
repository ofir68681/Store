import uvicorn
from init_app import *


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5555)


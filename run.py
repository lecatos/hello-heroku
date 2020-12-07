import os
import threading

a = threading.Thread(os.system("FLASK_APP=web.py python -m flask run --host=0.0.0.0 --port=$PORT"))
b = threading.Thread(os.system("python"))

a.join()
b.join()

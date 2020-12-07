import os
import threading

a = threading.Thread(target=lambda : os.system("FLASK_APP=web.py python -m flask run --host=0.0.0.0 --port=$PORT"))
b = threading.Thread(target=lambda : os.system("python"))
c = threading.Thread(target=lambda : os.system("python"))

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()

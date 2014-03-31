# Härskisti kopioitua netistä
import os

processoutput = os.popen("ps -Af").read()
print(processoutput)

__author__ = 'Feely'

import subprocess
import os
def php(code):
  # open process
  p = subprocess.Popen(['php'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)

  # read output
  o = p.communicate(code)[0]

  # kill process
  try:
    os.kill(p.pid, os.signal.SIGTERM)
  except:
    pass

  # return
  return o

php("-f /tmp/test/autokj.php autokj '7' '4' '4' '4' '4' 1 '140823053' 1")

#/usr/bin/python
import time
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.strerr_path = '/dev/tty'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
        while True:
            pring("1s")
            time.sleep(10)

app = App()
daemon_runner - runner.DaemonRunner(app)
daemon_runner.do_action()


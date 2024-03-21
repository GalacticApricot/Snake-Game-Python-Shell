import sys
import termios
import tty
import select

class _Getch:
    """Gets a single character from standard input. Does not echo to the
    screen."""

    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        pass

    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            if select.select([sys.stdin], [], [], 0.3)[0]:
                ch = sys.stdin.read(1)
                return ch
            else:
                return None
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


getch = _Getch()

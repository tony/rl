# Complete system commands

import os
from completion import completer


class complete(object):
    # Completion function implementing readline's
    # generator protocol

    def __call__(self, text, state):
        if state == 0:
            self.matches = []
            for dir in os.environ.get('PATH').split(':'):
                for name in os.listdir(dir):
                    if name.startswith(text):
                        if os.access(os.path.join(dir, name), os.R_OK|os.X_OK):
                            self.matches.append(name)
        try:
            return self.matches[state]
        except IndexError:
            return None


def main():
    # Set the completion function
    completer.completer = complete()

    # Enable TAB completion
    completer.parse_and_bind('tab: complete')

    command = raw_input('command> ')
    print 'You typed:', command


if __name__ == '__main__':
    main()
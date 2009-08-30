"""Interface to readline history."""

import _readline as readline


class History(object):
    """Interface to readline history.

    This class is not intended for instantiation beyond
    the one ``history`` object in this module.
    Applications wanting to use the History interface will
    typically import the ``history`` object and use its
    properties and methods to work with readline history.

    Example::

        from rl import history
        import atexit

        history.read_file(histfile)
        history.length = 100
        atexit.register(history.write_file, histfile)
    """

    @property
    def current_length(self):
        """Get the current (not the maximum) length of history."""
        return readline.get_current_history_length()

    def __len__(self):
        """Alias for ``current_length``."""
        return self.current_length

    @property
    def base(self):
        """Get the current history base position."""
        return readline.get_history_base()

    @apply
    def length():
        doc="""This many lines will be saved in the history file."""
        def get(self):
            return readline.get_history_length()
        def set(self, int):
            readline.set_history_length(int)
        return property(get, set, doc=doc)

    def add(self, line):
        """Add a line to the history."""
        readline.add_history(line)

    def clear(self):
        """Clear the current readline history."""
        readline.clear_history()

    def get_item(self, pos):
        """Return the current contents of history at pos (relative to ``history.base``)."""
        return readline.get_history_item(pos)

    def remove_item(self, pos):
        """Remove a history item given by its position (zero-based)."""
        readline.remove_history_item(pos)

    def replace_item(self, pos, line):
        """Replace a history item given by its position with contents of line (zero-based)."""
        readline.replace_history_item(pos, line)

    def read_file(self, filename=None, raise_exc=False):
        """Load a readline history file. The default filename is ~/.history."""
        self._file_op(readline.read_history_file, filename, raise_exc)

    def write_file(self, filename=None, raise_exc=False):
        """Save a readline history file. The default filename is ~/.history."""
        self._file_op(readline.write_history_file, filename, raise_exc)

    def _file_op(self, op, filename, raise_exc):
        """Perform a file operation optionally ignoring IOErrors."""
        try:
            if filename:
                op(filename)
            else:
                op()
        except IOError:
            if raise_exc:
                raise

history = History()


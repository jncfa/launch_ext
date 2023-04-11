
from pathlib import Path
from tempfile import NamedTemporaryFile

from launch.substitutions import PathJoinSubstitution
from launch_ext.substitutions import FileContents


def test_file_contents():
    with NamedTemporaryFile() as f:
        f.write(b'asdf')
        f.flush()
        sub = FileContents(f.name)
        assert sub.perform(None) == 'asdf'

        p = Path(f.name)
        sub = FileContents(PathJoinSubstitution([p.parent, p.name]))
        assert sub.perform(None) == 'asdf'

from pathlib import Path, PurePath
exec(next(
    Path(Path.cwd().parent.parent/'typeshed/stdlib/').rglob('pathlib*')).read_text(), globals())
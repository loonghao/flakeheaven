# built-in
from hashlib import md5
from pathlib import Path


def make_baseline(path: Path, context: str, code: str, line: int) -> str:
    digest = md5()
    digest.update(path.as_posix().lstrip('./').encode())
    digest.update((context or str(line)).strip().encode())
    digest.update(code.encode())
    return digest.hexdigest()

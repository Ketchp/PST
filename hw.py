from json import load
from sys import argv
from pathlib import Path
from typing import Any, Optional


def run_ipynb(*, filename: Optional[Path | str] = None, code: Optional[dict[str, Any]] = None):
    if filename is None:
        src_name = argv[1] if len(argv) > 1 else 'hw.ipynb'
        return run_ipynb(filename=Path(src_name))
    if code is None:
        with open(filename, 'r') as f:
            src: dict[str, Any] = load(f)
        return run_ipynb(filename=filename, code=src)

    code_cells = [cell['source'] for cell in code['cells'] if cell['cell_type'] == 'code']

    _globals = {'__file__': str(Path(filename).resolve())}
    for cell in code_cells:
        code = ''.join(cell)
        exec(code, _globals)


if __name__ == '__main__':
    exit(run_ipynb())

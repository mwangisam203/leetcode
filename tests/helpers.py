"""Load each practice variant before a later definition replaces its name."""
import ast
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_variants():
    variants = []
    for relative in ('Arrays/arrays.py', 'Hashing/hashing.py', 'Notes.py', 'test.py'):
        path = ROOT / relative
        namespace = {'__name__': 'practice_examples'}
        tree = ast.parse(path.read_text(), filename=str(path))
        with redirect_stdout(StringIO()):
            for node in tree.body:
                exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
                label = f'{relative}:{node.lineno}'
                if isinstance(node, ast.FunctionDef):
                    variants.append((label, node.name, namespace[node.name]))
                elif isinstance(node, ast.ClassDef):
                    cls = namespace[node.name]
                    if node.name == 'MyHashMap':
                        variants.append((label, node.name, cls))
                    else:
                        instance = cls()
                        for method in node.body:
                            if isinstance(method, ast.FunctionDef):
                                variants.append((label, method.name, getattr(instance, method.name)))
    return variants


VARIANTS = load_variants()
SMALL_ARRAYS = [list(items) for n in range(5) for items in product((-1, 0, 1), repeat=n)]

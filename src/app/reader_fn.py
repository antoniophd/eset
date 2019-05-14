import traceback
import json
import re
from app.reader import Reader


class Reader_fn(Reader):
    def __init__(self):
        super().__init__()

    def get(self, fns, trafo):
        try:
            dct = {}
            for fn in fns:
                # TODO think about a decorator. this solution is weak
                isTimestamp = re.search('\/(\d{10})_', fn)
                if isTimestamp:
                    dct.update({'timestamp': isTimestamp.group(1)})
                dct.update(json.loads(open(fn).read()))
            return tuple(trafo(dct))
        except Exception:
            traceback.print_exc()
        return False

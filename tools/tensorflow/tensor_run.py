import json
import sys
import time
from importlib import import_module

import tensorflow as tf


def resolve():
    functions = import_module("GMM")
    return getattr(functions, "calculate_jacobian")

def run():
    func = resolve()
    vals = "d2_k5.txt"    
    start = time.perf_counter_ns()
    ret = func(vals)
    end = time.perf_counter_ns()
    return {"return": list(ret.numpy()), "nanoseconds": end - start}


def main():
    # cfg = json.load(sys.stdin)
    # outputs = [run(params) for params in cfg["inputs"]]
    print(json.dumps({"outputs": run()}))


if __name__ == "__main__":
    main()


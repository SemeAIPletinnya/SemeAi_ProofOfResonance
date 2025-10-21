
import sys, time

def log(*args):
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(f"[{{ts}}]", *args, file=sys.stdout, flush=True)

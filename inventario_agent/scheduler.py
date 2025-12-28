import time

class Scheduler:
    def __init__(self, interval_seconds: int):
        self.interval = interval_seconds

    def run_forever(self, tick_fn):
        while True:
            try:
                tick_fn()
            except Exception as e:
                print(f"[scheduler] error en ciclo: {e}")
            time.sleep(self.interval)

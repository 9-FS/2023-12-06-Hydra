# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import logging
import threading
import time


def main(DEBUG: bool) -> None:
    while True:
        try:
            logging.info("Hail hydra!")
            time.sleep(10)
        except KeyboardInterrupt:
            threading.Thread(target=main, args=(DEBUG,)).start()
            threading.Thread(target=main, args=(DEBUG,)).start()
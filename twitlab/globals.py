import logging

def _get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    _ch = logging.StreamHandler()
    _ch.setLevel(logging.DEBUG)
    f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    _ch.setFormatter(f)
    log.addHandler(_ch)
    return log

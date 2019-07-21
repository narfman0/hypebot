import logging


def create_logger(name):
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    return logger

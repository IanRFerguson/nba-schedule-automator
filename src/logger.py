import logging
import os

logger = logging.getLogger(__name__)
_handler = logging.StreamHandler()
_formatter = logging.Formatter("%(levelname)s %(message)s")
_handler.setFormatter(_formatter)
logger.addHandler(_handler)
logger.setLevel("INFO")

if os.environ.get("DEBUG").lower() == "true":
    logger.setLevel(level=10)
    logger.debug("** Debugger Active **")

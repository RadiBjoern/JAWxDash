import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,  # Options: DEBUG, INFO, WARNING, CRITICAL
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

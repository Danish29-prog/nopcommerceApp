import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename='C:/Users/Admin/PycharmProject/nopcommerceApp/Logs/automation.log',
            filemode='w',
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s: %(message)s',
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

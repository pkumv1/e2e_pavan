import sys
from src.logger import logging


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.frame.f_code.co_filename
    error_message = "this error occoured because of python script filename[{0}], line no[{1}] message [{2}]".format(
        file_name, exc_tb.lineno, str(error)
    )
    return error_message


class CustomEXception(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(self, error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


# if __name__ == "__main__":
#
#    try:
#        a = 1 / 0
#    except:
#        logging.info("divide by zero error")
#        raise CustomEXception

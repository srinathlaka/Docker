import os
import sys


class HousingException(Exception):

    def  __init__(self , error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                         error_detail=error_detail)


    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys) -> str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """

        exc_type, exc_value, exc_traceback = error_detail.exc_info()
        line_number = exc_traceback.tb_lineno
        file_name = exc_traceback.tb_frame.f_code.co_filename

        error_message = f"Error occurred in script [{file_name}] at line number [{line_number}]: {error_message}"

        return error_message
    

    def __str__(self):
        return self.error_message
    

    def __repr__(self) -> str:
        return HousingException.__name__.str()
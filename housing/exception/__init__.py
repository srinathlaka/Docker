import os
import sys


class HousingException(Exception):

    def  __init__(self , error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                         error_details=error_details)


    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:

        """
        
        error_message: Exception object
        error_detail: ibject of sys module
        """

        _,_exec_tb = error_detail.exc_info()
        line_number = _exec_tb.tb_frame.f_lineno
        file_name = _exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in script; [{file_name}] at line munber: [{line_number}] error message : [{error_message}]"



        return error_message
    

    def __str__(self):
        return self.error_message
import os
import sys
import unittest
from io import StringIO
from getpass import getpass
import coding_clinic as coding_clinic
<<<<<<< HEAD

class ClinicTestCase(unittest.TestCase):
    def test_do_main_red(self):
        sys.argv[0] = '/goinfre/imogano/CODING-CLINIC-BOOKING-SYSTEM/iteration_two/Coding_Clinic/coding_clinic.py'
        invalid_commands = ['awfgdv3','-sdt4','a-help',' - - help', '', '23-help', ' ']
=======
from team32 import sys_encryp as sys_encrypt
from team32 import view_calednar as view_calednar
from team32 import make_booking as booking
from team32 import create_slots as createslots
from team32 import cancel_booking as cancel_b
from team32 import cancel_slots as cancel_slots
from tests import test_cancel_booking as test_cancel_booking
from tests import test_cancel_slots as test_cancel_slots
from tests import test_create_slots as test_create_slots
from tests import test_make_booking as test_make_booking


class ClinicTestCase(unittest.TestCase):
    def test_do_main_red(self):
        sys.argv[0] = 't'
        invalid_commands = ['awfgdv3','-sdt4','a-help',' - - help', '', \
'23-help', ' ']
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
        expected_output = """Help

    View calendar            cmd arg:    vc
    View clinic calendar     cmd arg:    vcc
    Make booking             cmd arg:    mb
    Create Slot              cmd arg:    cs
    Cancel Booking           cmd arg:    cb
    Cancel Slot              cmd arg:    csl
    Delete pickle            cmd arg:    dp
    Logged in user           cmd arg:    who
    Log in                   cmd arg:    login
    Log out                  cmd arg:    logout
    Help                     cmd arg:    help

i.e: clinic -help
"""
        for command in invalid_commands:
            sys.argv[1] = command
            temp_out = StringIO()
            sys.stdout = temp_out
            coding_clinic.do_main()
            obtained_output = temp_out.getvalue()
            temp_out.close()
            self.assertEqual(expected_output, obtained_output)


    def test_do_main_green(self):
<<<<<<< HEAD
        sys.argv[0] = '/goinfre/imogano/CODING-CLINIC-BOOKING-SYSTEM/iteration_two/Coding_Clinic/coding_clinic.py'
=======
        sys.argv[0] = 't'
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
        valid_commands = ['help', '-help', '--help']
        expected_output = """Help

    View calendar            cmd arg:    vc
    View clinic calendar     cmd arg:    vcc
    Make booking             cmd arg:    mb
    Create Slot              cmd arg:    cs
    Cancel Booking           cmd arg:    cb
    Cancel Slot              cmd arg:    csl
    Delete pickle            cmd arg:    dp
    Logged in user           cmd arg:    who
    Log in                   cmd arg:    login
    Log out                  cmd arg:    logout
    Help                     cmd arg:    help

i.e: clinic -help
"""
        for command in valid_commands:
            sys.argv[1] = command
            temp_out = StringIO()
            sys.stdout = temp_out
            coding_clinic.do_main()
            obtained_output = temp_out.getvalue()
            temp_out.close()
            self.assertEqual(expected_output, obtained_output)

    
    def test_validate_cmd_arg_red(self):
        invalid_commands = ['asvc', '-vdccde3','- vc- rr', '1']
        for command in invalid_commands:
            return_result = coding_clinic.validate_cmd_arg(command)
            self.assertFalse(return_result)
    
   
    def test_validate_cmd_arg_green(self):
        invalid_commands = ['-vc', '-help','--mb', 'cs', ' vcc ']
        for command in invalid_commands:
            return_result = coding_clinic.validate_cmd_arg(command)
            self.assertTrue(return_result)


<<<<<<< HEAD
    # def test_step_validate_user_red(self):
    #     temp_out = StringIO()
    #     temp_in = StringIO("n\n")

    #     sys.stdout = temp_out
    #     sys.stdin = temp_in

    #     temp_in.write('n\n')

    #     coding_clinic.decrypt_credentials = lambda : {"red_passwd" : "testing"}

    #     coding_clinic.getpass.getpass = lambda str: 'redpasswd'

    #     return_result = coding_clinic.validate_user()

    #     obtained_output = temp_out.getvalue()

    #     self.assertFalse(return_result)



=======
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046
    def test_step_validate_user_green(self):

        coding_clinic.decrypt_credentials = lambda : {"red_passwd" :"testing",
                                                     "1234"        :"kkolo", 
                                                     "12ab"        :"rokloo"}

        coding_clinic.getpass.getpass = lambda str: 'red_passwd'

        return_result = coding_clinic.validate_user()

        expected_result = "testing"

        self.assertEqual(return_result, expected_result)

        coding_clinic.getpass.getpass = lambda str: '1234'

        return_result = coding_clinic.validate_user()

        expected_result = "kkolo"

        self.assertEqual(return_result, expected_result)
  
        coding_clinic.getpass.getpass = lambda str: '12ab'

        return_result = coding_clinic.validate_user()

        expected_result = "rokloo"

        self.assertEqual(return_result, expected_result)
        

    def test_prompt_first_time_red(self):
        temp_out = StringIO()
        temp_in = StringIO("asd\n1qq2s\n s 2\n cdd\n n\n")

        sys.stdout = temp_out
        sys.stdin = temp_in

        coding_clinic.prompt_first_time()

        obtained_output = temp_out.getvalue()
        expected_output = """\
Is this your first time login? [n/Y] \
Is this your first time login? [n/Y] \
Is this your first time login? [n/Y] \
Is this your first time login? [n/Y] \
Is this your first time login? [n/Y] \
"""
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        self.assertEqual(expected_output,obtained_output)


    def test_prompt_first_time_green(self):               
        valid_commands = [" n", "N ", "y ", "Y"]
        for i in valid_commands:
            a = f'{i}\n'
            temp_out = StringIO()
            temp_in = StringIO(a)

            sys.stdin = temp_in
            sys.stdout = temp_out

            return_result = coding_clinic.prompt_first_time()
            self.assertEqual(i.strip().lower(), return_result)    

            obtained_output = temp_out.getvalue()
            expected_output = "Is this your first time login? [n/Y] "
            self.assertEqual(expected_output,obtained_output)

            temp_in.close()
            temp_out.close()
            
            sys.stdin = sys.__stdin__     
            sys.stdout = sys.__stdout__
        

    def test_first_time_user_red(self):
        temp_out = StringIO()
<<<<<<< HEAD
        temp_in = StringIO("asdberj@gmail.com\nimoa@yahoo.co.za\nimog@studio.o\ni@wethinkcode.co.za\n")
=======
        temp_in = StringIO("asdberj@gmail.com\nimoa@yahoo.co.za\nimog@studio.o\
\ni@wethinkcode.co.za\n")
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

        sys.stdin = temp_in
        sys.stdout = temp_out

        expected_output = """\
WTC email: WTC users only.\n\
WTC email: WTC users only.\n\
WTC email: WTC users only.\n\
WTC email: \
"""
        coding_clinic.get_new_password = lambda : ''
        coding_clinic.update_json_first_time_use = lambda a, b: True
        coding_clinic.first_time_user()
        
        obtained_output = temp_out.getvalue()

        sys.stdin = sys.__stdin__     
        sys.stdout = sys.__stdout__

        self.assertEqual(expected_output,obtained_output)
    
    
    def test_first_time_user_green(self):
        temp_out = StringIO()
        temp_in = StringIO("imogano@student.wethinkcode.co.za\n")

        sys.stdin = temp_in
        sys.stdout = temp_out

        expected_output = """WTC email: """
        coding_clinic.get_new_password = lambda : ''
        coding_clinic.update_json_first_time_use = lambda a, b: True
        coding_clinic.first_time_user()
        
        obtained_output = temp_out.getvalue()

        sys.stdin = sys.__stdin__     
        sys.stdout = sys.__stdout__

        self.assertEqual(expected_output,obtained_output)
<<<<<<< HEAD


    def test_step_five_red(self):
        pass

    def test_step_five_green(self):
        pass
    
    def test_step_six_red(self):
        pass
    def test_step_six_green(self):
        pass
    def test_step_seven_red(self):
        pass
    def test_step_seven_green(self):
        pass
    def test_step_eight_red(self):
        pass
    def test_step_eight_green(self):
        pass
    def test_step_nine_red(self):
        pass
    def test_step_nine_green(self):
        pass
    def test_step_ten_red(self):
        pass

    # def test_step_make_booking_tests(self):
    #     # See test_main in tests folder

    #     loader = unittest.TestLoader()

    #     suite = loader.loadTestsFromName('test_main')

    #     runner = unittest.TextTestRunner(stream=sys.stdout)
        
    #     # return runner.run(suite)
        
    #     # test_result = run_unittests("make_booking")

    #     test_result = runner.run(suite)

    #     self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")

    # def test_step_create_volunteer_slots_tests(self):
    #     # See test_main in tests folder

    #     loader = unittest.TestLoader()

    #     suite = loader.loadTestsFromName('test_main')

    #     runner = unittest.TextTestRunner(stream=sys.stdout)
        
    #     # return runner.run(suite)
        
    #     # test_result = run_unittests("create_volunteer_slots")

    #     test_result = runner.run(suite)

    #     self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")
=======
>>>>>>> cf241b6cb422db7e0961459f488ab894a181f046

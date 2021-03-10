import sys

if len(sys.argv) > 1:
    print("(package and module load output)")
    for i in sys.argv[1:]:
        print(i) 
    print("(and the rest of the output)")

    
else:
    from user import authentication
    from transactions import journal
    from banking import reconciliation
    from banking import *
    # import banking.fvb.reconciliation as fvb
    # import banking.ubsa.reconciliation as ubsa
    # import banking.online.reconciliation as online

    authentication.authenticate_user()

    journal.receive_income(100)
    journal.pay_expense(100)
    reconciliation.do_reconciliation()

    # fvb.do_reconciliation()
    # ubsa.do_reconciliation()
    # online.do_reconciliation()
    '''help("modules")'''
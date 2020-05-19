import csv
import gettext
file1 = open(r"C:\Users\Michiel\Desktop\Pyhon\Full test file.txt", 'r')
file2 = ""
with file1 as f:
    for line in f:
        keys = {'600001130260', 'CTOT', 'CUR', 'Due Date', 'VAT', '020', '030', '010', '040', 'STOT', '000', '005',
                '050', '0100', 'BBF', 'INT',
                'CIN', 'CTOT', 'DD', 'YVLEVY', 'YRREM'}
        tokens = line.split("|")

        if len(tokens) and tokens[0] in keys and tokens[5] == 'CTOT':
            Total_due = ' '.join(tokens[7:8])
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'DD':
            Due_date = ' '.join(tokens[7:8])
            print ["Due_date", Due_date]
        elif len(tokens) and tokens[0] in keys and tokens[4] == 'VAT':
            Vat_14 = ' '.join(tokens[7:8])
            print ["Vat_14", Vat_14]
        elif len(tokens) and tokens[0] in keys and tokens[1] == '020':
            Adrress_code = ' '.join(tokens[4:6])
            print ["Adrress_code", Adrress_code]
            Company_name = ' '.join(tokens[3:4])
            print ["Company_name", Company_name]
        elif len(tokens) and tokens[0] in keys and tokens[1] == '030':
            Portion = ' '.join(tokens[5:6])
            print ["Portion", Portion]
        elif len(tokens) and tokens[0] in keys and tokens[1] == '010':
            Account = ' '.join(tokens[4:5])
            print ("Account", Account)
            tax = ' '.join(tokens[13:14])
            print ["tax", tax]
            post_office = ' '.join(tokens[7:8])
            print ["post_office", post_office]
            Easy_pay = ' '.join(tokens[6:7])
            print ["Easy_pay", Easy_pay]
        elif len(tokens) and tokens[0] in keys and tokens[1] == '040':
            Stand_size = ' '.join(tokens[3:4])
            print ["Stand_size", Stand_size]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'BBF':
            Open_balance = ' '.join(tokens[7:8])
            print["Open_balance", Open_balance]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'STOT':
            Sub_total = ' '.join(tokens[7:8])
            print["Sub_total", Sub_total]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'CUR':
            Current_charges = ' '.join(tokens[7:8])
            print ["Current_charges", Current_charges]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'INT':
            Open_balance = ' '.join(tokens[7:8])
            print ["Open_balance", Open_balance]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'CIN':
            Instal_Amount = ' '.join(tokens[8:9])
            print ["Instal_Amount", Instal_Amount]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'CTOT':
            Total_Due = ' '.join(tokens[7:8])
            print["Total_Due", Total_Due]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'YSBASC':
            Sewerage = ' '.join(tokens[7:8])
            print ["Sewerage", Sewerage]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'BBF':
            Open_balance = ' '.join(tokens[7:8])
            print ["Open_balance", Open_balance]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'YVLEVY':
            Rates_taxA = ' '.join(tokens[7:8])
         #   if Rates_tax == '0.00': print ("???")
            print ["Rates_tax", Rates_taxA]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'YRREM':
            Refuse = ' '.join(tokens[7:8])
            print ["Refuse", Refuse]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'YECONS':
            Electricity = ' '.join(tokens[7:8])
            print["Electricity", Electricity]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'YWCONS':
            Water = ' '.join(tokens[7:8])
            print ["Water", Water]  # type: str
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'OIP':
            Instal_Deposit = ' '.join(tokens[7:8])
            print["Instal_Deposit", Instal_Deposit]
        elif len(tokens) and tokens[0] in keys and tokens[5] == 'BBF':
            Instal_Balance = ' '.join(tokens[7:8])
            print ["Install_Balance", Instal_Balance]
        elif len(tokens) and tokens[0] in keys and tokens[1] == '150':
            ninety_days = ' '.join(tokens[3:4])
            print ["Ninety_Days", ninety_days]
            sixty_days = ' '.join(tokens[4:5])
            print ["Sixty_Days", sixty_days]
            thirty_days = ' '.join(tokens[5:6])
            print ["Thirty_Days", thirty_days]
            current_days = ' '.join(tokens[6:7])
            if current_days == ' ':
                print('empty')
            print ["Current_Days", current_days]
            instal_plan = ' '.join(tokens[7:8])
            print ["Instal_plan", instal_plan]
#Not Sure What you want To do here but it will print row list with thos default values defined if ypu want to print the data then simply replace the Row list array by saying Row_list = tokens and its should print in the ouput fine including empty values
#example code to print values will be Row_list = tokens
#Remeber Very important in Python is indentation it can screw you over in terms of errors aswell as incorrect output so make sure the indetation is correct 
    Row_list =['ADDRESS', 'PORTION', 'ACC_NUM', 'DEPOSIT', 'STAND_SIZE', 'TAX_INVOICE', 'OPEN_BAL',
                 'SUB_TOTAL', 'CURRENT_CHARGES', 'INTEREST_ARREARS', 'INSTAL_AMOUNT', 'VAT', 'TOTAL_DUE', 'DUE_DATE',
                 'SEWERAGE', 'RATES_TAXES', 'REFUSE', 'ELECTRICITY', 'WATER', 'TOTAL_CHARGES', 'INSTAL_PLAN_AMOUNT',
                 'INSTAL_DEPOSIT', 'INSTAL_BALANCE', 'MONTH_INSTAL_AMOUNT', 'NINETY_DAYS', 'SIXTY_DAYS', 'CURRENT_DAYS',
                 'INSTAL_PLAN', 'THIRTY_DAYS', 'TOTAL_INSTAL_OUTSTANDING', 'EASY_PAY_REF', 'POST_OFFICE_REF',
                 'BENEFICIARY', 'COMPANY_NAME', 'CIN', 'MANUAL_DEPOSIT', 'REFERENCE', 'ACC_NUM', 'FIRST_NAME']
    file2 = "writing.csv"
    with open("writing.csv", "w", newline='') as output:
        wr = csv.writer(output, quoting=csv.QUOTE_ALL)
        for row in Row_list:
                wr.writerow([Row_list])
                
#This is what you had to write to the file 
   # with open("writing.csv","w", newline='') as output:
   #     for row in Row_list:
   #         output.write(str(row)+ '\n')
   #          #writer = csv.writer(file2, delimiter=',')
   #         writer.writerows(Row_list)
   #        writer = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   #         writer.writerow(
   #         ["ADDRESS"])
   #        writer.writerow([Adrress_code])


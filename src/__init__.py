import os

# General flags
NO_ARG = 0
N_OUT = 1
Y_OUT = 2
M_OUT = 3
SRCH_SCHOOLDESC = 3
SRCH_PARID = 4

# Index of each position in the arguments list
POS_ARG_TYPE = 0
POS_ARG_KEY = 1
POS_ARG_OUT = 2
POS_ARG_PATH = 3

# Path of the CSV file.
# P. S.: This path should be absolute ou passed as a parameter to read_data. Here it is assumed that this
# application will be executed through main.py
CSV_PATH = os.getcwd() + "\input\property_sales_transactions.csv"

def parse_arg(arg):
    argum = {}
    # If the correct number of arguments was entered
    if  (len(arg) >= 2) and (len(arg) <= 4):
        if arg[POS_ARG_TYPE] == "--filter-school-desc":
            argum["srch_type_in"] = arg[POS_ARG_TYPE]
            argum["srch_key"] = arg[POS_ARG_KEY]
            argum["srch_type_code"] = SRCH_SCHOOLDESC                    
        elif arg[POS_ARG_TYPE] == "--find-pair-id":
            argum["srch_type_in"] = arg[POS_ARG_TYPE]
            argum["srch_key"] = arg[POS_ARG_KEY]
            argum["srch_type_code"] = SRCH_PARID
        else:
            argum["srch_type_code"] = NO_ARG
            return argum

        # If a option to save the results may have been chosen
        if len(arg) > 2:
            # If the 'output' option was typed
            if (arg[POS_ARG_OUT] == "-o") or (arg[POS_ARG_OUT] == "--output"):
                # if the path may have been provided
                if len(arg) > 3:
                    argum["srch_out_path"] = arg[POS_ARG_PATH] # to-do: check for forbidden characters
                    argum["out"] = Y_OUT
                # Otherwise (len(arg) == 3) we report an error and tell the function caller
                # that the output path is missing
                else:
                    argum["srch_type_code"] = NO_ARG # This error turns the whole command invalid
                    argum["out"] = M_OUT # This flag tells the caller that the path is missing
            # Otherwise the command is invalid
            else:
                argum["srch_type_code"] = NO_ARG
        # Otherwise (len(arg) == 2) the command is valid but the results shall not be saved
        else:
            argum["out"] = N_OUT  

    else:
        argum["srch_type_code"] = NO_ARG
    
    return argum

def read_data():
    file_csv = open(CSV_PATH, 'r')

    data_in = []

    for line in file_csv:
        columns = line.strip().split(',')
        data_in.append(columns)

    file_csv.close()

    return data_in
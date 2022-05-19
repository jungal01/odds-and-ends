#!/usr/bin/env python3

"""
WorkDay Export Updater - CVS version
The purpose of this file is to update spreadsheets that were exported from
Workday. This is especially useful when tracking coworkers in unionization
campaigns. This script accepts two csv files and compares them after removing
the formatting from workday. It outputs a CSV file that contains all the people
not in the old file and removes people that are not in the new file. The
primary advantage to this file is that it has less engineering overhead.
WorkDay exports exclusively to excel formatting, so it will need to be manually
converted to csv to use this script. Some manual massaging is also required on
the CSV file to format correctly, such as deleting or combining columns.
------------------------------------------------------------------------------
Known issues: attempting to use the full functionality of this script causes
all data left of the name to shift up one column. While this is being fixed,
cleaning up the data is still fully functional.
"""


def cli_prompt():
    old_file = None
    new_file = None
    output = "output.csv"
    done = False
    while not done:
        old_file = str(input("Path to the old file: "))
        new_file = str(input("Path to the new file: "))
        # testing inputs for data validation. Data manipulation happens later
        try:
            test1 = open(old_file)
            test2 = open(new_file)
            test1.close()
            test2.close()
            done = True

            if ".csv" not in (old_file or new_file):
                print("One or more files are not CSV. This script only accepts CSV")
                done = False

        except:
            print("one or more file paths were incorrect. Try again.")
            print("tip: if the files are within the same directory as this script, just enter the file names")
            print("")

            

    output_name = str(input("(optional) name of the output file: "))
    if output_name != "":
        output = output_name+".csv"

    return old_file, new_file, output


def main():
    #old_file, new_file, output_file = cli_prompt()
    #old_data = open(old_file)
    new_data = open("new_folks.csv")
    output = open("output.csv", "w")
    
    #old_list = list(old_data.read().split('\n'))
    new_list = list(new_data.read().split('\n'))
    output_list = []
    new_people = set()
    current_people = set()
    
    # from WD format to desired format: 
    # 0                ,2, 4                              , 1                     , 3             
    # John Doe (000111), , John.Doe@company.com (John Doe), QA Functional Tester I, Trudy Eve
    
    # 0                , 1                     ,2, 3        , 4
    # John Doe (000111), QA Functional Tester I, , Trudy Eve, John.Doe@company.com (John Doe)
    temp_list = []
    for line in range(len(new_list)-1):
        temp_data = new_list[line].split(',')
        temp_data += [''] * 17
        # in place swapping to avoid complex data manipulation
        temp_data[1], temp_data[3] = temp_data[3], temp_data[1]
        temp_data[2], temp_data[3] = temp_data[3], temp_data[2]
        temp_data[4], temp_data[3] = temp_data[3], temp_data[4]
        # This isolates the name of the supervisor. WorkDay manager formatting
        # all follows the same format, so this can be relied upon in most cases
        print(temp_data[0])
        temp_data[3] = temp_data[3].split("(")[2].strip()
        temp_list.append(','.join(temp_data))
        new_people.add(temp_data[0])
    
    """
    # The good stuff; comparing lists to write to output
    for line in range(len(old_list)):
        if old_list[line].split(',')[0] in new_people:
            current_people.add(old_list[line].split(',')[0])
            output_list.append(old_list[line])
    S"""     
    for line in range(len(temp_list)):
        if temp_list[line].split(',')[0] not in current_people:
            output_list.append(temp_list[line])
    
    # write to the output file. The first line is the table header
    output.write('Name (Employee ID),Job Title,Card Signer,Manager,Work Email,Home Address,Home City,Home State,Home Zip,Personal Email,Personal Phone,Twitter Handle,Discord Handle,Primary Contact,ABK National OC,Committee,Attended Past Meeting?,Attend 2/16 OC Meeting?,Invited to Discord?,Assessment,Unit Eligible?,Last 1:1 Contact,Notes\n')
    for final_data in output_list:
        output.write(final_data+'\n')
        
    #old_data.close()
    new_data.close()
    output.close()
    


main()

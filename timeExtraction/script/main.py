import os
from utils import *


main_folder = "../"
solver_folder = "all_kissat/"
cnf_folder = "../../test_file/"
solver_list = ["Kissat_MAB-HyWalk/", "kissat_inc/sources/", "ekissat-mab-db-v1/", "Kissat_MAB_MOSS/build/kissat/", "Kissat_MAB_UCB/build/kissat/"]
options = ["", "--ultimate", "--sat --no-options", "--unsat --no-options"]
timeout = 60
result_filname = ["global.txt","y.txt"]
     
def main():
    os.chdir(main_folder)
    cnf_list = folder_content(cnf_folder)
    cnf_total_result = []
    y = []
    for cnf in cnf_list:
        time_cnf_result = find_best(cnf, timeout, solver_list, solver_folder, options, cnf_folder)
        print(time_cnf_result)
        new_result = extract_result(time_cnf_result,cnf, options, solver_list, timeout)
        cnf_total_result.append(new_result)
        y.append([new_result[1]])
        print(y)
        print(cnf_total_result)
    store_array_in_file(cnf_total_result,result_filname[0])
    store_array_in_file(y,result_filname[1])

main()
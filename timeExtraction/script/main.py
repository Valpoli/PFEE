import os
from utils import *


main_folder = "../"
solver_folder = "all_kissat/"
cnf_folder = "../../test_file/"
# cnf_folder = "for_test/"
solver_list = ["Kissat_MAB-HyWalk/", "kissat_inc/sources/", "ekissat-mab-db-v1/", "Kissat_MAB_MOSS/build/kissat/", "Kissat_MAB_UCB/build/kissat/"]
# solver_list = ["Kissat_MAB-HyWalk/"]
options = ["", "--ultimate", "--sat --no-options", "--unsat --no-options"]
timeout = 250
result_filname = ["result_19_06","complete_time_result_19_06"]
     
def main():
    os.chdir(main_folder)
    cnf_list = folder_content(cnf_folder)
    # cnf_total_result = []
    # y = []
    for cnf in cnf_list:
        time_cnf_result = find_best(cnf, timeout, solver_list, solver_folder, options, cnf_folder)
        print(time_cnf_result)
        new_result = extract_result(time_cnf_result,cnf, options, solver_list, timeout)
        # cnf_total_result.append(new_result)
        # y.append([new_result[1]])
        # print(y)
        # print(cnf_total_result)
        print(cnf)
        print("///////////////////////////Done, going to the next/////////////////////////////")
        ajouter_ligne_fichier(new_result,result_filname[0])
        ajouter_ligne_fichier(time_cnf_result,result_filname[1])
        # store_array_in_file([new_result[1]],result_filname[1])
main()
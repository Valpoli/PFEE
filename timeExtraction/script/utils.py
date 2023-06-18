import subprocess
import os
import re


def execute_command(command, timeout):
    try:
        print(command)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _, stderr = process.communicate(timeout=timeout)
        return [stderr.decode(), _.decode()]
    except subprocess.TimeoutExpired:
        if process is not None:
            process.kill()
            # Timeout reached
        return ["TO", ""]
    

# parse the result of a solver
def find_result(string):
    if "UNSATISFIABLE" in string:
        return False
    elif "SATISFIABLE" in string:
        return True
    else:
        return False

# return name list of folder's element 
def folder_content(folder_path):
    res = []
    for filename in os.listdir(folder_path):
        res.append(filename)
    return res


def compte_mots(chaine):
    mots = chaine.split('/')
    nombre_mots = len(mots)
    if nombre_mots > 1:
        return "../" * (nombre_mots - 1)
    else:
        return ""
    

def find_best(file_path, timeout, solver_list, solver_folder, options, cnf_folder):
    execution_time = []
    i = 0
    nb_s = len(solver_list)
    #check if the solver make a good response
    good_result = True
    while i < nb_s:
        time_result = []
        if (i != 0):
            os.chdir(compte_mots(solver_list[i-1]) + solver_list[i])
        else :
            os.chdir(solver_folder + solver_list[i])
        for option in options:
            # building of the command
            config = "./configure " + option + " && "
            make = "make" " && "
            to = "time timeout " + str(timeout) + " "
            solver_exec = "build/kissat " + compte_mots(solver_list[i]) + "../" + cnf_folder + file_path
            # execute command
            command_res = execute_command(config + make + to + solver_exec, timeout)
            # si time out on ajoute pas de temps
            if (option == ""):
                if (not find_result(command_res[1])):
                    good_result = False
            if (command_res[0] == "TO"):
                time_result.append(-3)
            else :
                if (good_result):
                    # extract the time
                    match = re.search(r"(\d+\.\d+)user", command_res[0])
                    if match:
                        time_seconds = float(match.group(1))
                        time_execution = int(time_seconds * 1000)
                        time_result.append(time_execution)
                    else:
                        time_result.append(-1)
                else:
                    time_result.append(-2)
        execution_time.append(time_result)
        i += 1
    os.chdir("../" + compte_mots(solver_list[i-1]))
    return execution_time

def extract_result(time_cnf_result,cnf, options, solver_list, timeout):
    options_len = len(options)
    solver_len = len(solver_list)
    i = 0
    best_time = timeout * 1001
    best_solv = 0
    best_option = 0
    while i < solver_len :
        j = 0
        while j < options_len :
            if (time_cnf_result[i][j] > 0 and time_cnf_result[i][j] < best_time):
                best_solv = i
                best_option = j
                best_time = time_cnf_result[i][j]
            j += 1
        i += 1
    # si aucune solution n'a été trouvé on renvoi NS (no solution)
    if (best_time == timeout * 1001):
        return [cnf,"NS","NS","NS","NS"]
    # sinon on renvoi dans l'ordre nom cnf, l'index utile au svm, le nom du solver, le nom de l'option, le temps
    else :
        return [cnf,best_option + best_solv * options_len,solver_list[best_solv],options[best_option],best_time]
    
def store_array_in_file(array, filename):
    try:
        with open(filename, 'w') as file:
            file.truncate(0)  # Delete the existing content of the file
            for sub_array in array:
                line = ' '.join(map(str, sub_array)) + '\n'
                file.write(line)
        print("The array has been successfully stored in the file.")
    except IOError:
        print("Error writing to the file.")
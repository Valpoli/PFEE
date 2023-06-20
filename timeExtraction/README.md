# Explication des résultats:

## les résultats sont de la forme:

"nom_du_cnf" "nombre_de_meilleur_solveur" "list_indices_des_meilleurs_solveur" "list_nom_meilleur_solveur" "list_meilleur_option" "meilleur_temps_en_milli_seconde"

"list_nom_meilleur_solveur" et "list_meilleur_option" son mapper : par exemple pour savoir avec quelle option list_nom_meilleur_solveur[i] est la il faut regarder l'option list_meilleur_option[i]

par exemple :
232bac5a9ffa8d764c3f4687bc853784_0ss.cnf 1 [5] ['kissat_inc/sources/'] ['--ultimate'] 80 
232bac5a9ffa8d764c3f4687bc8.cnf 2 [5, 9] ['kissat_inc/sources/', 'ekissat-mab-db-v1/'] ['--ultimate', '--ultimate'] 90 


## list_indice_des_meilleurs_solveur -> chaque indice correspond a un solveur avec une option spécifique,
l'ordre des solveurs/options choisi est le suivant :

["Kissat_MAB-HyWalk/", "kissat_inc/sources/", "ekissat-mab-db-v1/", "Kissat_MAB_MOSS/build/kissat/", "Kissat_MAB_UCB/build/kissat/"]
"", "--ultimate", "--sat --no-options", "--unsat --no-options"

index = numéro_solveur * nombre_option + option

ainsi :
    index 0 = Kissat_MAB-HyWalk/ ""
    index 1 = Kissat_MAB-HyWalk/ "--ultimate"
    index 2 = Kissat_MAB-HyWalk/ "--sat --no-options"
    index 4 = kissat_inc/sources/ ""
    index 9 = ekissat-mab-db-v1/ "--ultimate"
    etc ...
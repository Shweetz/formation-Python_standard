#!/usr/bin/env python 

FILE_PATH = "../../../assets/ministere_culture/frequentation-des-musees-de-france.csv"


def display_max_visites(file_path=FILE_PATH):
    max_visites = 0
    visites_data = None

    with open(file_path) as freq_file:
        freq_file.readline()
        for line in freq_file:
            visites = line[:-1].split(';')[-1]

            if visites and int(visites) > max_visites:
                max_visites = int(visites)
                visites_data = line

    print(visites_data)


def load_as_dicts(file_path=FILE_PATH):
    """
    Extrait les informations sur les musées sous forme d'un dictionnaire.

    :param file_path: Chemin vers le fichier csv de l'OpenData
    :return: un dictionnaire dont la clef est l'identifiant et la valeur une représentation du musée et du comptage.
    :rtype: dict
    """
    museums = {}

    with open(file_path) as freq_file:
        freq_file.readline()
        for line in freq_file:
            museum_id, region, museum_name, city, kind, year, visits \
                = line.split(';')

            try:
                visits = int(visits)
            except ValueError:
                visits = None

            if museum_id not in museums:
                museums[museum_id] = {'region': region,
                                      'museum_name': museum_name,
                                      'city': city,
                                      'id': museum_id,
                                      'visits': []}

            museums[museum_id]['visits'].append([year, visits, kind])

    return museums


if __name__ == "__main__":
    for name in sorted([(element['museum_name'], element['city'], len(element["visits"]))
                        for element in load_as_dicts().values()]):
        print(name)

    last_museum = list(load_as_dicts().values())[-1]

    print("------------------------------")
    print("exemple de comptage")
    print(last_museum["museum_name"], "-", last_museum['city'])
    for year, visits, kind in sorted(last_museum['visits'], key=lambda x: (x[0], x[-1])):
        print("  {:4} - {:>5} ({})".format(year, visits if visits is not None else "--", kind))

    for museum in load_as_dicts().values():
        print("------------------------------")
        print("exemple de comptage")
        print(museum["museum_name"], "-", museum['city'])
        for year, visits, kind in sorted(museum['visits'], key=lambda x: (x[0], x[-1])):
            print("  {:4} - {:>5} ({})".format(year, visits if visits is not None else "--", kind))


import stage.mediatheque as media

file_name = r"../assets/showslist.csv"


# TODO ouvrir fichier et afficher ligne a ligne
# my_file = open(r"../assets/showslist.csv")
# print(my_file.readlines())

with open(file_name) as media_file:
    for line in media_file:
        print(line)

# TODO afficher le fichier sous forme d'une liste
#my_file.seek(0)
#my_list = [line for line in my_file]
#print(my_list)

with open(file_name) as media_file:
    for line in media_file:
        print(line.split(";"))


# TODO récupérer les infos dans leur bon type pour en faire un Episode
#for line in my_list:
#    for title_show, num_sea, num_ep, title_ep, ep_list = line.replace("\n," "").split(";")

# debut

with open(file_name) as media_file:
    syntax = media_file.readline().replace("\n", "").split(";")

    my_list = []
    for line in media_file:
        ep_dict = {}
        for index, data in enumerate(line.replace("\n", "").split(";")):
            ep_dict[syntax[index]] = data

        my_list.append(ep_dict)
        print(ep_dict)

    # print duration of flight or flight
    for episode in my_list:
        if episode["ep_title"] == "Fight or Flight":
            print("ep_number of 'Fight or Flight' = " + episode["ep_number"])

# fin

with open(file_name) as media_file:
    media_file.readline()

    for line in media_file:
        show, season, number, title, *_ = line.split(";")
        print(media.Episode(title, int(number), int(season)))

print("--------")


# TODO générer pour chaque élément un objet de type Episode
def csv_2_episode(file_path):
    with open(file_name) as media_file:
        media_file.readline()

        for line in media_file:
            show, season, number, title, *_ = line.split(";")

            yield media.Episode(title, int(number), int(season))

    print("Fini")


my_gen = csv_2_episode(file_name)

for element in my_gen:
    if element.title == "Pilot":
        print("PILOT STOP")
        break
    print(element)

for element in my_gen:
    print(element)

############



import draft.media.media_db as db

file_name = r"../assets/showslist.csv"

my_db = db.TvShowDao()


def csv_2_episode(file_path):
    with open(file_name) as media_file:
        media_file.readline()

        for line in media_file:
            show, season, number, title, *_ = line.split(";")

            yield title, int(number), int(season)


my_gen = csv_2_episode(file_name)

for title, number, season in my_gen:
    my_db.add_episode(title, number, season)

print(my_db.episodes)

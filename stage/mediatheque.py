
class TvShow:
    def __init__(self, name: str):
        self.name = name
        self._episodes = []

    @property
    def duration(self):
        return len(self._episodes * 25)

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title: str, number: int, season_number: int):
        episode = Episode(title, number, season_number)

        if episode in self._episodes:
            raise ValueError(f"Episode {title} exists")

        self._episodes.append(episode)


class Episode:
    def __init__(self, title: str, number: int, season_number: int):
        self.title = title
        self.number = number
        self.season_number = season_number

    def __eq__(self, other):
        return (self.number, self.season_number) == (other.number, other.season_number)

    def __str__(self):
        return f"Episode {self.title} ({self.season_number}, {self.number})"


class Movie:
    def __init__(self, title: str):
        self.title = title


def display_title(media):
    print(media.title)


class MyException(Exception):
    pass


# n'exécute le code que si on exécute le fichier et non si on l'importe
if __name__ == "__main__":
    display_title(Episode("The Book", 2, 1))
    display_title(Movie("Moi moche mechant"))

    # affiche "stage.mediatheque" si code exécuté depuis un import
    print(__name__)
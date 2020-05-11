from stage import mediatheque as media
import pytest


def test_show_creation_correct_name():
    my_show = media.TvShow("GoT")
    # print(my_show.name)
    assert my_show.name == "GoT"


def test_correct_addition_of_episode():
    my_show = media.TvShow("GoT")
    my_show.add_episode("Pilote", 1, 1)
    # print(len(my_show.episodes))
    assert len(my_show.episodes) == 1


"""def test_duplicate_episode_should_rise_exception():
    my_show = media.TvShow("GoT")
    my_show.add_episode("Pilote", 1, 1)

    with pytest.raises(ValueError):
        my_show.add_episode("Pilote", 2, 3)"""


def test_duplicate_number_should_rise_exception():
    my_show = media.TvShow("GoT")
    my_show.add_episode("Pilote", 1, 1)

    with pytest.raises(ValueError):
        my_show.add_episode("Outro", 1, 1)

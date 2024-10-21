from app import process_query


def test_knows_about_dinosaurs():
    test_str = "Dinosaurs ruled the Earth 200 million years ago"
    assert process_query("dinosaurs") == test_str


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"

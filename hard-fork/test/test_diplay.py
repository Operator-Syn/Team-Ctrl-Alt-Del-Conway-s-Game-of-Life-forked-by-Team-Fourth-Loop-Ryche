import os
from src.display import clear_screen, print_grid


def test_clear_screen(monkeypatch):
    commands_executed = []  # record executed commands

    def mock_system(command):
        commands_executed.append(command)  # record the command instead of executing it

    monkeypatch.setattr("os.system", mock_system)  # replace os.system with our mock
    clear_screen()
    expected_command = "cls" if os.name == "nt" else "clear"
    assert commands_executed == [expected_command]


def test_print_grid(monkeypatch, capsys):
    commands_executed = []

    def mock_clear_screen():
        commands_executed.append("clear_screen_called")

    monkeypatch.setattr("src.display.clear_screen", mock_clear_screen)

    grid = ("""\
            ...
            .*.
            ...""")
    generation = 5
    print_grid(grid, generation=generation)

    captured = capsys.readouterr()
    expected_output = "Generation: 5\
                            ...\
                            ...\
                            ..."

    assert commands_executed == ["clear_screen_called"]
    assert captured.out == expected_output

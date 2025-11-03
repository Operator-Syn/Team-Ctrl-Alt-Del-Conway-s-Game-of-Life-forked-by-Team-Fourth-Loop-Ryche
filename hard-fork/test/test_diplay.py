import os
import textwrap
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
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    
    generation = 5
    print_grid(grid, generation=generation)

    captured = capsys.readouterr()  
    expected_output = textwrap.dedent(f"""\
                                    Generation: {generation}
                                    ...
                                    .*.
                                    ...
                                    """)
    assert commands_executed == ["clear_screen_called"]
    assert captured.out == expected_output

def test_print_grid_no_generation(monkeypatch, capsys):
    commands_executed = []

    def mock_clear_screen():
        commands_executed.append("clear_screen_called")

    monkeypatch.setattr("src.display.clear_screen", mock_clear_screen)
    grid = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 0],
    ]
    
    print_grid(grid)

    captured = capsys.readouterr()  
    expected_output = textwrap.dedent("""\
                                    *.*
                                    .*.
                                    **.
                                    """)
    assert commands_executed == ["clear_screen_called"]
    assert captured.out == expected_output

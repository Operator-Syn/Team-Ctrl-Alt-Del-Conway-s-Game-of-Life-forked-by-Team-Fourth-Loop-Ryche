import os
from src.display import clear_screen


def test_clear_screen(monkeypatch):
    commands_executed = [] #record executed commands

    def mock_system(command):
        commands_executed.append(command) #record the command instead of executing it

    monkeypatch.setattr("os.system", mock_system) #replace os.system with our mock
    clear_screen()
    expected_command = "cls" if os.name == "nt" else "clear"
    assert commands_executed == [expected_command]



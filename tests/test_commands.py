from app import CommandHandler
from unittest.mock import patch


def test_add_command(capsys):

    handler = CommandHandler()
    handler.register_command("add", AddCommand())

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["5", "3"]

        handler.execute_command("add")
        stdout, stderr = capsys.readouterr()
        assert "Enter first number:" in stdout
        assert "Enter second number:" in stdout
        assert "Result: 8" in stdout      

def test_subtract_command(capsys):

    handler = CommandHandler()
    handler.register_command("subtract", SubtractCommand())

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["5", "3"]

        handler.execute_command("subtract")
        stdout, stderr = capsys.readouterr()
        assert "Enter first number:" in stdout
        assert "Enter second number:" in stdout
        assert "Result: 2" in stdout 

def test_multiply_command(capsys):

    handler = CommandHandler()
    handler.register_command("multiply", MultiplyCommand())

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["5", "3"]

        handler.execute_command("multiply")
        stdout, stderr = capsys.readouterr()
        assert "Enter first number:" in stdout
        assert "Enter second number:" in stdout
        assert "Result: 15" in stdout 

def test_divide_command(capsys):

    handler = CommandHandler()
    handler.register_command("divide", DivideCommand())

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["5", "3"]

        handler.execute_command("divide")
        stdout, stderr = capsys.readouterr()
        assert "Enter first number:" in stdout
        assert "Enter second number:" in stdout
        assert "Result: 1.666666666666666666666666667" in stdout 

def test_exit_command(capsys):
        with patch('sys.exit') as mock_exit:
            handler = CommandHandler()
            handler.register_command("exit", ExitCommand())
            mock_input = patch("builtins.input", return_value="exit")
            with mock_input:
                handler.execute_command("exit")

            mock_exit.assert_called_once_with("Exiting")

def test_menu_command(capsys):

    handler = CommandHandler()
    handler.register_command("menu", MenuCommand(handler))

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = ["menu"]

        handler.execute_command("menu")
        stdout, stderr = capsys.readouterr()
        assert "Available commands:\nmenu\n" in stdout 


#Leave this file alone
import mock
import averages
def test_averages(capsys):
    with mock.patch('builtins.input', side_effect=[1, 2, 3, 'bad data', 'done']):
        averages.averages()
        captured = capsys.readouterr()
        statements = captured.out.split("\n")
        final_result = statements[-2]
        assert final_result == "6 3 3 1"
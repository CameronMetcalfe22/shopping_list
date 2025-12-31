from shopping_list.cli import main


def test_smoke(capsys):
    main()
    captured = capsys.readouterr()
    assert "it works" in captured.out

from pathlib import Path

print(Path().home()/'Documents')
print(f'{Path().home()}/Documents')
Path(f'{Path().home()}/Documents/keywords/').touch(exist_ok=True)

print("".join(['\n', '2023-03-15\n', '\n', 'Крысы не дают покоя полосатым кошкам\n']))
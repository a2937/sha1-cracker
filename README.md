# Sha1-cracker

Sha1-cracker is a command-line tool that gives
the user to crack a provided hash. It is written in Python.

## Installation

Place `main.py` and `password_cracker.py` in the current working directory,
along with the data files `known-salts.txt` and `top-100000-passwords.txt`.
Your own salts and password content files may be provided but they must 
have the given names and it must be one value per line. 

## Usage

`python main.py`

## Testing

`python -m unittest test_module`

## Contributing

Please open an issue to discuss improvements to this software. 

## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

# Ell Adventure

![Ell Adventure](./banner.png)

Ell Adventure is an innovative text-based adventure game that leverages the power of Large Language Models (LLMs) and the ell framework to create dynamic, personalized gaming experiences.

## Features

- Dynamic narrative adaptation based on player choices
- Customizable game worlds using player-provided novels or custom descriptions
- Persistent game state across sessions
- Modular design for easy expansion and modification

## Technologies Used

- [ell Framework](https://docs.ell.so/): Core system for defining and managing the planner, tools, and agents
- [ChromaDB](https://docs.trychroma.com/): Persistent data storage and retrieval
- [Textual](https://textual.textualize.io/): Text-based user interface
- [Python 3.12+](https://www.python.org/): Programming language

## Installation

1. Ensure you have Python 3.12+ installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/Nitewriter/ell-adventure.git
   cd ell-adventure
   ```
3. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```
4. Install the project dependencies:
   ```bash
   poetry install
   ```

## Usage

To start the adventure:

```bash
poetry run adventure
```

## Development

We use a Makefile to simplify common development tasks. Here are some useful commands:

### Setup

To set up the virtual environment and install dependencies:

```bash
make
```

### Linting

To run the linter (ruff):

```bash
make lint
```

### Testing

To run the test suite:

```bash
make test
```

### Formatting

To format the code and sort the pyproject.toml file:

```bash
make format
```

### Check

To run both linting and formatting checks:

```bash
make check
```

### Cleaning

To clean up generated files and caches:

```bash
make clean
```

### Updating Dependencies

To update project dependencies:

```bash
make update-deps
```

## Project Structure

- `src/`: Source code for the game
  - `tools/`: Modular tools for game mechanics
  - `agents/`: Dynamic agent definitions
  - `ui/`: Textual UI components
- `tests/`: Test suite
- `docs/`: Additional documentation
  - `system-design.md`: Detailed system design document

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The ell team for their powerful LMP framework
- The ChromaDB team for their efficient vector database
- The Textual team for their excellent TUI library

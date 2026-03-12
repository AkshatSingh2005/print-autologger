# print-autologger

Automatically log all `print()` output from your Python program to a file, with almost no changes to existing code.

Once initialized, every `print()` call is written to a timestamped log file.

---

## Features

- Drop‑in: add one setup call, keep using `print()`.
- Logs to a file using the standard `logging` module.
- Creates the log directory automatically.
- Configurable log directory, file name, logger name, and level.
- No external dependencies.

---

## Installation

```bash
pip install print-autologger
```

Upgrade:

```bash
pip install --upgrade print-autologger
```

---

## Quick Start

```python
from autologger import setup_autologger

# Call once at the start of your program
setup_autologger()

print("Hello world!")
print("Some value:", 42)
```

After running, you’ll get:

```text
experiment/
  experiment_logs/
    experiment_log.txt
```

Example log content:

```text
2026-03-12 10:30:01,234 - Hello world!
2026-03-12 10:30:01,235 - Some value: 42
```

---

## Configuration

```python
from autologger import setup_autologger
import logging

logger = setup_autologger(
    log_dir="experiment/experiment_logs",   # folder for logs
    log_file_name="experiment_log.txt",     # log file name
    logger_name="experiment_logger",        # logger name
    level=logging.INFO                      # logging level
)
```

You can still use the returned `logger`:

```python
logger.info("Logged with logger.info()")
print("Logged with print()")
```

---

## How It Works

- Creates `log_dir` if it doesn’t exist.
- Configures a `logging.Logger` with a `FileHandler`.
- Replaces `sys.stdout` with a wrapper that forwards `print()` output to the logger.

Any `print()` after `setup_autologger()` is logged.

---

## Limitations

- Intended mainly for scripts / CLI programs.
- Must be called before the prints you want to capture.
- Uses a single log file (no rotation yet).

---
## Contributing
Contributions, ideas, and bug reports are very welcome!

- ⭐ Star this repository if you like the project.
- 🐛 Open an issue for bugs or feature requests.
- 🔧 Open a pull request to add improvements or new features.

---

## Development

```bash
git clone https://github.com/AkshatSingh2005/print-autologger.git
cd print-autologger
pip install -e .
python example.py
```
---

## License

MIT
```

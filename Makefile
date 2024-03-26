# Variables
PYTHON_INTERPRETER = python3
MAIN_FILE = onlinefood.py
TEST_FILE = test.py
REQUIREMENTS_FILE = requirements.txt

# Targets
.PHONY: help clean lint test run

help:
	@echo "Available targets:"
	@echo "  help       - Show this help message"
	@echo "  clean      - Remove generated files"
	@echo "  lint       - Run linting checks"
	@echo "  test       - Run unit tests"
	@echo "  run        - Run the main script"

clean:
	find . -type f -name '*.pyc' -delete
	rm -rf __pycache__ .pytest_cache

lint:
	$(PYTHON_INTERPRETER) -m flake8 $(MAIN_FILE) $(TEST_FILE)

test:
	$(PYTHON_INTERPRETER) -m unittest discover -s . -p $(TEST_FILE)

run:
	$(PYTHON_INTERPRETER) $(MAIN_FILE)


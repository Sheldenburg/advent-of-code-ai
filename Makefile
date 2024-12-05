# Read the config file
CONFIG_FILE=config.ini

Year=$(shell awk -F' *= *' '/^Year/ {print $$2}' $(CONFIG_FILE))
Day=$(shell awk -F' *= *' '/^Day/ {print $$2}' $(CONFIG_FILE))
Part1=$(shell awk -F' *= *' '/^Part1/ {print $$2}' $(CONFIG_FILE))

# Set the environment variable 'Part1' to be True
export Part1=True

.PHONY: part1 part2

part1:
	python main.py; \
	python day_${Day}_${Year}.py

part2:
	@export Part1=False; \
	python main.py; \
	python day_${Day}_${Year}.py

all: part1
	@read -p "Do you want to proceed to part 2? (yes/no): " proceed; \
	if [ "$$proceed" = "yes" ]; then \
		$(MAKE) part2; \
	fi

# Makefile for compiling and running Java program

# Directories
SRC_DIR := src
BIN_DIR := bin

# List of Java source files
JAVA_SOURCES := $(wildcard $(SRC_DIR)/barScheduling/*.java)

# Compiler and flags
JC := javac
JFLAGS := -d $(BIN_DIR)

# Run command
JAVA := java
MAIN_CLASS := barScheduling.SchedulingSimulation

.PHONY: all clean run

all: $(JAVA_SOURCES)
	$(JC) $(JFLAGS) $(JAVA_SOURCES)

run: all
	$(JAVA) -cp $(BIN_DIR) $(MAIN_CLASS) $(ARGS)

clean:
	rm -rf $(BIN_DIR)

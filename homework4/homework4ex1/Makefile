# vim: noet
#
SRC_DIR := src
BUILD_DIR := build

all: $(BUILD_DIR)
	cd $(BUILD_DIR) && ghc -o h4 -hidir . -odir . ../$(SRC_DIR)/Main.hs ../$(SRC_DIR)/Functions.hs

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all clean

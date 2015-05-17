SHELL := /bin/sh
PROTOC := protoc
PYTHON := /usr/bin/python3
BASE_DIR := $(realpath $(dir $(lastword $(MAKEFILE_LIST))))
PROTO_DIR := $(BASE_DIR)/proto
PROTO_FLAT_DIR := $(BASE_DIR)/proto-flat
PYTHON_TMP := $(BASE_DIR)/_python-generated
PYTHON_OUT := $(BASE_DIR)/python/hsproto
PYTHON_FIX_BIN := $(BASE_DIR)/python/relativize_module.py
GO_OUT := $(BASE_DIR)/go


all: python go

python_clean:
	test -d "$(PYTHON_TMP)" && rm -rf "$(PYTHON_TMP)" || exit 0
	test -d "$(PYTHON_OUT)" && rm -rf "$(PYTHON_OUT)" || exit 0

python: python_clean
	mkdir -p "$(PYTHON_TMP)"
	find "$(PROTO_DIR)" -type f -name '*.proto' -exec $(PROTOC) --proto_path="$(PROTO_DIR)" --python_out="$(PYTHON_TMP)" {} \;
	find "$(PYTHON_TMP)" -type f -name '*.py' -exec $(PYTHON) "$(PYTHON_FIX_BIN)" "$(PYTHON_TMP)" {} \;
	mv "$(PYTHON_TMP)" "$(PYTHON_OUT)"

go_clean:
	test -d "$(GO_OUT)" && rm -rf "$(GO_OUT)" || exit 0

go: go_clean
	mkdir -p "$(GO_OUT)"
	find "$(PROTO_FLAT_DIR)" -type f -name '*.proto' -exec $(PROTOC) --proto_path="$(PROTO_FLAT_DIR)" --go_out="$(GO_OUT)" {} \;

clean: python_clean go_clean

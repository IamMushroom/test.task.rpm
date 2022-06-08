include .env

GOBASE := $(shell pwd)
GOPATH := $(GOBASE)/vendor:$(GOBASE)
GOBIN := $(GOBASE)/bin
GOSRC := $(GOBASE)/src
GOFILE := $(GOSRC)/main.go
INSTALLPATH := /usr/bin

MAKEFLAGS += --silent

copy:
	@echo "  >  Install app"
	@cp $(GOBIN)/$(PROJECTNAME) $(INSTALLPATH)

compile: clean build
build:
	@echo "  >  Building binary"
	@GOPATH=$(GOPATH) GOBIN=$(GOBIN) go build -o $(GOBIN)/$(PROJECTNAME) $(GOFILE)
clean:
	@echo "  >  Cleaning build cache"
	@GOPATH=$(GOPATH) GOBIN=$(GOBIN) go clean

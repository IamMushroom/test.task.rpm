include .env

GOBASE := $(shell pwd)
GOPATH := $(GOBASE)/vendor:$(GOBASE)
GOBIN := $(GOBASE)/bin
GOSRC := $(GOBASE)/src
GOFILE := $(GOSRC)/main.go

LDFLAGS += --build-id

copy:
	@echo "  >  Install app into $(INSTALLPATH)"
	@install -Dpm 0755 $(GOBIN)/$(PROJECTNAME) $(INSTALLPATH)/$(PROJECTNAME)

compile: clean build
build:
	@echo "  >  Building binary"
	@GOPATH=$(GOPATH) GOBIN=$(GOBIN) go build -o $(GOBIN)/$(PROJECTNAME) $(GOFILE)
clean:
	@echo "  >  Cleaning build cache"
	@GOPATH=$(GOPATH) GOBIN=$(GOBIN) go clean

remove:
	@rm -f $(INSTALLPATH)/$(PROJECTNAME)

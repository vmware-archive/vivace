#
# Copyright VMware, Inc 2015
#
VVC_SRCROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


# build dir (stage/* output)
PHOTON_STAGE := $(VVC_SRCROOT)stage

# specs dir to use
PHOTON_SPECS_DIR := $(VVC_SRCROOT)SPECS

# Sources pulling
PHOTON_SOURCES := sources sources-vivace
VIVACE_BINTRAY_CONFIG := $(VVC_SRCROOT)support/pullsources/bintray.conf
VIVACE_SOURCES_LIST := $(VVC_SRCROOT)support/pullsources/sources_list.sha1

# package list to build
PHOTON_PACKAGE_LIST := $(VVC_SRCROOT)support/package-builder/input.json

# package list to create iso
PHOTON_INSTALLER_PACKAGE_LIST := $(VVC_SRCROOT)installer/package_list.json

PHOTON_DATA_DIR := $(VVC_SRCROOT)common/data

THREADS=4

$(VVC_SRCROOT)/photon/Makefile: ;

include $(VVC_SRCROOT)/photon/Makefile

sources-vivace:
	@echo "Pulling sources from bintray vivace..."
	@$(MKDIR) -p $(PHOTON_SRCS_DIR) && \
	 cd $(PHOTON_PULL_SOURCES_DIR) && \
	 $(PHOTON_PULL_SOURCES) -c $(VIVACE_BINTRAY_CONFIG) -s $(VIVACE_SOURCES_LIST) $(PHOTON_SRCS_DIR)

sha1:
	$(eval SHA1_TOTAL = $(shell mktemp))
	@cd $(PHOTON_SRCS_DIR) && \
		sha1sum * | awk '{print $$2" - "$$1}' > $(SHA1_TOTAL)
	@comm $(SHA1_TOTAL) $(PHOTON_SOURCES_LIST) -2 -3 > $(VIVACE_SOURCES_LIST)
	@rm -f $(SHA1_TOTAL)


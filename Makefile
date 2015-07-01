#
# Copyright VMware, Inc 2015
#
VVC_SRCROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


# build dir (stage/* output)
PHOTON_STAGE := $(VVC_SRCROOT)stage

# specs dir to use
PHOTON_SPECS_DIR := $(VVC_SRCROOT)SPECS

# Sources pulling
PHOTON_BINTRAY_CONFIG := $(VVC_SRCROOT)support/pullsources/bintray.conf
PHOTON_SOURCES_LIST := $(VVC_SRCROOT)support/pullsources/sources_list.sha1

# package list to build
PHOTON_PACKAGE_LIST := $(VVC_SRCROOT)support/package-builder/input.json

# package list to create iso
PHOTON_INSTALLER_PACKAGE_LIST := $(VVC_SRCROOT)installer/package_list.json

PHOTON_DATA_DIR := $(VVC_SRCROOT)common/data

$(VVC_SRCROOT)/photon/Makefile: ;

include $(VVC_SRCROOT)/photon/Makefile


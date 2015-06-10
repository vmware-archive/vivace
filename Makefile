#
# Copyright VMware, Inc 2015
#
VVC_SRCROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


# build dir (stage/* output)
PHOTON_STAGE := $(VVC_SRCROOT)stage

# specs dir to use
PHOTON_SPECS_DIR := $(VVC_SRCROOT)SPECS

# bintray config for sources pulling
PHOTON_BINTRAY_CONFIG := $(VVC_SRCROOT)support/pullsources/bintray.conf

# package list to create iso
PHOTON_INSTALLER_PACKAGE_LIST := $(VVC_SRCROOT)installer/package_list.json


$(VVC_SRCROOT)/photon/Makefile: ;

include $(VVC_SRCROOT)/photon/Makefile


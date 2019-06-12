#
# Copyright VMware, Inc 2015
#
VVC_SRCROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


# build dir (stage/* output)
PHOTON_STAGE := $(VVC_SRCROOT)stage

# specs dir to use
PHOTON_SPECS_DIR := $(VVC_SRCROOT)SPECS

# Sources pulling
#PHOTON_BINTRAY_CONFIG := $(VVC_SRCROOT)photon/support/package-builder/bintray.conf:$(VVC_SRCROOT)support/package-builder/pullsources.conf
PHOTON_PULLSOURCES_CONFIG := $(VVC_SRCROOT)photon/support/package-builder/bintray.conf:$(VVC_SRCROOT)support/package-builder/pullsources.conf
#PHOTON_PULLSOURCES_CONFIG=$(VVC_SRCROOT)support/package-builder/pullsources.conf

#THREADS=4

$(VVC_SRCROOT)photon/Makefile: 
	@:

$(VVC_SRCROOT)photon/common/data/packages_minimal.json: ;

include $(VVC_SRCROOT)photon/Makefile


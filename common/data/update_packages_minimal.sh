#! /bin/sh

cp -L packages_minimal.json packages_minimal2.json
sed -i 's/photon-release/vivace-release/g;s/open-vm-tools/open-vm-tools-vivace/g' packages_minimal2.json


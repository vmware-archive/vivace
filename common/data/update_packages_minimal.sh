#! /bin/sh

cp -L packages_minimal.json packages_minimal2.json
sed -i 's/photon-release/vivace-release/g;s/"open-vm-tools",//g' packages_minimal2.json
sed -i 's/]/, "linux-drivers-gpu", "linux-sound" ]/g' packages_minimal2.json


#!/bin/bash
cd SAND
pelican content -t ../martin-sand
read -n 1 -s -r -p "Press any key to continue..."

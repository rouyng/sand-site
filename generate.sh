#!/bin/bash
cd SAND
python3 -m pelican content -t ../martin-sand
read -n 1 -s -r -p "Press any key to continue..."

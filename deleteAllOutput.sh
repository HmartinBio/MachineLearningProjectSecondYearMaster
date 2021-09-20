#!/bin/bash

## Changing folder to output folder

cd "output"

## Deleting all the files in the output folder

ls -F | grep -Ev "/$" | xargs -i -t rm {}

## Going to 2264GenesDataframe folder and deleting dataframe file inside 

cd "2264GenesDataframe" && ls | xargs -i -t rm {}

cd ".."

## Going to 399GenesDataframe folder and deleting dataframe file inside

cd "399GenesDataframe" && ls | xargs -i -t rm {}

cd "../.."

## Moving to figures folder and deleting all the figures inside

cd "figures" && ls | xargs -i -t rm {}

exit $?


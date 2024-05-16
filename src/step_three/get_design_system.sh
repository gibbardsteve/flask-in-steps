#! /bin/sh

set -e

TMPFILE=`mktemp ./templates.XXXXXXXXXX`

wget https://github.com/ONSdigital/design-system/releases/download/70.0.4/templates.zip -O $TMPFILE
rm -rf ds/templates/components
rm -rf ds/templates/layout

unzip -d ./ds $TMPFILE
rm $TMPFILE

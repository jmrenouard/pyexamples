#!/bin/bash

OUTPUT_DIR="./out"
TEMPLATE_DIR="./templates"
DATA_DIR="./data"

for tmpl in ${TEMPLATE_DIR}/*; do
	item=$(basename "${tmpl%.*}")
	echo "-----------------------------------------------"
	echo "GENERATING $OUTPUT_DIR/${item}.html"
	echo "TEMPLATE: $tmpl"
	echo "DATA: $DATA_DIR/${item}.yaml"
	echo "-----------------------------------------------"

	if [ -f "$DATA_DIR/${item}.json" ]; then
		echo "** GENERATION FROM JSON...."
		jinja2 $tmpl $DATA_DIR/${item}.json --format=json > $OUTPUT_DIR/${item}.html
		exit $?
	fi
	export LC_ALL='en_US.utf8'
	if [ -f "$DATA_DIR/${item}.yaml" ]; then
		echo "** VALIDATION FROM YAML DATA: ${item}.yaml"
		python -c "from yaml import load, Loader; load(open('$DATA_DIR/${item}.yaml'), 
Loader=Loader)"
		if [ $? -ne 0 ];then
			echo "[ERROR] VALIDATION FAILED FOR ${item}.yaml"
			exit 2
		fi
			echo "[INFO] VALIDATION OK FOR ${item}.yaml"
		echo "** GENERATION FROM YAML...."
		jinja2 $tmpl $DATA_DIR/${item}.yaml --format=yaml > $OUTPUT_DIR/${item}.html
		RC=$?
		ls -ls $OUTPUT_DIR
		exit $RC
	fi
	echo "* MISSING SOME TEMPLATE"
	ls -ls $TEMPLATE_DIR
	echo "* MISSING SOME DATA"
	ls -ls $DATA_DIR
	
	exit 1
done 

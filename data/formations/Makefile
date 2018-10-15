.DEFAULT_GOAL := echo
serve: stop
	(cd ./out;python3 -m http.server &)

stop:
	killall python3 || true

generate:
	rm -f out/*
	sh generate.sh
	cp -R res/* out/
list:
	ls -ls ./out ./data ./templates		
echo:
	echo "Default nothing action"
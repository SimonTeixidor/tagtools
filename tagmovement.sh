#!/bin/bash

to_roman() {
	case "$1" in
		1) 
			echo I
			;;
		2) 
			echo II
			;;
		3) 
			echo III
			;;
		4) 
			echo IV
			;;
		5) 
			echo V
			;;
		6) 
			echo VI
			;;
		7) 
			echo VII
			;;
		8) 
			echo VIII
			;;
		9) 
			echo IX
			;;
		10) 
			echo X
			;;
		11) 
			echo XI
			;;
		12) 
			echo XII
			;;
		13) 
			echo XIII
			;;
		14) 
			echo XIV
			;;
		15) 
			echo XV
			;;
		16) 
			echo XVI
			;;
		17) 
			echo XVII
			;;
		18) 
			echo XVIII
			;;
		19) 
			echo XIX
			;;
		20) 
			echo XX
			;;
	esac
}

TMPFILE=`mktemp /tmp/tagmovement.XXXXXX`
work=0
i=0
for f in "$@"; do
	old_work="$work"
	work="$(metaflac --show-tag=WORK "$f")"
	if [ "$old_work" = "$work" ]; then
		i=$((1+i))
	else
		i=1
	fi
	if [ -n "$work" ]; then
		echo "$(to_roman $i)|$f" >> "$TMPFILE"
	fi
done
vim "$TMPFILE"
while read line; do
	FILE=`echo "$line" | rev | cut -d'|' -f1 | rev`
	MOVEMENT=`echo "$line" | rev | cut -d'|' -f2- | rev`
	metaflac --set-tag="MOVEMENT=$MOVEMENT" "$FILE"
done < $TMPFILE

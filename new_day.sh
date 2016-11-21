#!/usr/bin/env bash
# Create a new directory for a new day of the adventofcode

echo "What date are you going to solve today?"
read day

if [ $day -le 9 ] ; then
    DAYNAME=day0$day
else
    DAYNAME=day$day
fi

if [ -d $DAYNAME ] ; then
    echo "Directory $DAYNAME exists!"
    exit 1
fi

mkdir $DAYNAME
cd $DAYNAME
cat <<EOF > ${DAYNAME}.py 
#!/usr/bin/env python3

"""Day ${day}: ."""

import re

INPUT_FILE = "${DAYNAME}_input.txt"

with open(INPUT_FILE, 'r') as f:
    for line in f:
        pattern = '^.*$'
        result = re.match(pattern, line)
        print(result.groups())

EOF

touch ${DAYNAME}_input.txt

vi -p ${DAYNAME}_input.txt ${DAYNAME}.py 

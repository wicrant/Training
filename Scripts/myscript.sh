echo Hello World
NAME="Vikrant"
#echo "My name is $NAME"
#read -p "Enter your name: " NAME
#echo "hello $NAME, nice to meet you"
if [ "$NAME" == "Vikrant" ]
then
	echo "Your name is Vikrant"
else
	echo "Your name is not Vikrant"
fi

NUM1=31
NUM2=5
if [ "$NUM1" -gt "$NUM2" ]
then
	echo "$NUM1 is greater than $NUM2"
else
	echo "$NUM1 is less than $NUM2"
fi
FILE="test.txt"
if [ -f "$FILE" ]
then
	echo "$FILE is a file"
else	
	echo "$FILE is not a file"
fi

#read -p "are you 21 or over? Y/N " ANSWER
#case "$ANSWER" in
#	[yY] | [yY][eE][sS])
#		echo "you can have a beer :)"
#		;;
#	[nN] | [nN][oO])
#		echo "sorry"
#		;;
#	*)
#		echo "Please enter y/yes or n/no"
#		;;
#esac
NAMES="Vikrant Harshada Anu Tanu"
for NAME in $NAMES
	do
		echo "hello $NAME"
done 
#FILES=$(ls *.txt)
#NEW="new"
#for FILE in $FILES
#	do
#		echo "Renaming $FILE to new-$FILE"
#		mv $FILE $NEW-$FILE
#done
LINE=1
while read -r CURRENT_LINE
	do
		echo "$LINE: $CURRENT_LINE"
		((LINE++))
done < "./1.txt"
#function
function sayHello() {
	echo "hello world"
}
sayHello

function greet() {
	echo "Hello, I am $1 and I am $2"
}
greet "Vikrant" "40"

# create folder and write to a file
mkdir hello
touch "hello/world.txt"
echo "Hello World" > "hello/world.txt"
echo "Create hello/world.txt"
DATE=$(date)
echo "Today is $DATE"
echo "it is $(date "+%d/%m/%Y")"
CURDIR=$(pwd)
echo "Current Directory = $(pwd)"
echo "Current User = $(whoami)"
echo -e  "Files are \n $(ls -lah)"

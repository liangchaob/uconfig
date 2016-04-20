echo "输入操作系统名(空格以'-'代替):"
read SYSTEMNAME

mkdir "$SYSTEMNAME"
mkdir "$SYSTEMNAME/user"
mkdir "$SYSTEMNAME/network"
mkdir "$SYSTEMNAME/system"
mkdir "$SYSTEMNAME/software"
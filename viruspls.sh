path=$(pwd)
h=1
j=0
for i in $(seq 1 1 10)
do
d=$(($h+$j))
h=$j
j=$d
path="$path/$d"
mkdir $path
done
ls / -la>$path/root.txt
ls ~ -la>$path/home.txt
echo "javier felix alonso lopez">$path/javieralonso.txt

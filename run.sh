a='2000'
n=$1+1
for (( i=3; i<=$n; i++ ))
do
	a="${a} ${i}000"
done
echo "${a}"
for (( i=2; i<=$n; i++ ))
do
	echo "Opening port ${i}000"
	gnome-terminal -e "python3 peer.py ${i}000 ${a}"
done

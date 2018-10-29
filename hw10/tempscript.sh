temp1=`i2cget -y 2 0x4A`
temp2out=$(($temp1*9/5 + 32))
echo $temp2out

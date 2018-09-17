temp=`i2cget -y 2 0x48`
temp1=`i2cget -y 2 0x4A`
tempout=$(($temp*9/5 + 32))
temp2out=$(($temp1*9/5 + 32))

echo Temp1 is $tempout
echo Temp2 is $temp2out

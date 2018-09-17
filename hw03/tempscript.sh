temp = `i2cget -y 1 0x48`
temp1 = `i2cget -y 1 0x4A`
tempout = $(($temp*1.8 + 32))
temp2out = $(($temp*1.8 + 32))

echo tempout
echo temp2out

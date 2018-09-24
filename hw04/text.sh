# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'My name is Anne Boxeth' \
      -draw "text 0,100 'This is for Embedded Linux'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font

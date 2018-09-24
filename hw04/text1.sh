# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/temppic.png

# From: http://www.imagemagick.org/Usage/text/
convert boris.png -undercolor white -font Times-Roman -pointsize 24 \
      -resize 35% \
      -draw "text 0,200 'This is Boris'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font


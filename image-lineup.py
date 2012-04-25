import ImageFile, Image
import os, sys, re

infile = sys.argv[1]

first_frame = Image.open(infile)
print ("\n---------------------------")
print "\neach frame is sized width: %i, height: %i"  % first_frame.size

image_width = first_frame.size[0]
image_height = first_frame.size[1]

base_name, e = os.path.splitext(infile)

#print base_name
frames = sys.argv[2]

dirname = os.path.dirname(base_name)

print "the directory we're working in: " + dirname

file_name = base_name.split(os.sep)

file_name_pos = len(file_name) - 1
file_name = file_name[file_name_pos]

file_base = re.search('\D+', file_name)

print "the base name of this is: " + file_base.group(0)
sequence_name = file_base.group(0)

new_width = image_width * int(frames)

comb_image = Image.new("RGBA", (new_width, image_height))

for i in range(0, int(frames)):
    if i < 10:
        framefile = dirname + "/" + file_base.group(0) + "0000" + str(i) + e
    elif i >= 10 and i < 100:
        framefile = dirname + "/" + file_base.group(0) + "000" + str(i) + e
    elif i >= 100 and i < 1000:
        framefile = dirname + "/" + file_base.group(0) + "00" + str(i) + e
    elif i >= 1000:
        framefile = dirname + "/" + file_base.group(0) + "0" + str(i) + e

    tmp_image = Image.open(framefile)
    x_coord = image_width * i
    #print "%i - %s" % (i, framefile)
    comb_image.paste(tmp_image, (image_width * i,0))


final_image_name = dirname + "/" + sequence_name + "seq.png"
comb_image.save(final_image_name, "PNG")

print("\n\n\n----> YAY! It's complete!")
print("filename: %s.png" % sequence_name)
print("new file dimensions width: %i, height: %i" % (image_width * i, image_height))
print ("\n---------------------------\n")

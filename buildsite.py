import shutil
import os

# Make the basic directory, if you need to.
if os.path.isdir('PianoStudio/'):
    shutil.rmtree('PianoStudio/')
else:
	os.mkdir('PianoStudio/')

# Copy both the content and picture directories into a resources directory.
import distutils.dir_util
distutils.dir_util.copy_tree('content', 'PianoStudio/resources/content/')
distutils.dir_util.copy_tree('pictures', 'PianoStudio/resources/pictures/')

# This list of files is needed in the root of the site. Copy them all.
copy_files = ('header.php', 'body.php', 'footer.php', 'piano.css', 'gallery.js',
              'headerfunction.php', 'index.php', 'piano.jpg', 'favicon.ico', '/home/blaine/Business/PianoStudio/Management/PolicyandPhilosophy.pdf')
for copy_file in copy_files:
    shutil.copy(copy_file, 'PianoStudio/')

# Pull open the configuration file
mystring = open('config.txt', 'r').read()

# And split it apart.
import string
lines = mystring.split('\n')

# Each content file has three different names that correlate to:
directory_names = []    # The directory it's stored in, and therefore what it's URL appears as.
nav_names = []          # What the link pointing to it says.
file_names = []         # What the file is actually called.
# Using a delimiter of ';', split apart the config lines and direct each to it's proper array.
for line in lines:
    words = line.split(';')

    directory_names.append(words[0])
    nav_names.append(words[1])
    file_names.append(words[2])

# A debug line, prints the directories as they end up after config splitting.
print(directory_names, nav_names, file_names)

# Build all the files and stick them in the right places.
nav_string = '<?php ?><div id="navigation" class="area"><div class="firstline block">Site Sections</div>'
i = 0
while i < len(directory_names):
    os.mkdir('PianoStudio/' + directory_names[i] +'/')
    nav_string += '<a href="../'+ directory_names[i] +'"><div class="link block"><p>'+ nav_names[i] +'</p></div></a>'
    open('PianoStudio/'+ directory_names[i] +'/index.php', 'w').write("""<?php
            include('../header.php');
            include('../body.php');
            body('"""+ file_names[i] +"""');
            include('../nav.php');
            include('../footer.php'); ?>""")
    i += 1
nav_string += '</div><?php ?>'
open('PianoStudio/nav.php', 'w').write(nav_string)

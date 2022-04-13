
# dict to classify file extentions into categories
file_extension_dict = {
    "webp" : 0, 
    "exe" : 0,
    "zip" : 0,
    "egg" : 0,
    "msi" : 0,
    "torrent" : 0,
    
    "pdf" : 1,
    "xlsx" : 1,
    "docx" : 1,
    "txt" : 1,

    "jpg" : 2,
    "png" : 2,

    "py" : 3,

    "mp4" : 4,
    "mkv" : 4,

    "mp3" : 5,
    "wav" : 5,

    "lnk" : 6,

    "folder" : 7
}

"""
0 - extension_delete # file extensions to be deleted with no consideration
1 - extension_doc
2 - extension_pic
3 - extension_coding
4 - extension_vid
5 - extension_mp3
6 - extension_shortcut
7 - folder
8 - extension_unclassified

"""

# classify file extension into category above
def process_file_extension (extension):
    extension_variables = [0] * 9

    if extension in file_extension_dict:
        extension_variables[file_extension_dict[extension]] = 1
    else:
        extension_variables[-1] = 1

    return extension_variables
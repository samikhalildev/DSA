import os

def findNumberOfDirs(d, formatType, search):

    if not d:
        return 0

    count = 0

    for subdir, dirs, files in os.walk(d):

        # iterate over all .txt and add to count
        for f in files:
            if search in f and f.endswith(formatType):
                print(f)
                count += 1

        # iterate over all directories and call function resursively.
        for subDir in dirs:
            count += findNumberOfDirs(subDir, formatType, search)

    return count

path = '/Users/sami/documents'
formatType = '.txt'
search = 'data'

count = findNumberOfDirs(path, formatType, search)
print('{0} files found'.format(count))

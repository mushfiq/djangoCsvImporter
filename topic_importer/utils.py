import csv
def csv_to_list(file_path):
    file_object = csv.reader(open(file_path, "rb"), delimiter=',',quotechar='|')
    movie_list = []
    for f in file_object:
        movie_list.append(f)
    return movie_list

def handle_uploaded_file(f):
    print "file name is", f.content_type
    if f.content_type=="text/csv":
        destination = open('/home/caveman/sites/csv_importer/topic_importer/file.csv', 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
        return "true"
    else:
        return "invalid file type"


  
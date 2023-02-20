import csv


with open("names.csv",'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open("newcsvfile.csv","w") as new_file:
        fnames=['first_name','last_name']
        csv_writer = csv.DictWriter(new_file,fieldnames=fnames,delimiter = ",",lineterminator="\n")
        csv_writer.writeheader()
        for i in csv_reader:
            del i["email"]
            csv_writer.writerow(i)
        print("written sucessfully")
    
    
    
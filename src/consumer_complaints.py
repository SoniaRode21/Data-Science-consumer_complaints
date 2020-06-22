import csv
import sys
from collections import defaultdict,Counter


def read_file(input_file):
    """
    Function to read the input file
    :param input_file: input filename
    :return: results : list of list containing complaints
    """

    result=[]
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i=100
        for row in readCSV:
            result.append(row)

            i-=1
            if i<0:
                break

    result.pop(0)
    return result


def write_to_file(filename,hashmap):
    """
    Function to process the input and write the output to the file
    :param filename: Output file name
    :param hashmap: A map of product to its complaints
    :return:
    """
    import csv

    writer=csv.writer(open(filename, 'w'), delimiter=',',quotechar='"')
    for product in sorted(hashmap.keys()):
        years_list=list(val[0]  for val in hashmap[product])
        years=list(set(years_list))
        years.sort()

        for year in years:
            unique_data = [list(x) for x in set(tuple(x) for x in hashmap[product] if x[0]==year )]
            list_yearwise=[ x for x in hashmap[product] if x[0]==year ]
            #print(list_yearwise)
            max_count=max(list_yearwise)

            #print(max_count)
            percent=(list_yearwise.count(max_count)*100)/len(list_yearwise)

            #print(len(unique_data)," ______________",len(hashmap[product]))
            #print(product)
            if "," in product:
                writer.writerow([""+product+"",year,years_list.count(year),len(unique_data),round(percent)])
            else:
                writer.writerow([product,year,years_list.count(year),len(unique_data),round(percent)])


def get_sorted_hashmap(hashmap):
    """
    Function to sort complaints for each product according to year
    :param hashmap: A map of product to its complaints
    :return: sorted hashmap
    """
    # For each product
    for product in hashmap.keys():
            #print(product,hashmap[product])

            # Sort the complaints according to year
            hashmap[product]=[ complaint for complaint in sorted(hashmap[product], key=lambda x: x[0])]
    return hashmap


def get_hashmap(records):
    """

    :param records: List of list containing complaints
    :return: hashmap:  A map of product to its complaints
    """
    hashmap=defaultdict(list)
    for record in records:
        key =record[1].lower()

        hashmap[key].append([record[0][0:4],record[7].lower()])

    return hashmap


def main():

    # Read command line arguments
    input_file = str(sys.argv[1])
    output_file = sys.argv[2]
    output_file="report.csv"

    # Read data from file
    result = read_file(input_file)

    #print('\n')
    # Get a hashmap containing products as keys and their complaints as values
    hashmap = get_hashmap(result)
    #print("PART 1\n")
    hashmap = get_sorted_hashmap(hashmap)
    #print("PART 2\n")
    #print(hashmap)



    write_to_file(output_file,hashmap)
    #print("PART 3\n")


if __name__ == '__main__' :
    main()






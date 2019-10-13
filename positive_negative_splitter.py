import sys

def positive_negative_splitter(filepath, en_or_ja, output_filename):
    output_filename_positive = output_filename + "_positive.dict"
    output_filename_negative = output_filename + "_negative.dict"

    with open(filepath, "r", encoding="utf-8") as imported_dict:
        with open(output_filename_positive, "w", encoding="utf-8") as positive_file:
            with open(output_filename_negative, "w", encoding="utf-8") as negative_file:
                positive_set = set()
                negative_set = set()
                while True:
                    row = imported_dict.readline().split(":")

                    if not len(row) == 4 and not len(row) == 3:
                        break

                    if en_or_ja == "ja":
                        kanji = row[0]
                        hiragana = row[1]
                        positive_negative_value = float(row[3])

                        if positive_negative_value > 0:
                            positive_set.add(kanji + "\n")
                            positive_set.add(hiragana + "\n")
                        elif positive_negative_value < 0:
                            negative_set.add(kanji + "\n")
                            negative_set.add(hiragana + "\n")

                    elif en_or_ja == "en":
                        word = row[0]
                        positive_negative_value = float(row[2])

                        if positive_negative_value > 0:
                            positive_set.add(word + "\n")
                        elif positive_negative_value < 0:
                            negative_set.add(word + "\n")

                positive_file.writelines(positive_set)
                negative_file.writelines(negative_set)


    print("dictionary:\"" + filepath + "\" converted into binary dictionaries")
    print("positive dict:" + output_filename_positive)
    print("negative dict:" + output_filename_negative)
    
filepath = sys.argv[1]
en_or_ja = sys.argv[2]
output_filename = sys.argv[3]
positive_negative_splitter(filepath, en_or_ja, output_filename)


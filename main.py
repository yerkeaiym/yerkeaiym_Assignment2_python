from scrapper import DataScrapper

scrapper = DataScrapper()

NameMark = input("Enter name of currency or \"stop\" to end session:")
while NameMark != "stop":
    scrapper.get_data_by_name(NameMark)
    NameMark = input("Enter name of currency or \"stop\" to end session:")
   


    
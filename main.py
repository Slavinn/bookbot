def sort_on(dict):
    return dict["count"]

def main() -> int:
    with open("books/frankenstein.txt") as f:
        file_content = f.read().lower()
        dic = {}
        for i in file_content:
            if not i in  dic:
                dic[i] = 1
            else:
                dic[i] +=1
        dic_list = []
        for d in dic:
            if d.isalpha():
                dic_list.append({"letter": d, "count": dic[d]})
        dic_list.sort(reverse=True,key=sort_on)

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{len(file_content.split())} words found in document\n")

        for i in dic_list:
            print(f"The '{i["letter"]}' character was found {i["count"]} times")
        print("--- End report ---")

if __name__ == '__main__':
    main()

class utils:
    def __init__(self):
        pass

    @staticmethod
    def parse_context(urls_filename):
        return "empty.dat"

    @staticmethod
    def similarity_search_context(database, query_filename, answer_filenames):
        for filename in answer_filenames:
            with open(filename, 'w') as f:
                f.write("")
        return answer_filenames

    @staticmethod
    def mmr_search_context(database, query_filename, answer_filenames):
        for filename in answer_filenames:
            with open(filename, 'w') as f:
                f.write("")
        return answer_filenames

if __name__ == '__main__':
    database = parse_context("")
    main_context = similarity_search_context(database, "query.txt", ["main1.txt", "main2.txt", "main3.txt", "main4.txt", "main5.txt"])
    alt_context = mmr_search_context(database, "query.txt",  ["alt1.txt", "alt2.txt", "alt3.txt", "alt4.txt", "alt5.txt"])

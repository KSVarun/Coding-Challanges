no_of_test_cases = input()
no_books = 0
book_reading_index = 0
no_of_given_time_queries = 0
time_to_read_books = []
given_time_queries = []
index = 0


def sum_time(book_index, time_to_read_books, t, sum_t):
    sum_t += time_to_read_books[book_index]
    # print("SUM:"+str(sum_t))
    # print(t)
    if(t >= sum_t):
        book_index += 1
        sum_time(book_index, time_to_read_books, t, sum_t)
    else:
        book_index -= 1
        #print("book index:"+str(book_index))
        print(time_to_read_books[book_index])


for i in no_of_test_cases:
    no_books = int(input())
    book_reading_index = int(input())
    book_reading_index = book_reading_index-1
    no_of_given_time_queries = int(input())
    for j in range(no_books):
        time_to_read_books.append(int(input()))
    for k in range(no_of_given_time_queries):
        given_time_queries.append(int(input()))

    # print(len(given_time_queries))
    for l in range(len(given_time_queries)):
        if(time_to_read_books[book_reading_index] > given_time_queries[l]):
            print("-1")
            break
        sum_time(book_reading_index, time_to_read_books,
                 given_time_queries[l], 0)

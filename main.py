from modules import Book, Customers, Loans
# overall - very good project
# you did everything clearly, and wrote classes and modules in a very good manner
# try to avoid using the string like you did instead of object
# Well done!


# better to put these functions outside of main.
# this way you will have a clear code in main.py
def first_read():
    all_list = []
    with open("book_rank.txt", "r") as file:
        file.readline()
        for item in file:
            temp_list = item.split(",")
            # good - but why do you do str(Book)? why not just Book?
            # please fix
            book = str(Book(id=temp_list[0],
                            title=temp_list[1],
                            author=temp_list[2],
                            publisher=temp_list[3],
                            genre=temp_list[4],
                            frequency=temp_list[5][:-1]))
            all_list.append(book)
        return all_list, temp_list[0]

# why not add last_id to the Book class. it will be clearer
details = first_read()
last_id = details[1]
book_list = details[0]


def customer_read():
    customer_list = []
    with open("customers.txt", "r") as file:
        file.readline()
        for item in file:
            temp_list = item.split(",")
            # same here with the str - please fix
            customer = str(Customers(id=temp_list[0],
                                     name=temp_list[1],
                                     city=temp_list[2],
                                     age=temp_list[3][:-1]))
            customer_list.append(customer)
        return temp_list[0], customer_list

# same here with the id
customers_details = customer_read()
customer_id = customers_details[0]
customer_list = customers_details[1]


def loan_read():
    loans_list = []
    with open("loans.txt", "r") as file:
        file.readline()
        for item in file:
            temp_list = item.split(",")
            #same str(
            loan = str(Loans(custid=temp_list[0],
                             bookid=temp_list[1],
                             loandate=temp_list[2],
                             returndate=temp_list[3][:-1]))
            loans_list.append(loan)
        return temp_list[0],temp_list[1], loans_list

# i see that you dont user the loan_id and the book_id.
loans_details = loan_read()
loan_id = loans_details[0]
book_id = loans_details[1]
loans_list = loans_details[2]



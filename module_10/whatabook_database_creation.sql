CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!'\g
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost'\g

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
)\g

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
)\g

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
)\g

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
)\g

INSERT INTO store(locale)
    VALUES('28 Keowee Ave, Greenville, SC 29605')\g

INSERT INTO book(book_name, author, details)
    VALUES('It', 'Stephen King', 'A two part story about a cursed town')\g

INSERT INTO book(book_name, author, details)
    VALUES('The Walking Dead', 'Robert Kirkman', 'A zombie apocalypse story')\g

INSERT INTO book(book_name, author, details)
    VALUES('Cyberthreats', 'William Landis', 'Protecting your devices from cyberattacks')\g

INSERT INTO book(book_name, author, details)
    VALUES('Star Wars', 'George Lucas', 'The book of the movie')\g

INSERT INTO book(book_name, author, details)
    VALUES('The Night of the Living Dead', 'George Romero', 'Graphic novel')\g

INSERT INTO book(book_name, author, details)
    VALUES('Where the Sidewalk Ends', 'Shel Silverstein', 'Children')\g

INSERT INTO book(book_name, author)
    VALUES('The Escape', 'Marshall Tucker')\g

INSERT INTO book(book_name, author, details)
    VALUES('The Predator', 'Charles Fields', 'Non fiction')\g

INSERT INTO book(book_name, author)
    VALUES('The Deep', 'James L. Smith')\g

INSERT INTO user(first_name, last_name) 
    VALUES('Maynard', 'Keenan')\g

INSERT INTO user(first_name, last_name)
    VALUES('Trent', 'Reznor')\g

INSERT INTO user(first_name, last_name)
    VALUES('Chino', 'Moreno')\g

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Maynard'), 
        (SELECT book_id FROM book WHERE book_name = 'The Walking Dead')
    )\g

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Trent'),
        (SELECT book_id FROM book WHERE book_name = 'Where the Sidewalk Ends')
    )\g

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chino'),
        (SELECT book_id FROM book WHERE book_name = 'The Night of the Living Dead')
    )\g

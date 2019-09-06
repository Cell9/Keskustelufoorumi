# CREATE TABLE-lauseet

- Create account table
```
CREATE TABLE account (
        date_created DATETIME,
        date_modified DATETIME,
        id INTEGER NOT NULL,
        name VARCHAR(60) NOT NULL,
        username VARCHAR(60) NOT NULL,
        email VARCHAR(60) NOT NULL,
        password VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
);
```
- Create article table
```
CREATE TABLE article (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        postname VARCHAR(80) NOT NULL,
        active BOOLEAN NOT NULL,
        text VARCHAR(2000) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (active IN (0, 1)),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```
- Create groups table
```
CREATE TABLE groups (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(50) NOT NULL,
        "desc" VARCHAR(1000) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```
- Create response table
```
CREATE TABLE response (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        text VARCHAR(2000) NOT NULL,
        article_id INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(article_id) REFERENCES article (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```

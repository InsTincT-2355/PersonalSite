ALTER TABLE CUSTOMERS
ADD CONSTRAINT pk_customers PRIMARY KEY (CUSTOMER_ID);

ALTER TABLE MOVIES
ADD CONSTRAINT pk_movies PRIMARY KEY (TITLE_ID);

ALTER TABLE MEDIA
ADD CONSTRAINT pk_media PRIMARY KEY (MEDIA_ID);

ALTER TABLE MEDIA
ADD CONSTRAINT fk_media_movies FOREIGN KEY (TITLE_ID) REFERENCES MOVIES(TITLE_ID);

ALTER TABLE RENTAL_HISTORY
ADD CONSTRAINT pk_rental PRIMARY KEY (MEDIA_ID, RENTAL_DATE);

ALTER TABLE RENTAL_HISTORY
ADD CONSTRAINT fk_rental_media FOREIGN KEY (MEDIA_ID) REFERENCES MEDIA(MEDIA_ID);

ALTER TABLE RENTAL_HISTORY
ADD CONSTRAINT fk_rental_customers FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID);

ALTER TABLE ACTORS
ADD CONSTRAINT pk_actors PRIMARY KEY (ACTOR_ID);

ALTER TABLE STAR_BILLINGS
ADD CONSTRAINT pk_star_billings PRIMARY KEY (ACTOR_ID, TITLE_ID);

CREATE VIEW TITLE_UNAVAIL AS
SELECT MO.TITLE, RH.MEDIA_ID
FROM RENTAL_HISTORY RH
JOIN MEDIA M ON RH.MEDIA_ID = M.MEDIA_ID
JOIN MOVIES MO ON M.TITLE_ID = MO.TITLE_ID
WHERE RH.RETURN_DATE IS NULL;

COMMIT;



CREATE SEQUENCE customer_id_seq
START WITH 101
INCREMENT BY 1;

CREATE SEQUENCE title_id_seq
START WITH 1
INCREMENT BY 1;

CREATE SEQUENCE media_id_seq
START WITH 92
INCREMENT BY 1;

CREATE SEQUENCE actor_id_seq
START WITH 1001
INCREMENT BY 1;


SELECT sequence_name, min_value, increment_by
FROM user_sequences
WHERE sequence_name = 'CUSTOMER_ID_SEQ';

SELECT sequence_name, min_value, increment_by
FROM user_sequences
WHERE sequence_name = 'TITLE_ID_SEQ';

SELECT sequence_name, min_value, increment_by
FROM user_sequences
WHERE sequence_name = 'MEDIA_ID_SEQ';

SELECT sequence_name, min_value, increment_by
FROM user_sequences
WHERE sequence_name = 'ACTOR_ID_SEQ';

commit;


INSERT INTO CUSTOMERS (CUSTOMER_ID, LAST_NAME, FIRST_NAME, HOME_PHONE, ADDRESS, CITY, STATE, EMAIL, CELL_PHONE)
VALUES (customer_id_seq.NEXTVAL, 'Palombo', 'Lisa', '716-270-2669', '123 Main St', 'Buffalo', 'NY', 'palombo@ecc.edu', '716-555-1212');

INSERT INTO MOVIES (TITLE_ID, TITLE, DESCRIPTION, RATING, CATEGORY, RELEASE_DATE)
VALUES (title_id_seq.NEXTVAL, 'Remember the Titans', 'The true story of a newly appointed African-American coach and his high school team on their first season as a racially integrated unit.', 'PG', 'DRAMA', TO_DATE('29-SEP-2000', 'DD-MON-YYYY'));

INSERT INTO ACTORS (ACTOR_ID, STAGE_NAME, FIRST_NAME, LAST_NAME, BIRTH_DATE)
VALUES (actor_id_seq.NEXTVAL, 'Brad Pitt', 'William', 'Pitt', TO_DATE('18-DEC-1963', 'DD-MON-YYYY'));

INSERT INTO MEDIA (MEDIA_ID, FORMAT, TITLE_ID)
VALUES (media_id_seq.NEXTVAL, 'DVD', title_id_seq.CURRVAL);

INSERT INTO MEDIA (MEDIA_ID, FORMAT, TITLE_ID)
VALUES (media_id_seq.NEXTVAL, 'VHS', title_id_seq.CURRVAL);

commit;


CREATE INDEX idx_customers_last_name ON CUSTOMERS(LAST_NAME);

SELECT index_name, table_name, column_name
FROM user_ind_columns
WHERE table_name = 'CUSTOMERS' AND column_name = 'LAST_NAME';

commit;


CREATE SYNONYM TU FOR TITLE_UNAVAIL;

SELECT synonym_name, table_owner, table_name
FROM user_synonyms
WHERE synonym_name = 'TU';

BEGIN
  FOR r IN (SELECT * FROM TU) LOOP
    DBMS_OUTPUT.PUT_LINE(r.TITLE || ', ' || r.MEDIA_ID);
  END LOOP;
END;
/

commit;

INSERT INTO CUSTOMERS (CUSTOMER_ID, LAST_NAME, FIRST_NAME, HOME_PHONE, ADDRESS, CITY, STATE, EMAIL, CELL_PHONE)
VALUES (customer_id_seq.NEXTVAL, 'Smith', 'John', '123-456-7890', '456 Oak Street', 'New York', 'NY', 'john.smith@example.com', '987-654-3210');

INSERT INTO CUSTOMERS (CUSTOMER_ID, LAST_NAME, FIRST_NAME, HOME_PHONE, ADDRESS, CITY, STATE, EMAIL, CELL_PHONE)
VALUES (customer_id_seq.NEXTVAL, 'Johnson', 'Emma', '234-567-8901', '789 Maple Avenue', 'Los Angeles', 'CA', 'emma.johnson@example.com', '876-543-2109');

INSERT INTO CUSTOMERS (CUSTOMER_ID, LAST_NAME, FIRST_NAME, HOME_PHONE, ADDRESS, CITY, STATE, EMAIL, CELL_PHONE)
VALUES (customer_id_seq.NEXTVAL, 'Brown', 'Emily', '456-789-0123', '789 Pine Street', 'Houston', 'TX', 'emily.brown@example.com', '654-321-0987');

INSERT INTO CUSTOMERS (CUSTOMER_ID, LAST_NAME, FIRST_NAME, HOME_PHONE, ADDRESS, CITY, STATE, EMAIL, CELL_PHONE)
VALUES (customer_id_seq.NEXTVAL, 'Jones', 'Daniel', '567-890-1234', '234 Cedar Street', 'Miami', 'FL', 'daniel.jones@example.com', '543-210-9876');

INSERT INTO CUSTOMERS (CUSTOMER_ID, LAST_NAME, FIRST_NAME, HOME_PHONE, ADDRESS, CITY, STATE, EMAIL, CELL_PHONE)
VALUES (customer_id_seq.NEXTVAL, 'Altouqi', 'ahmed', '517-890-1244', '234 apple Street', 'columbia', 'SC', 'ahmed.t@example.com', '533-434-2367');

INSERT INTO MOVIES (TITLE_ID, TITLE, DESCRIPTION, RATING, CATEGORY, RELEASE_DATE)
VALUES (title_id_seq.NEXTVAL, 'Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', 'PG13', 'SCI-FI', TO_DATE('16-JUL-2010', 'DD-MON-YYYY'));

INSERT INTO MOVIES (TITLE_ID, TITLE, DESCRIPTION, RATING, CATEGORY, RELEASE_DATE)
VALUES (title_id_seq.NEXTVAL, 'The Dark Knight', 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.', 'PG13', 'ACTION', TO_DATE('18-JUL-2008', 'DD-MON-YYYY'));

INSERT INTO MOVIES (TITLE_ID, TITLE, DESCRIPTION, RATING, CATEGORY, RELEASE_DATE)
VALUES (title_id_seq.NEXTVAL, 'Pulp Fiction', 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 'R', 'DRAMA', TO_DATE('14-OCT-1994', 'DD-MON-YYYY'));

INSERT INTO MOVIES (TITLE_ID, TITLE, DESCRIPTION, RATING, CATEGORY, RELEASE_DATE)
VALUES (title_id_seq.NEXTVAL, 'The Shawshank Redemption', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'R', 'DRAMA', TO_DATE('14-OCT-1994', 'DD-MON-YYYY'));

INSERT INTO MOVIES (TITLE_ID, TITLE, DESCRIPTION, RATING, CATEGORY, RELEASE_DATE)
VALUES (title_id_seq.NEXTVAL, 'Forrest Gump', 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.', 'PG13', 'DRAMA', TO_DATE('06-JUL-1994', 'DD-MON-YYYY'));

delete from movies where title_ID = 23;

INSERT INTO ACTORS (ACTOR_ID, STAGE_NAME, FIRST_NAME, LAST_NAME, BIRTH_DATE)
VALUES (actor_id_seq.NEXTVAL, 'Tom Hanks', 'Thomas', 'Hanks', TO_DATE('1956-07-09', 'YYYY-MM-DD'));

INSERT INTO ACTORS (ACTOR_ID, STAGE_NAME, FIRST_NAME, LAST_NAME, BIRTH_DATE)
VALUES (actor_id_seq.NEXTVAL, 'Leonardo DiCaprio', 'Leonardo', 'DiCaprio', TO_DATE('1974-11-11', 'YYYY-MM-DD'));

INSERT INTO ACTORS (ACTOR_ID, STAGE_NAME, FIRST_NAME, LAST_NAME, BIRTH_DATE)
VALUES (actor_id_seq.NEXTVAL, 'Meryl Streep', 'Mary', 'Streep', TO_DATE('1949-06-22', 'YYYY-MM-DD'));

INSERT INTO ACTORS (ACTOR_ID, STAGE_NAME, FIRST_NAME, LAST_NAME, BIRTH_DATE)
VALUES (actor_id_seq.NEXTVAL, 'Brad Pitt', 'William', 'Pitt', TO_DATE('1963-12-18', 'YYYY-MM-DD'));

INSERT INTO STAR_BILLINGS (ACTOR_ID, TITLE_ID, COMMENTS)
VALUES (actor_id_seq.NEXTVAL, title_id_seq.NEXTVAL, 'Romantic Lead');

INSERT INTO STAR_BILLINGS (ACTOR_ID, TITLE_ID, COMMENTS)
VALUES (actor_id_seq.NEXTVAL, title_id_seq.NEXTVAL, 'Supporting Role');

INSERT INTO STAR_BILLINGS (ACTOR_ID, TITLE_ID, COMMENTS)
VALUES (actor_id_seq.NEXTVAL, title_id_seq.NEXTVAL, 'Main Villain');

INSERT INTO STAR_BILLINGS (ACTOR_ID, TITLE_ID, COMMENTS)
VALUES (actor_id_seq.NEXTVAL, title_id_seq.NEXTVAL, 'Cameo Appearance');

INSERT INTO MEDIA (MEDIA_ID, FORMAT, TITLE_ID)
VALUES (94, 'DVD', 27);

INSERT INTO MEDIA (MEDIA_ID, FORMAT, TITLE_ID)
VALUES (95, 'DVD', 28);

INSERT INTO MEDIA (MEDIA_ID, FORMAT, TITLE_ID)
VALUES (96, 'VHS', 29);


INSERT INTO RENTAL_HISTORY (MEDIA_ID, RENTAL_DATE, CUSTOMER_ID, RETURN_DATE)
VALUES (92, TO_DATE('01-APR-2024', 'DD-MON-YYYY'), 121, TO_DATE('02-APR-2024', 'DD-MON-YYYY'));

INSERT INTO RENTAL_HISTORY (MEDIA_ID, RENTAL_DATE, CUSTOMER_ID, RETURN_DATE)
VALUES (93, TO_DATE('02-APR-2024', 'DD-MON-YYYY'), 122, TO_DATE('03-APR-2024', 'DD-MON-YYYY'));

INSERT INTO RENTAL_HISTORY (MEDIA_ID, RENTAL_DATE, CUSTOMER_ID, RETURN_DATE)
VALUES (94, TO_DATE('03-APR-2024', 'DD-MON-YYYY'), 124, TO_DATE('04-APR-2024', 'DD-MON-YYYY'));

INSERT INTO RENTAL_HISTORY (MEDIA_ID, RENTAL_DATE, CUSTOMER_ID, RETURN_DATE)
VALUES (95, TO_DATE('04-APR-2024', 'DD-MON-YYYY'), 125, TO_DATE('05-APR-2024', 'DD-MON-YYYY'));

INSERT INTO RENTAL_HISTORY (MEDIA_ID, RENTAL_DATE, CUSTOMER_ID, RETURN_DATE)
VALUES (96, TO_DATE('05-APR-2024', 'DD-MON-YYYY'), 126, TO_DATE('06-APR-2024', 'DD-MON-YYYY'));

select * from customers;
select * from media;
select * from movies;
select * from rental_history;
select * from actors;
select * from star_billings;

commit;
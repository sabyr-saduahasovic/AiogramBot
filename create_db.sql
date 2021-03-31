create table if not exists products
(
    idx text,
    title text,
    body text,
    photo bytea,
    price integer,
    tag text
);

create table if not exists categories
(
    idx text,
    title text
);

create table if not exists cart
(
    cid integer,
    idx text,
    quantity integer
);

create table if not exists orders
(
    cid integer,
    user_name text,
    user_address text,
    products text
);

create table if not exists questions
(
    cid integer,
    question text
);

create table if not exists wallet
(
    cid integer,
    balance real
);

alter table products
    owner to postgres;

alter table categories
    owner to postgres;

alter table cart
    owner to postgres;

alter table orders
    owner to postgres;

alter table questions
    owner to postgres;

alter table wallet
    owner to postgres;


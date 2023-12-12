DROP TABLE IF EXISTS user, offer, history;

CREATE TABLE "offer" {
    "id" uuid PRIMARY KEY,
    "title" varchar(255),
    "price" float,
    "details" json,
    "record_time" date,
    "user_id" uuid
}

CREATE TABLE "history" {
    "id" bigserial,
    "offer_id" uuid,
    "prices" float[],
    "record_times" date[]
}

CREATE TABLE "user" {
    "id" uuid PRIMARY KEY,
    "name" varchar(100)
}

ALTER TABLE "history" ADD FOREIGN KEY ("offer_id") REFERENCES "offer" ("id");
ALTER TABLE "offer" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

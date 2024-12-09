--SCHEMA
DROP TABLE IF EXISTS "pizzas";
DROP SEQUENCE IF EXISTS pizzas_id_seq;
CREATE SEQUENCE pizzas_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."pizzas" (
    "id" integer DEFAULT nextval('pizzas_id_seq') NOT NULL,
    "name" character varying NOT NULL,
    "ingredients" character varying NOT NULL,
    "price" double precision NOT NULL,
    CONSTRAINT "ix_pizzas_name" UNIQUE ("name"),
    CONSTRAINT "pizzas_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_pizzas_id" ON "public"."pizzas" USING btree ("id");

--DATA
INSERT INTO "pizzas" ("id", "name", "ingredients", "price") VALUES
(2,	'Margherita',	'Basilic, Mozzarella',	6);
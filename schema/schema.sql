CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "name" VARCHAR(255),
  "email" VARCHAR(255),
  "updated_at" TIMESTAMP,
  "deleted_at" TIMESTAMP
);

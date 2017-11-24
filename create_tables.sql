DROP TABLE IF EXISTS words;

CREATE EXTENSION IF NOT EXISTS intarray;

CREATE TABLE words (
  word          VARCHAR(60) NOT NULL,
  letter_numbers INT []
);

CREATE INDEX idx_letter_number ON words USING GIN(letter_numbers gin__int_ops);

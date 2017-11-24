-- EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) 
WITH wan AS (
	SELECT ARRAY(SELECT ascii(unnest(regexp_split_to_array(upper('ETRAMOIL'), ''))))::int[] as lookup_numbers
)
SELECT words.word
FROM wan, words
WHERE wan.lookup_numbers @> words.letter_numbers
ORDER BY icount(wan.lookup_numbers & words.letter_numbers) DESC

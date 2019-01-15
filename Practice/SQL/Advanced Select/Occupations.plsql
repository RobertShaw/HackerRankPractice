#Oracle Implementation
#Two implementations

SELECT MIN(D), MIN(P), MIN(S), MIN(A) FROM (( SELECT DENSE_RANK() OVER (PARTITION BY occupation ORDER BY name) as Rank, Name, Occupation FROM Occupations) PIVOT ( MIN(NAME) FOR occupation IN ('Doctor' as D, 'Professor' as P, 'Actor' as A, 'Singer' as S))) group by RANK order by rank;

select min(D), min(P), min(S), min(A) from ( SELECT DENSE_RANK() OVER (PARTITION BY occupation ORDER BY name) as Rank, DECODE(occupation, 'Doctor', name, NULL) as D, DECODE(occupation, 'Professor', name, NULL) as P ,DECODE(occupation, 'Singer', name, NULL) as S,DECODE(occupation, 'Actor', name, NULL) as A FROM Occupations) group by Rank order by Rank;

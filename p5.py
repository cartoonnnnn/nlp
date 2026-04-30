docker start neo4j-container
docker exec -it neo4j-container cypher-shell -u neo4j -p password

CREATE 
(:User {UserID:1, Username:'John'}),
(:User {UserID:2, Username:'Alice'}),
(:User {UserID:3, Username:'Bob'}),
(:User {UserID:4, Username:'Emma'}),
(:User {UserID:5, Username:'Liam'}),
(:Movie {MovieID:1, Title:'Inception'}),
(:Movie {MovieID:2, Title:'The Matrix'}),
(:Movie {MovieID:3, Title:'Interstellar'}),
(:Movie {MovieID:4, Title:'Avatar'}),
(:Movie {MovieID:5, Title:'Titanic'});

MATCH (u:User), (m:Movie)
WHERE (u.Username = 'John' AND m.Title IN ['Inception','The Matrix']) OR
      (u.Username = 'Alice' AND m.Title = 'Inception') OR
      (u.Username = 'Bob' AND m.Title = 'The Matrix') OR
      (u.Username = 'Emma' AND m.Title = 'Inception') OR
      (u.Username = 'Liam' AND m.Title IN ['Inception','The Matrix'])
CREATE (u)-[:LIKES]->(m);

MATCH (u:User {Username:'John'})-[:LIKES]->(m:Movie)
RETURN m.Title;

MATCH (u:User)-[:LIKES]->(m:Movie {Title:'Inception'})
RETURN u.Username;

MATCH (m:Movie)
RETURN m.Title
ORDER BY m.Title;

MATCH (u:User)-[:LIKES]->(:Movie {Title:'The Matrix'}),
      (u)-[:LIKES]->(:Movie {Title:'Inception'})
RETURN u.Username;

MATCH (m:Movie)<-[:LIKES]-(u:User)
RETURN m.Title, COUNT(u) AS likes
ORDER BY likes DESC
LIMIT 1;

MATCH (u:User)-[:LIKES]->(m:Movie)
RETURN u.Username, COUNT(m) AS totalLikes
ORDER BY totalLikes DESC
LIMIT 5;



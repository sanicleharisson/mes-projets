import MySQLdb
async def on_connect(self):

#SELECT [ DISTINCT ] * | colonne1 [, colonne2, colonne3, …] | fonction d’agrégation
FROM table1

[ ( [ INNER | LEFT | RIGHT | FULL ] JOIN table2 ON table1.colonne_i = table2.colonne_j )

[ JOIN table3 ON table_i.colonne_k = table3.colonne_l …] ]

[ WHERE condition]

[ GROUP BY colonne1 [, colonne2, …]

[ HAVING condition ] ]

[ ORDER BY colonne1 [ ASC | DESC ] [, colonne2 [ ASC | DESC ], …]
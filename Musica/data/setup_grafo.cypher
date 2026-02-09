// 1. Criar os Nós de Usuários
CREATE (:Usuario {nome: 'Thiago'}),
       (:Usuario {nome: 'Mariana'}),
       (:Usuario {nome: 'Pedro'}),
       (:Usuario {nome: 'Ana'});

// 2. Criar os Nós de Músicas
CREATE (:Musica {titulo: 'Bohemian Rhapsody', genero: 'Rock'}),
       (:Musica {titulo: 'Imagine', genero: 'Pop'}),
       (:Musica {titulo: 'Hotel California', genero: 'Rock'}),
       (:Musica {titulo: 'Back in Black', genero: 'Rock'});

// 3. Criar as Conexões (Relacionamentos)
MATCH (u:Usuario {nome: 'Thiago'}), (m:Musica {titulo: 'Bohemian Rhapsody'}) CREATE (u)-[:OUVIU]->(m);
MATCH (u:Usuario {nome: 'Thiago'}), (m:Musica {titulo: 'Imagine'}) CREATE (u)-[:OUVIU]->(m);
MATCH (u:Usuario {nome: 'Mariana'}), (m:Musica {titulo: 'Imagine'}) CREATE (u)-[:OUVIU]->(m);
MATCH (u:Usuario {nome: 'Pedro'}), (m:Musica {titulo: 'Bohemian Rhapsody'}) CREATE (u)-[:OUVIU]->(m);
MATCH (u:Usuario {nome: 'Pedro'}), (m:Musica {titulo: 'Back in Black'}) CREATE (u)-[:OUVIU]->(m);
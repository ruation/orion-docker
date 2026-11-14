CREATE TABLE cursos(
    id SERIAL PRIMARY KEY,
    nome_curso TEXT NOT NULL);

CREATE TABLE alunos(
   id SERIAL PRIMARY KEY,
   nome TEXT NOT NULL,
   email TEXT NOT NULL,
   curso_id INT REFERENCES cursos(id));

INSERT INTO cursos (nome_curso) VALUES 
('Engenharia de Software'), 
('Ciência da Computação'), 
('Ciência de Dados');

INSERT INTO alunos (nome, email, curso_id) VALUES 
('Ruan', 'ruan@orion.com', 2),
('Yago', 'yago@orion.com', 2), 
('dani', 'dani@orion.com', 1);

SELECT * FROM alunos;
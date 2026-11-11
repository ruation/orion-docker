SELECT alunos.nome, cursos.nome_curso
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id;

SELECT alunos.nome, cursos.nome_curso
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id
WHERE cursos.nome_curso = 'Ciência da Computação';

UPDATE alunos SET curso_id = 1 WHERE id = 1;

SELECT alunos.nome, cursos.nome_curso
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id;

SELECT cursos.nome_curso
FROM cursos
LEFT JOIN alunos ON cursos.id = alunos.curso_id
WHERE alunos.id IS NULL;
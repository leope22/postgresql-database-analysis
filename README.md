# Análise e Otimização de um Banco de Dados para E-learning

Este repositório contém o projeto de estruturação, população e otimização de um banco de dados PostgreSQL para a **TechEduStream**, uma plataforma de educação online focada em tecnologia. O projeto abrange desde o design do esquema relacional até a análise de performance de consultas e a implementação de regras de segurança avançadas.

## Visão Geral do Projeto

O objetivo foi modelar um sistema de grande escala, analisar gargalos de performance em consultas complexas e implementar otimizações e funcionalidades de segurança utilizando recursos avançados do PostgreSQL.

### Principais Destaques

  * **Modelagem de Dados**: Criação de um esquema de banco de dados coeso, incluindo Entidade-Relacionamento (DER) e Modelo Relacional (MR).
  * **População em Larga Escala**: Geração de um dataset massivo com `Python` e `Faker`, simulando um ambiente de produção realista.
  * **Otimização de Consultas**: Análise profunda de planos de execução (`EXPLAIN ANALYZE`) para identificar e corrigir gargalos, resultando em **melhorias de performance de até 45%**.
  * **Segurança e Controle de Acesso**: Implementação de um sistema robusto de perfis de usuário (`Admin`, `Instrutor`, `Aluno`, `Anônimo`) com `ROLES`, `GRANTs`, `VIEWS` e `TRIGGERS` para garantir a integridade e a privacidade dos dados.
  * **Programação no SGBD**: Desenvolvimento de `Funções Armazenadas` em PL/pgSQL para encapsular lógicas de negócio complexas e garantir a segurança contra SQL Injection.

## Análise e Otimização de Consultas

Uma parte central do projeto foi a análise aprofundada e a reestruturação de consultas SQL complexas para maximizar a performance do banco de dados. Utilizando a ferramenta `EXPLAIN ANALYZE`, foram identificados gargalos de performance, como junções ineficientes e varreduras sequenciais (`Seq Scan`) em tabelas de grande volume.

Para solucionar esses problemas, as consultas foram reescritas com **técnicas avançadas de SQL**, como o uso de Common Table Expressions (CTEs) e a criação de índices estratégicos. Essas mudanças permitiram que o otimizador do PostgreSQL gerasse planos de execução muito mais eficientes, pré-filtrando dados e reduzindo o custo computacional das junções.

O processo validou a eficácia das otimizações aplicadas, resultando em melhorias de performance significativas. Em alguns casos, a reestruturação das consultas levou a uma **redução de mais de 35% no tempo médio de execução**.

## Segurança e Funções Armazenadas

Para garantir a segurança e a correta aplicação das regras de negócio, foram implementados múltiplos níveis de controle de acesso e funções armazenadas.

  * **Perfis de Usuário**: Quatro roles (`administrador`, `instrutor`, `aluno`, `anonimo`) com permissões estritamente definidas.
  * **`TRIGGERS`**: Para garantir que instrutores só possam modificar seus próprios cursos e aulas.
  * **`VIEWS`**: Para permitir que alunos vejam apenas seus próprios dados de inscrição, protegendo a privacidade.
  * **`STORED FUNCTIONS`**: Para criar endpoints de consulta seguros e parametrizados, prevenindo SQL Injection.

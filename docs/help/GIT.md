# Ajudas GIT

## Como desfazer o último commit sem perder as alterações?

Para desfazer o último commit sem perder as alterações no código, use o seguinte comando:

```bash
git reset --soft HEAD~1
```
### O que esse comando faz?

- --soft mantém todas as alterações no staging area (índice), então você pode simplesmente fazer um novo commit corrigido se quiser.
- HEAD~1 indica que queremos desfazer apenas o último commit.

Se você quiser manter as alterações, mas removê-las do staging area, use:

```bash
git reset --mixed HEAD~1
```

# Front-end fornecido

Este front-end está pronto. O trabalho do grupo é construir uma API FastAPI compatível com as chamadas existentes em `app.js`.

Para executá-lo no terminal do VS Code:

```powershell
python -m http.server 5500
```

Acesse `http://localhost:5500`.

Não altere a constante `URL_API`, os nomes das propriedades JSON ou os códigos HTTP esperados apenas para ocultar erros no back-end. Alterações justificadas de interface são permitidas depois que a integração básica funcionar.

=========================================================================
## Backend
O back-end é a parte de uma aplicação que roda no servidor, nos bastidores, e que o usuário final não vê diretamente (ao contrário da interface visual, que é o front-end). Ele é o "cérebro" do sistema, responsável por processar regras de negócio, gerenciar dados e garantir que a aplicação funcione de forma segura e eficiente.

Abaixo estão as principais funções do back-end:

Gerenciamento de Banco de Dados: O back-end é responsável por se conectar, ler, gravar, atualizar e excluir dados em bancos de dados (como SQL, MongoDB, etc.), garantindo que as informações persistam de forma segura.

Processamento de Regras de Negócio: É nele que a lógica da aplicação acontece. Por exemplo: calcular descontos, validar se um usuário tem permissão para acessar determinada página, processar pagamentos ou verificar regras de estoque.

Criação e Gerenciamento de APIs: O back-end expõe endpoints (rotas, como GET /api/avisos ou POST /api/avisos) que permitem que o front-end envie e receba dados, geralmente estruturados em formato JSON.

Autenticação e Segurança: Gerencia o cadastro, login e controle de acesso dos usuários por meio de tokens (como JWT), senhas criptografadas e proteção contra ataques cibernéticos comuns.

Comunicação com Serviços Externos: Integra a aplicação com APIs de terceiros, como gateways de pagamento (Stripe, PayPal), serviços de e-mail, envio de SMS ou armazenamento em nuvem.

http://127.0.0.1:8000/docs

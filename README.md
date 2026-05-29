# Loja Veloz - Arquitetura de Microsserviços e Cloud DevOps

## 🎬 Video Pitch

[![Assista ao Video Pitch da Loja Veloz](https://img.youtube.com/vi/2T3ks1kI7VY/maxresdefault.jpg)](https://youtu.be/2T3ks1kI7VY)

> Clique na imagem acima para assistir ao pitch completo da solução — apresentando a arquitetura, os desafios de negócio resolvidos e a visão técnica por trás da modernização da plataforma Loja Veloz.

---

Este repositório contém a implementação da modernização da plataforma **Loja Veloz**, utilizando uma arquitetura distribuída baseada em microsserviços, totalmente conteinerizada com Docker, orquestrada em ambiente de produção via Kubernetes e integrada com uma esteira automatizada de CI/CD através do GitHub Actions.

O objetivo central desta arquitetura é garantir alta disponibilidade, resiliência (self-healing) e escalabilidade elástica para suportar com segurança picos de tráfego promocionais (como campanhas de vendas e Black Friday), blindando a experiência e a jornada do usuário final nas interfaces front-end.

---

## 🚀 Componentes do Sistema

O ecossistema é dividido em cinco componentes principais que interagem de forma isolada e segura:

| Componente | Tecnologia | Porta |
|---|---|---|
| **Serviço de Pedidos** | Python/Flask | 5001 |
| **Serviço de Estoque** | Python/Flask | 5002 |
| **Serviço de Pagamentos** | Python/Flask | 5003 |
| **Banco de Dados** | PostgreSQL 15-Alpine | — |
| **API Gateway** | Nginx | 8080 (local) / 30080 (K8s) |

---

## 🛠️ Pré-requisitos

Antes de iniciar, certifique-se de ter instalado na sua máquina:

- **Docker** (com suporte a WSL2 se estiver no Windows)
- **Docker Compose**
- **Kubectl** (para administração do cluster)
- Um **cluster Kubernetes local** ativo (Docker Desktop Kubernetes habilitado ou Minikube)

---

## 💻 1. Execução em Ambiente Local (Docker Compose)

Para fins de desenvolvimento padronizado, testes rápidos e reprodutibilidade imediata, utilize o Docker Compose.

**Passo 1: Inicializar o ecossistema**

Navegue até a pasta raiz do projeto (`loja-veloz`) no seu terminal e execute:

```bash
docker-compose up --build -d
```

**Passo 2: Validar o status dos contêineres**

```bash
docker compose ps
```

**Passo 3: Testar o acesso através do Gateway**

Abra o navegador ou utilize uma ferramenta de requisições (Postman/cURL):

- Pedidos: `http://localhost:8080/pedidos`
- Estoque: `http://localhost:8080/estoque`
- Pagamentos: `http://localhost:8080/pagamentos`

**Passo 4: Parar o ambiente local**

```bash
docker compose down
```

---

## ☸️ 2. Implantação em Produção (Kubernetes Local)

Para simular o ambiente de produção com alta disponibilidade, tolerância a falhas e autoescalamento, os manifestos devem ser injetados no cluster Kubernetes.

**Passo 1: Construir as imagens Docker locais**

```bash
docker build -t loja-veloz-pedidos:v1 ./pedidos
docker build -t loja-veloz-estoque:v1 ./estoque
docker build -t loja-veloz-pagamentos:v1 ./pagamentos
```

**Passo 2: Configurar o contexto do kubectl**

```bash
kubectl config use-context docker-desktop
```

**Passo 3: Aplicar ConfigMaps e Secrets**

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
```

**Passo 4: Inicializar o Banco de Dados (PostgreSQL)**

```bash
kubectl apply -f k8s/db.yaml
```

**Passo 5: Implantar os Microsserviços**

```bash
kubectl apply -f k8s/pedidos.yaml
kubectl apply -f k8s/estoque.yaml
kubectl apply -f k8s/pagamentos.yaml
```

**Passo 6: Implantar o API Gateway (Nginx)**

```bash
kubectl apply -f k8s/gateway.yaml
```

**Passo 7: Ativar a Escalabilidade Automática (HPA)**

```bash
kubectl autoscale deployment servico-pedidos --cpu-percent=70 --min=2 --max=5
```

**Passo 8: Validar a saúde do cluster**

```bash
kubectl get pods
kubectl get services
kubectl get hpa
```

**Passo 9: Testar em Produção**

Acesse a aplicação via NodePort:

```
http://localhost:30080/pedidos
```

---

## 🔄 3. Esteira de CI/CD (GitHub Actions)

O repositório está configurado com automação contínua através do arquivo `.github/workflows/pipeline.yml`.

**Gatilho (Trigger):** Qualquer `push` realizado na ramificação principal (`main`) dispara a esteira de forma 100% automatizada.

**Etapas executadas no Pipeline:**

1. **Checkout** — Baixa o código atualizado em um ambiente Ubuntu limpo na nuvem.
2. **Configuração de Ambiente** — Instala e configura a versão estável do Python 3.11.
3. **Lint & Testes Sintáticos** — Executa o módulo nativo `py_compile` para assegurar que nenhum erro de digitação ou quebra de sintaxe do Python seja promovido para produção.
4. **Docker Build** — Realiza a compilação e construção das novas imagens de contêiner de todos os microsserviços de forma automatizada, garantindo que o artefato final esteja pronto para o deploy.

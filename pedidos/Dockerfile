# pedidos/Dockerfile
# Usar uma imagem base oficial e leve do Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar apenas os requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY app.py .

# Criar um usuário não-root por segurança e mudar a propriedade dos arquivos
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expor a porta que a aplicação vai rodar
EXPOSE 5001

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
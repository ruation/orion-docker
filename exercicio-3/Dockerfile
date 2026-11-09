# Estágio 1: Base e instalação de dependências
FROM python:3.11-alpine AS base
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Estágio 2: Imagem final otimizada para produção (ou desenvolvimento)
FROM base AS final
COPY . ./
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
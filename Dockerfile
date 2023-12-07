# Separate build image
FROM python:3.10.8-slim-buster as compile-image

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip

# Final image
FROM python:3.10.8-slim-buster

COPY --from=compile-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
ENV HOME=/app

RUN addgroup --system app && adduser --system --group app

COPY . .

RUN chown -R app:app $HOME
RUN chown -R app:app "/opt/venv/"

USER app

RUN pip install -e .
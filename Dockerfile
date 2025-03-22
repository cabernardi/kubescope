FROM python:3.12-slim

RUN pip3 install poetry

RUN useradd -ms /bin/bash kubescope -u 1001
USER kubescope
WORKDIR /home/kubescope

COPY poetry.lock pyproject.toml ./

COPY --chown=kubescope ./kubescope ./kubescope

RUN poetry install --without dev

CMD ["poetry", "run", "uvicorn", "kubescope.main:app", "--host", "0.0.0.0", "--port", "8000"]

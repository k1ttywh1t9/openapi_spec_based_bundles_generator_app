# Указываем, что корень для импортов Python — это папка app
export PYTHONPATH := app

POETRY = poetry run
PYTHON = $(POETRY) python

.PHONY: help worker cli test

help:
	@echo "Доступные команды (запуск из корня репозитория):"
	@echo "  make worker          - Запустить фонового воркера (демона)"
	@echo "  make cli f=<путь>    - Загрузить OpenAPI спеку через CLI"
	@echo "  make test            - Запустить тесты"

# 1. Запуск воркера (модуль ищется внутри app/ благодаря PYTHONPATH)
worker:
	$(PYTHON) -m application.worker.main

# 2. Загрузка спеки через CLI
cli:
	@if [ -z "$(f)" ]; then \
		echo "Ошибка: Укажи путь к файлу через f=... Пример: make cli f=./openapi.json"; \
		exit 1; \
	fi
	$(PYTHON) -m application.cli.upload_spec --file $(f) $(if $(t),--title "$(t)",)

# 3. Прогон тестов
test:
	$(POETRY) pytest app/ -s -v
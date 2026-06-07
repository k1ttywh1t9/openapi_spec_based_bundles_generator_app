# Команда для запуска всего проекта
.PHONY: run monitor

# Запуск генератора
run:
	poetry run python main.py

# Мониторинг "снаружи" (без изменения кода)
monitor:
	@echo "--- Запуск мониторинга процессов и файлов ---"
	@# Открываем панель с логированием, мониторингом нагрузки и счетчиком файлов
	@tmux new-session -d 'tail -f debug.log' \; \
		split-window -h 'glances' \; \
		split-window -v 'watch -n 1 "find generated_code -type f | wc -l"' \; \
		attach
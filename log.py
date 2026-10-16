import logging as l

l.basicConfig(
    level=l.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

l.debug("Отладочная информация") # лог 1 уровня
l.info("Приложение запущено") # лог 2 уровня
l.warning("Внимание: низкий уровень диска") # лог 3 уровня
l.error("Не удалось подключиться к БД") # лог 4 уровня
l.critical("Критическая ошибка: остановка работы") # лог 5 уровня